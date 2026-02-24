
import subprocess
import time
import sys
import os
import signal
from datetime import datetime

# Configuration
BOT_SCRIPT = "main.py"
RESTART_DELAY = 10  # Seconds to wait before restarting
MAX_RESTARTS_PER_HOUR = 5

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [WATCHDOG] {message}")

def run_bot():
    """Starts the bot process and waits for it to finish."""
    python_executable = sys.executable
    cmd = [python_executable, BOT_SCRIPT] 
    
    log(f"Starting bot: {' '.join(cmd)}")
    
    # Start the process
    process = subprocess.Popen(
        cmd,
        cwd=os.getcwd(),
        stdout=sys.stdout,
        stderr=sys.stderr
    )
    
    return process

def main():
    log("Watchdog initiated. rigorous monitoring engaged.")
    
    restart_history = []
    
    while True:
        # Clean up old restart timestamps (older than 1 hour)
        now = time.time()
        restart_history = [t for t in restart_history if now - t < 3600]
        
        if len(restart_history) >= MAX_RESTARTS_PER_HOUR:
            log("CRITICAL: Too many restarts in the last hour. Aborting watchdog to prevent loop.")
            break
            
        process = run_bot()
        
        try:
            # Wait for the bot to exit
            return_code = process.wait()
            
            if return_code == 0:
                log("Bot exited gracefully (code 0). Watchdog stopping.")
                break
            else:
                log(f"Bot crashed with exit code {return_code}.")
                
        except KeyboardInterrupt:
            log("Watchdog stopped by user. Terminating bot...")
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
            break
            
        # Record restart
        restart_history.append(time.time())
        log(f"Restarting in {RESTART_DELAY} seconds...")
        time.sleep(RESTART_DELAY)

def run_scheduler():
    """Runs the session report every 24 hours."""
    import threading
    
    def job():
        while True:
            # Calculate time until next run (e.g., 00:00 UTC or just every 24h from now)
            # For simplicity, we just run it every 24h from start, or we could target a specific time.
            # User asked "every 24hr", let's just sleep 24h.
            # Ideally we run it once immediately if requested, but let's stick to a loop.
            time.sleep(24 * 3600) 
            
            log("Running daily session report...")
            try:
                # Use the same python executable
                subprocess.run([sys.executable, "scripts/session_report.py"], check=False)
            except Exception as e:
                log(f"Failed to run session report: {e}")

    t = threading.Thread(target=job, daemon=True)
    t.start()
    log("Daily report scheduler started (cycle: 24h).")

if __name__ == "__main__":
    run_scheduler()
    main()
