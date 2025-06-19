"""
RegimeDetector: Erkennt das Marktregime (Trend/Range/Spike/Neutral)
"""


class RegimeDetector:
    def __init__(self, asset_config):
        self.asset = asset_config["symbol"]

    def detect(self, market):
        # Beispiel-Logik, kann angepasst werden
        return "neutral"
