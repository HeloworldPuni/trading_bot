"""
Runtime schema validator for orchestrator <-> specialist agent messages.

This module validates:
1) Message envelope
2) Payload by message type
3) Cross-field safety rules from the implementation plan
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional


class SchemaValidationError(ValueError):
    """Raised when an agent message fails validation."""

    def __init__(self, errors: List[str]):
        self.errors = errors
        super().__init__("Message validation failed: " + "; ".join(errors))


@dataclass
class ValidationResult:
    valid: bool
    errors: List[str]


class AgentSchemaValidator:
    """
    Lightweight JSON-schema-like validator for the project schemas.

    The validator intentionally supports only the schema features used by:
    - schemas/agents/message_envelope.schema.json
    - schemas/agents/task_assignment.payload.schema.json
    - schemas/agents/task_result.payload.schema.json
    - schemas/agents/decision_packet.payload.schema.json
    """

    def __init__(self, schema_dir: Optional[str] = None):
        if schema_dir is None:
            schema_dir = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "..", "..", "schemas", "agents")
            )
        self.schema_dir = schema_dir

        self.schemas: Dict[str, Dict[str, Any]] = {
            "envelope": self._load_schema("message_envelope.schema.json"),
            "task_assignment": self._load_schema("task_assignment.payload.schema.json"),
            "task_result": self._load_schema("task_result.payload.schema.json"),
            "decision_packet": self._load_schema("decision_packet.payload.schema.json"),
        }

        # Challenge request/response reuse existing payload contracts until dedicated schemas are added.
        self.payload_schema_by_message_type: Dict[str, str] = {
            "TASK_ASSIGNMENT": "task_assignment",
            "TASK_RESULT": "task_result",
            "CHALLENGE_REQUEST": "task_assignment",
            "CHALLENGE_RESPONSE": "task_result",
            "DECISION_PACKET": "decision_packet",
        }

    def _load_schema(self, filename: str) -> Dict[str, Any]:
        path = os.path.join(self.schema_dir, filename)
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def validate_message(self, message: Dict[str, Any]) -> ValidationResult:
        errors: List[str] = []

        errors.extend(self._validate_node(message, self.schemas["envelope"], "message"))

        message_type = message.get("message_type")
        payload = message.get("payload")
        payload_schema_name = self.payload_schema_by_message_type.get(str(message_type))
        if payload_schema_name is not None:
            payload_schema = self.schemas[payload_schema_name]
            errors.extend(self._validate_node(payload, payload_schema, "payload"))

        errors.extend(self._validate_cross_rules(message_type=str(message_type), payload=payload))

        return ValidationResult(valid=len(errors) == 0, errors=errors)

    def assert_valid_message(self, message: Dict[str, Any]) -> None:
        result = self.validate_message(message)
        if not result.valid:
            raise SchemaValidationError(result.errors)

    def _validate_cross_rules(self, message_type: str, payload: Any) -> List[str]:
        errors: List[str] = []
        if not isinstance(payload, dict):
            return errors

        if message_type in {"TASK_RESULT", "CHALLENGE_RESPONSE"}:
            claims = payload.get("claims")
            evidence = payload.get("evidence")
            if isinstance(claims, list) and len(claims) > 0 and isinstance(evidence, list) and len(evidence) == 0:
                errors.append(
                    "payload.evidence must be non-empty when payload.claims is non-empty."
                )

        if message_type == "DECISION_PACKET":
            final_action = payload.get("final_action")
            risk_veto = payload.get("risk_veto", {})
            vetoed = isinstance(risk_veto, dict) and bool(risk_veto.get("vetoed"))

            if vetoed and final_action not in {"WAIT", "EXECUTE_REDUCED"}:
                errors.append(
                    "payload.final_action must be WAIT or EXECUTE_REDUCED when risk_veto.vetoed=true."
                )

            disagreements = payload.get("disagreements", [])
            confidence = payload.get("confidence")
            if (
                isinstance(confidence, (int, float))
                and confidence < 0.55
                and isinstance(disagreements, list)
                and len(disagreements) > 0
                and final_action not in {"WAIT", "INSUFFICIENT_DATA"}
            ):
                errors.append(
                    "payload.final_action must be WAIT or INSUFFICIENT_DATA when disagreements exist and confidence < 0.55."
                )

        return errors

    def _validate_node(self, value: Any, schema: Dict[str, Any], path: str) -> List[str]:
        errors: List[str] = []

        expected_type = schema.get("type")
        if expected_type is not None and not self._matches_type(value, expected_type):
            expected = (
                ", ".join(expected_type)
                if isinstance(expected_type, list)
                else str(expected_type)
            )
            errors.append(f"{path} expected type [{expected}], got {type(value).__name__}.")
            return errors

        if "enum" in schema and value not in schema["enum"]:
            errors.append(f"{path} must be one of {schema['enum']}, got {value!r}.")

        if isinstance(value, str):
            min_len = schema.get("minLength")
            if isinstance(min_len, int) and len(value) < min_len:
                errors.append(f"{path} length must be >= {min_len}.")

            fmt = schema.get("format")
            if fmt == "date-time" and not self._is_datetime(value):
                errors.append(f"{path} must be ISO-8601 date-time.")

        if isinstance(value, (int, float)) and not isinstance(value, bool):
            minimum = schema.get("minimum")
            maximum = schema.get("maximum")
            if isinstance(minimum, (int, float)) and value < minimum:
                errors.append(f"{path} must be >= {minimum}.")
            if isinstance(maximum, (int, float)) and value > maximum:
                errors.append(f"{path} must be <= {maximum}.")

        if isinstance(value, list):
            min_items = schema.get("minItems")
            if isinstance(min_items, int) and len(value) < min_items:
                errors.append(f"{path} must contain at least {min_items} item(s).")

            item_schema = schema.get("items")
            if isinstance(item_schema, dict):
                for idx, item in enumerate(value):
                    errors.extend(self._validate_node(item, item_schema, f"{path}[{idx}]"))

        if isinstance(value, dict):
            required = schema.get("required", [])
            if isinstance(required, list):
                for req in required:
                    if req not in value:
                        errors.append(f"{path}.{req} is required.")

            properties = schema.get("properties", {})
            if isinstance(properties, dict):
                for key, item in value.items():
                    if key in properties:
                        errors.extend(
                            self._validate_node(item, properties[key], f"{path}.{key}")
                        )
                    else:
                        additional = schema.get("additionalProperties", True)
                        if additional is False:
                            errors.append(f"{path}.{key} is not allowed.")

        return errors

    @staticmethod
    def _matches_type(value: Any, expected_type: Any) -> bool:
        if isinstance(expected_type, list):
            return any(AgentSchemaValidator._matches_type(value, t) for t in expected_type)

        type_name = str(expected_type)
        if type_name == "object":
            return isinstance(value, dict)
        if type_name == "array":
            return isinstance(value, list)
        if type_name == "string":
            return isinstance(value, str)
        if type_name == "number":
            return isinstance(value, (int, float)) and not isinstance(value, bool)
        if type_name == "integer":
            return isinstance(value, int) and not isinstance(value, bool)
        if type_name == "boolean":
            return isinstance(value, bool)
        if type_name == "null":
            return value is None
        return False

    @staticmethod
    def _is_datetime(value: str) -> bool:
        try:
            datetime.fromisoformat(value.replace("Z", "+00:00"))
            return True
        except Exception:
            return False

