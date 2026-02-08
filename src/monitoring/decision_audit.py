"""
Decision Audit Logger - Solution #3
Tracks which systems influenced each trading decision for debugging.
"""
import json
import os
import logging
from dataclasses import dataclass, field, asdict
from typing import Optional, Dict, Any, List
from datetime import datetime, timezone

logger = logging.getLogger(__name__)


@dataclass
class DecisionAudit:
    """Complete audit trail for a single trading decision."""
    decision_id: str
    timestamp: str = ""
    symbol: str = ""
    
    # Final outcome
    action: str = "WAIT"
    direction: str = "FLAT"
    strategy: str = "WAIT"
    
    # What influenced the decision
    ml_confidence: Optional[float] = None
    ml_passed: bool = False
    
    ev_value: Optional[float] = None
    ev_passed: bool = True
    
    strategy_weight: float = 1.0
    strategy_blocked: bool = False
    
    regime: str = ""
    regime_confidence: float = 1.0
    
    # Risk filters
    risk_state: str = "SAFE"
    drawdown_pct: float = 0.0
    open_positions: int = 0
    position_blocked: bool = False
    
    # Signal quality
    rsi: float = 50.0
    trend_spread: float = 0.0
    htf_trend_spread: float = 0.0
    volume_zscore: float = 0.0
    
    # Override reasons
    blocked_reasons: List[str] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class DecisionAuditor:
    """
    Logs detailed audit trails for trading decisions.
    Answers the question: "Why did the bot do X?"
    """
    
    def __init__(self, log_path: str = "data/decision_audit.jsonl"):
        self.log_path = log_path
        os.makedirs(os.path.dirname(log_path), exist_ok=True)
    
    def create_audit(self, decision_id: str, symbol: str = "") -> DecisionAudit:
        """Start a new audit trail for a decision."""
        return DecisionAudit(
            decision_id=decision_id,
            timestamp=datetime.now(timezone.utc).isoformat(),
            symbol=symbol
        )
    
    def log_ml_result(self, audit: DecisionAudit, confidence: float, threshold: float):
        """Record ML model prediction."""
        audit.ml_confidence = confidence
        audit.ml_passed = confidence >= threshold
        if not audit.ml_passed:
            audit.blocked_reasons.append(f"ML confidence {confidence:.3f} < {threshold}")
    
    def log_ev_result(self, audit: DecisionAudit, ev_value: float, threshold: float):
        """Record expected value calculation."""
        audit.ev_value = ev_value
        audit.ev_passed = ev_value >= threshold
        if not audit.ev_passed:
            audit.blocked_reasons.append(f"EV {ev_value:.4f} < {threshold}")
    
    def log_strategy_filter(self, audit: DecisionAudit, strategy: str, weight: float, blocked: bool, reason: str = ""):
        """Record strategy filtering result."""
        audit.strategy = strategy
        audit.strategy_weight = weight
        audit.strategy_blocked = blocked
        if blocked:
            audit.blocked_reasons.append(f"Strategy {strategy} blocked: {reason}")
    
    def log_risk_state(self, audit: DecisionAudit, risk_state: str, drawdown: float, open_positions: int, max_positions: int):
        """Record risk state."""
        audit.risk_state = risk_state
        audit.drawdown_pct = drawdown
        audit.open_positions = open_positions
        audit.position_blocked = open_positions >= max_positions
        if audit.position_blocked:
            audit.blocked_reasons.append(f"Max positions ({max_positions}) reached")
        if risk_state == "DANGER":
            audit.blocked_reasons.append(f"Risk state DANGER (drawdown {drawdown:.1f}%)")
    
    def log_market_context(self, audit: DecisionAudit, regime: str, regime_confidence: float,
                           rsi: float, trend_spread: float, htf_trend_spread: float, volume_zscore: float):
        """Record market context."""
        audit.regime = regime
        audit.regime_confidence = regime_confidence
        audit.rsi = rsi
        audit.trend_spread = trend_spread
        audit.htf_trend_spread = htf_trend_spread
        audit.volume_zscore = volume_zscore
    
    def log_final_action(self, audit: DecisionAudit, action: str, direction: str):
        """Record final action taken."""
        audit.action = action
        audit.direction = direction
    
    def save(self, audit: DecisionAudit):
        """Persist audit to JSONL file."""
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(audit.to_dict()) + "\n")
    
    def get_recent(self, count: int = 20) -> List[Dict[str, Any]]:
        """Get recent audit entries for debugging."""
        if not os.path.exists(self.log_path):
            return []
        
        with open(self.log_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        recent = []
        for line in lines[-count:]:
            try:
                recent.append(json.loads(line.strip()))
            except json.JSONDecodeError:
                continue
        return recent
    
    def explain_last_decision(self) -> str:
        """Human-readable explanation of the last decision."""
        recent = self.get_recent(1)
        if not recent:
            return "No recent decisions found."
        
        d = recent[0]
        lines = [
            f"Decision: {d['decision_id'][:8]}... at {d['timestamp']}",
            f"Symbol: {d['symbol']} | Regime: {d['regime']}",
            f"Action: {d['action']} {d['direction']}",
            f"ML Confidence: {d['ml_confidence']:.3f} ({'✅' if d['ml_passed'] else '❌'})" if d['ml_confidence'] else "ML: N/A",
            f"EV: {d['ev_value']:.4f} ({'✅' if d['ev_passed'] else '❌'})" if d['ev_value'] else "EV: N/A",
            f"Strategy: {d['strategy']} (weight={d['strategy_weight']:.2f}) {'🚫 BLOCKED' if d['strategy_blocked'] else ''}",
            f"Risk: {d['risk_state']} | DD: {d['drawdown_pct']:.1f}% | Positions: {d['open_positions']}",
        ]
        
        if d['blocked_reasons']:
            lines.append("BLOCKED BY: " + ", ".join(d['blocked_reasons']))
        
        return "\n".join(lines)


# Global instance for easy access
_auditor = None

def get_auditor(log_path: str = "data/decision_audit.jsonl") -> DecisionAuditor:
    global _auditor
    if _auditor is None:
        _auditor = DecisionAuditor(log_path)
    return _auditor
