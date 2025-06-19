"""
ATR-Indikator (Average True Range)
"""


def atr(candles, period=14):
    trs = []
    for i in range(1, len(candles)):
        high = candles[i]["high"]
        low = candles[i]["low"]
        close_prev = candles[i - 1]["close"]
        tr = max(high - low, abs(high - close_prev), abs(low - close_prev))
        trs.append(tr)
    if len(trs) < period:
        return None
    return sum(trs[-period:]) / period
