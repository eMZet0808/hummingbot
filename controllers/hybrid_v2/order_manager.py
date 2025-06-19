"""
OrderManager: Entry, Exit, TP/SL, Trailing, Risk-Management
"""


class OrderManager:
    def __init__(self, asset_config):
        self.asset = asset_config["symbol"]
        self.tp = asset_config.get("tp", 1.0)
        self.sl = asset_config.get("sl", 0.5)
        self.trailing = asset_config.get("trailing", True)

    def decide_action(self, market, regime, spread):
        if regime == "trend" and spread < 1.0:
            return "enter_long"
        elif regime == "range" and spread < 1.5:
            return "enter_short"
        else:
            return "hold"

    def execute_action(self, action, market):
        if action == "enter_long":
            print(f"{self.asset}: Enter Long (Demo)")
        elif action == "enter_short":
            print(f"{self.asset}: Enter Short (Demo)")
        elif action == "hold":
            pass

    def on_fill(self, order_event):
        pass
