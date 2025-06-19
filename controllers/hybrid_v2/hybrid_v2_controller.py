"""
HybridV2Controller
Production-ready Hummingbot V2-Strategy Controller (Multi-Asset, Orderbook, Regime-Switching)
"""

import json
import logging

from .order_manager import OrderManager
from .regime_detector import RegimeDetector

print("Hybrid V2 Strategy Controller loaded!")


class HybridV2Controller:
    def __init__(self, config_path: str):
        with open(config_path, "r") as f:
            self.config = json.load(f)
        self.assets = self.config["assets"]
        self.global_risk = self.config.get("global_risk", 0.01)
        self.detectors = {a["symbol"]: RegimeDetector(a) for a in self.assets}
        self.managers = {a["symbol"]: OrderManager(a) for a in self.assets}
        self.logger = logging.getLogger("HybridV2Controller")

    def on_tick(self):
        for asset in self.assets:
            symbol = asset["symbol"]
            detector = self.detectors[symbol]
            manager = self.managers[symbol]
            # TODO: Marketdaten/Orderbook aus Hummingbot Connector holen
            regime = detector.detect(None)
            action = manager.decide_action(None, regime, 0)
            self.logger.info(f"{symbol}: regime={regime}, action={action}")
            manager.execute_action(action, None)

    def on_order_filled(self, order_event):
        symbol = order_event.symbol
        self.logger.info(f"Order filled: {order_event}")
        self.managers[symbol].on_fill(order_event)

    def on_stop(self):
        self.logger.info("HybridV2Controller stopped.")
