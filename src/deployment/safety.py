
import hashlib
import logging
import os
from typing import Dict, List

logger = logging.getLogger(__name__)

class SafetyLock:
    """
    Phase 11 Retrofit: Runtime Configuration Integrity.
    Prevents unauthorized config changes during operation.
    """
    def __init__(self, config_paths: List[str]):
        self.config_paths = config_paths
        self.hashes: Dict[str, str] = {}
        self._snapshot_configs()
        
    def _snapshot_configs(self):
        for path in self.config_paths:
            if os.path.exists(path):
                self.hashes[path] = self._get_hash(path)
                logger.debug(f"Locked config: {path}")
            else:
                logger.warning(f"Config path not found: {path}")

    def _get_hash(self, path: str) -> str:
        sha256 = hashlib.sha256()
        try:
            with open(path, 'rb') as f:
                while True:
                    data = f.read(65536)
                    if not data:
                        break
                    sha256.update(data)
            return sha256.hexdigest()
        except Exception as e:
            logger.error(f"Hashing failed for {path}: {e}")
            return ""

    def check_integrity(self) -> bool:
        """
        Verifies that config files haven't changed since startup.
        """
        all_safe = True
        for path, original_hash in self.hashes.items():
            current_hash = self._get_hash(path)
            if current_hash != original_hash:
                logger.critical(f"🔥 INTEGRITY BREACH: {path} modified during runtime!")
                all_safe = False
        
        return all_safe
