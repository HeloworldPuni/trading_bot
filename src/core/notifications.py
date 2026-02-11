import asyncio
import logging
from typing import Optional

logger = logging.getLogger(__name__)


class NotificationManager:
    """
    Minimal async notification manager used by utility scripts.
    """

    def __init__(self):
        self._queue: asyncio.Queue = asyncio.Queue()
        self._task: Optional[asyncio.Task] = None
        self._running = False

    async def _worker(self):
        while self._running:
            try:
                item = await self._queue.get()
                if item is None:
                    break
                message, level = item
                logger.info("[NOTIFY][%s] %s", level, message)
            except Exception as e:
                logger.warning("Notification worker error: %s", e)

    def start(self):
        if self._running:
            return
        self._running = True
        loop = asyncio.get_event_loop()
        self._task = loop.create_task(self._worker())

    def send(self, message: str, level: str = "INFO"):
        if not self._running:
            self.start()
        try:
            self._queue.put_nowait((message, level))
        except Exception:
            logger.info("[NOTIFY][%s] %s", level, message)

    async def stop(self):
        if not self._running:
            return
        self._running = False
        await self._queue.put(None)
        if self._task:
            await self._task
            self._task = None
