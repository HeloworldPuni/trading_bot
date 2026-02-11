
import json
import os
import logging
from typing import Dict, Any, Optional
from datetime import datetime, UTC

logger = logging.getLogger(__name__)

class ModelRegistry:
    def __init__(self, registry_path: Optional[str] = None):
        if registry_path is None:
            # Use absolute path relative to project root (2 levels up from src/ml/registry.py)
            root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
            self.registry_path = os.path.join(root, "models", "registry.json")
        else:
            self.registry_path = registry_path
            
        self.data = {
            "active_version": None,
            "models": {},
            "total_records_at_last_train": 0
        }
        self._load()

    def _load(self):
        if os.path.exists(self.registry_path):
            with open(self.registry_path, "r", encoding="utf-8") as f:
                self.data = json.load(f)
            logger.info(f"Registry: Loaded from {self.registry_path}")
        else:
            logger.warning(f"Registry: File not found at {self.registry_path}. Initializing new.")
            self._save()

    def _save(self):
        os.makedirs(os.path.dirname(self.registry_path), exist_ok=True)
        with open(self.registry_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)

    def register_model(self, version: str, path: str, metrics: Dict[str, float], record_count: int):
        self.data["models"][version] = {
            "type": "single",
            "path": path,
            "metrics": metrics,
            "trained_at": datetime.now(UTC).isoformat(),
            "record_count": record_count
        }
        self._save()
        logger.info(f"Registry: Registered model {version} with AUC: {metrics.get('test_roc_auc', 0):.4f}")

    def register_ensemble(self, version: str, specialized_models: Dict[str, Dict[str, Any]], record_count: int):
        """
        Registers a set of regime-specific models.
        specialized_models: { 'bull': { 'path': ..., 'metrics': ... }, ... }
        """
        self.data["models"][version] = {
            "type": "ensemble",
            "experts": specialized_models,
            "trained_at": datetime.now(UTC).isoformat(),
            "record_count": record_count
        }
        self._save()
        logger.info(f"Registry: Registered ensemble version {version} with {len(specialized_models)} experts.")

    def promote_model(self, version: str, total_records: int):
        if version in self.data["models"]:
            self.data["active_version"] = version
            self.data["total_records_at_last_train"] = total_records
            self._save()
            logger.info(f"Registry: Promoted model {version} to ACTIVE.")
        else:
            logger.error(f"Registry: Cannot promote unknown version {version}")

    def get_active_model_path(self) -> Optional[str]:
        version = self.data.get("active_version")
        if version and version in self.data["models"]:
            model_info = self.data["models"][version]
            if model_info.get("type") == "ensemble":
                return None
            return model_info.get("path")
        return None

    def get_active_metrics(self) -> Optional[Dict[str, float]]:
        version = self.data.get("active_version")
        if version and version in self.data["models"]:
            return self.data["models"][version].get("metrics")
        return None

    def get_active_experts(self) -> Optional[Dict[str, Dict[str, Any]]]:
        """Returns the experts dictionary for the currently active ensemble."""
        version = self.data.get("active_version")
        if version and version in self.data["models"]:
            model_info = self.data["models"][version]
            if model_info.get("type") == "ensemble":
                return model_info.get("experts")
        return None

    def update_expert(self, ensemble_version: str, regime_key: str, path: str, metrics: Dict[str, float]):
        """Updates a specific expert within an ensemble version."""
        if ensemble_version not in self.data["models"]:
            # If creating a new ensemble version for updates
            self.data["models"][ensemble_version] = {
                "type": "ensemble",
                "experts": {},
                "trained_at": datetime.now(UTC).isoformat(),
                "record_count": self.data.get("total_records_at_last_train", 0)
            }
        
        self.data["models"][ensemble_version]["experts"][regime_key] = {
            "path": path,
            "metrics": metrics
        }
        self._save()
        logger.info(f"Registry: Updated expert '{regime_key}' in ensemble {ensemble_version}")

    def get_last_trained_count(self) -> int:
        return self.data.get("total_records_at_last_train", 0)

    def get_next_version(self) -> str:
        count = len(self.data["models"]) + 1
        return f"v{count}"
