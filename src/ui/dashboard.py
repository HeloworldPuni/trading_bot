
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from rich.text import Text
from rich import box
import datetime

class Dashboard:
    def __init__(self):
        self.console = Console()
        self.layout = Layout()
        self._setup_layout()

    def _setup_layout(self):
        self.layout.split(
            Layout(name="header", size=3),
            Layout(name="main", ratio=1),
            Layout(name="footer", size=10)
        )
        self.layout["main"].split_row(
            Layout(name="left", ratio=2),
            Layout(name="right", ratio=1)
        )

    def generate_renderable(self, portfolio_summary: dict, active_positions: list, recent_history: list, latest_signal: dict = None):
        # Calculate used in positions
        used_in_positions = sum(p.get('margin_used', p['size_usd'] / p.get('leverage', 1)) for p in active_positions)
        available_balance = portfolio_summary['balance']
        
        # Calculate trade stats from history
        total_trades = len(recent_history)
        wins = sum(1 for t in recent_history if t.get('realized_pnl_usd', 0) > 0)
        win_rate = (wins / total_trades * 100) if total_trades > 0 else 0
        total_pnl = sum(t.get('realized_pnl_usd', 0) for t in recent_history)
        pnl_color = "green" if total_pnl >= 0 else "red"
        
        # 1. Header (Stats + Portfolio)
        header_text = Text.assemble(
            (" 🤖 AI TRADING BOT ", "bold white on blue"),
            "  ",
            (f"W/L: {wins}/{total_trades - wins}", "cyan"),
            " ",
            (f"({win_rate:.0f}%)", "bold cyan"),
            "  |  ",
            (f"PnL: ${total_pnl:+.2f}", f"bold {pnl_color}"),
            "  |  ",
            (f"Equity: ${portfolio_summary['equity']:,.2f}", "yellow"),
            "  |  ",
            (f"Open: {len(active_positions)}", "magenta")
        )
        
        # 2. Left: Active Positions Table
        pos_table = Table(title="Live Positions", box=box.ROUNDED, expand=True)
        pos_table.add_column("Symbol", style="bold")
        pos_table.add_column("Side", justify="center")
        pos_table.add_column("Entry")
        pos_table.add_column("TP", style="green")
        pos_table.add_column("SL", style="red")
        pos_table.add_column("Size", justify="right")
        pos_table.add_column("Lev", justify="center")
        pos_table.add_column("PnL ($)", justify="right")
        pos_table.add_column("PnL (%)", justify="right")

        for pos in active_positions:
            pnl_col = "green" if pos['unrealized_pnl_usd'] >= 0 else "red"
            side_col = "green" if pos['direction'] == "LONG" else "red"
            leverage = pos.get('leverage', 1)
            tp = pos.get('tp', 0)
            sl = pos.get('sl', 0)
            
            pos_table.add_row(
                pos['symbol'],
                Text(pos['direction'], style=side_col),
                f"{pos['entry_price']:.2f}",
                f"{tp:.2f}",
                f"{sl:.2f}",
                f"${pos['size_usd']:.0f}",
                Text(f"{leverage}x", style="cyan"),
                Text(f"${pos['unrealized_pnl_usd']:.2f}", style=pnl_col),
                Text(f"{pos['unrealized_pnl_pct']:.2f}%", style=pnl_col)
            )

        # 3. Right: Latest Signal / Market Info
        signal_panel = Panel(
            Text(f"Latest Analysis @ {datetime.datetime.now().strftime('%H:%M:%S')}\n\n" + 
                 (f"Signal: {latest_signal['strategy']}\nSide: {latest_signal['direction']}\nConf: {latest_signal['confidence']:.4f}\nReason: {latest_signal['reasoning']}" if latest_signal else "Waiting for next cycle..."),
                 style="italic"),
            title="Registry Feed", border_style="blue"
        )

        # 4. Footer: Recent History with Realized ROI
        realized_pnl = sum(h.get('realized_pnl_usd', 0) for h in recent_history)
        initial_cap = portfolio_summary.get('initial_capital', 10000)
        realized_roi = (realized_pnl / initial_cap * 100) if initial_cap > 0 else 0
        
        roi_text = f"Realized ROI: {realized_roi:+.2f}%" if recent_history else "No closed trades yet"
        hist_table = Table(title=f"Trade History (Last 5) | {roi_text}", box=box.SIMPLE, expand=True)
        hist_table.add_column("Time")
        hist_table.add_column("Symbol")
        hist_table.add_column("Result", justify="right")
        hist_table.add_column("Exit Reason")

        for h in recent_history[-5:]:
            res_col = "green" if h['realized_pnl_usd'] >= 0 else "red"
            hist_table.add_row(
                datetime.datetime.now().strftime("%H:%M"), # Mock or real ts
                h['symbol'],
                Text(f"{h['realized_pnl_pct']:.2f}%", style=res_col),
                h['exit_reason']
            )

        # Assemble
        self.layout["header"].update(Panel(header_text, style="white on black"))
        self.layout["left"].update(pos_table)
        self.layout["right"].update(signal_panel)
        self.layout["footer"].update(hist_table)

        return self.layout
