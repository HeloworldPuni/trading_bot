import asyncio
import logging
from src.core.notifications import NotificationManager
from src.config import Config

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("TestNotifications")

async def main():
    print("--- Testing Notification System ---")
    print(f"Discord Webhook: {'CONFIGURED' if Config.DISCORD_WEBHOOK_URL else 'MISSING'}")
    print(f"Telegram Bot:    {'CONFIGURED' if Config.TELEGRAM_BOT_TOKEN else 'MISSING'}")
    
    manager = NotificationManager()
    manager.start()
    
    print("\nSending test messages...")
    manager.send("This is a TEST INFO message.", level="INFO")
    manager.send("This is a TEST TRADE alert.", level="TRADE")
    manager.send("This is a TEST WARNING.", level="WARNING")
    
    print("Messages queued. Waiting for worker...")
    await asyncio.sleep(2)
    
    await manager.stop()
    print("Test complete.")

if __name__ == "__main__":
    asyncio.run(main())
