
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from rich.text import Text
from rich import box
import datetime


def _format_trade_time(trade: dict) -> str:
    ts = (
        trade.get("exit_time")
        or trade.get("closed_at")
        or trade.get("timestamp")
        or trade.get("entry_time")
    )
    if not ts:
        return "--:--"
    try:
        dt = datetime.datetime.fromisoformat(str(ts).replace("Z", "+00:00"))
        return dt.strftime("%H:%M")
    except Exception:
        return "--:--"

class Dashboard:
    def __init__(self):
        self.console = Console()
        self.layout = Layout()
        self._setup_layout()
        self._set_placeholder_view()

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

    def _set_placeholder_view(self):
        self.layout["header"].update(Panel("Starting bot...", style="white on black"))
        self.layout["left"].update(Panel("Waiting for first market scan...", title="Live Positions", border_style="blue"))
        self.layout["right"].update(Panel("Bootstrapping data feeds...", title="Registry Feed", border_style="blue"))
        self.layout["footer"].update(Panel("No trades yet.", title="Trade History", border_style="blue"))

    def generate_renderable(self, portfolio_summary: dict, active_positions: list, recent_history: list, 
                                latest_signal: dict = None, alerts: list = None, meta_learner_summary: dict = None):
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
            (f"Open: {len(active_positions)}", "magenta"),
            "  |  ",
            (f"DD: {portfolio_summary.get('drawdown_pct', 0.0):.1f}%", "red")
        )
        
        # 2. Left: Active Positions Table
        pos_table = Table(title="Live Positions", box=box.ROUNDED, expand=True)
        pos_table.add_column("Sym", style="bold", max_width=6)
        pos_table.add_column("Side", justify="center", width=4)
        pos_table.add_column("Ent", justify="right")
        pos_table.add_column("Cur", justify="right")
        pos_table.add_column("TP", style="green", justify="right")
        pos_table.add_column("SL", style="red", justify="right")
        pos_table.add_column("Size", justify="right")
        pos_table.add_column("PnL $", justify="right", min_width=8, no_wrap=True)
        pos_table.add_column("PnL %", justify="right", min_width=6, no_wrap=True)

        for pos in active_positions:
            pnl_col = "green" if pos['unrealized_pnl_usd'] >= 0 else "red"
            side_col = "green" if pos['direction'] == "LONG" else "red"
            side_text = "L" if pos['direction'] == "LONG" else "S"
            leverage = pos.get('leverage', 1)
            tp = pos.get('tp', 0)
            sl = pos.get('sl', 0)
            current_price = pos.get('current_price', pos['entry_price'])
            
            # Show trailing stop info when active
            if pos.get("trail_active"):
                tp_display = Text(f"🔥{pos.get('trail_sl', 0):.2f}", style="bright_yellow")
                sl_display = Text(f"TRAIL", style="bright_yellow")
            else:
                tp_display = f"{tp:.2f}"
                sl_display = f"{sl:.2f}"
            
            pos_table.add_row(
                pos['symbol'].split('/')[0],
                Text(side_text, style=side_col),
                f"{pos['entry_price']:.2f}",
                Text(f"{current_price:.2f}", style="yellow"),
                tp_display,
                sl_display,
                f"${pos['size_usd']:.0f}",
                Text(f"{pos['unrealized_pnl_usd']:+.1f}", style=pnl_col),
                Text(f"{pos['unrealized_pnl_pct']:+.1f}%", style=pnl_col)
            )

        # 3. Right: Latest Signal / Market Info / MetaLearner
        meta_info = ""
        if meta_learner_summary:
            meta_info = (
                f"\n\n--- Meta-Learning ---\n"
                f"Threshold: {meta_learner_summary['confidence_threshold']:.2f}\n"
                f"Recent WR: {meta_learner_summary['recent_win_rate']:.1%}\n"
                f"Top Loss: {meta_learner_summary['top_loss_category']}"
            )

        signal_panel = Panel(
            Text(f"Latest Analysis @ {datetime.datetime.now().strftime('%H:%M:%S')}\n\n" + 
                 (f"Symbol: {latest_signal.get('symbol', 'N/A')}\nSignal: {latest_signal['strategy']}\nSide: {latest_signal['direction']}\nConf: {latest_signal['confidence']:.4f}\nReason: {latest_signal['reasoning'][:100]}..." if latest_signal else "Waiting for next cycle...") +
                 meta_info,
                 style="italic"),
            title="Registry Feed", border_style="blue"
        )

        # 4. Footer: Recent History with Realized ROI
        realized_pnl = sum(h.get('realized_pnl_usd', 0) for h in recent_history)
        initial_cap = portfolio_summary.get('initial_capital', 10000)
        realized_roi = (realized_pnl / initial_cap * 100) if initial_cap > 0 else 0
        
        roi_text = f"Realized ROI: {realized_roi:+.2f}%" if recent_history else "No closed trades yet"
        alert_text = ""
        if alerts:
            alert_text = " | Alerts: " + ", ".join(alerts[:3])
        hist_table = Table(title=f"Trade History (Last 5) | {roi_text}{alert_text}", box=box.SIMPLE, expand=True)
        hist_table.add_column("Time")
        hist_table.add_column("Symbol")
        hist_table.add_column("Side", justify="center", width=4)
        hist_table.add_column("PnL $", justify="right")
        hist_table.add_column("PnL %", justify="right")
        hist_table.add_column("Exit Reason")

        for h in recent_history[-5:]:
            pnl_usd = float(h.get('realized_pnl_usd', 0))
            pnl_pct = float(h.get('realized_pnl_pct', 0))
            res_col = "green" if pnl_usd >= 0 else "red"
            direction = h.get('direction', 'N/A')
            side_text = "L" if direction == "LONG" else "S" if direction == "SHORT" else "?"
            side_col = "green" if direction == "LONG" else "red"
            hist_table.add_row(
                _format_trade_time(h),
                h.get('symbol', 'N/A'),
                Text(side_text, style=side_col),
                Text(f"${pnl_usd:+.2f}", style=res_col),
                Text(f"{pnl_pct:+.2f}%", style=res_col),
                h.get('exit_reason', 'N/A')
            )

        # Assemble
        self.layout["header"].update(Panel(header_text, style="white on black"))
        self.layout["left"].update(pos_table)
        self.layout["right"].update(signal_panel)
        self.layout["footer"].update(hist_table)

        return self.layout
