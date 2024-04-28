import pandas as pd

def calculate_bollinger_bands(data, window_size=20):
    """Calculate Bollinger Bands"""
    rolling_mean = data['Adj Close'].rolling(window=window_size).mean()
    rolling_std = data['Adj Close'].rolling(window=window_size).std()
    upper_band = rolling_mean + (rolling_std * 2)
    lower_band = rolling_mean - (rolling_std * 2)
    return upper_band, lower_band

def calculate_rsi(data, window_size=14):
    """Calculate Relative Strength Index (RSI)"""
    delta = data['Adj Close'].diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=window_size).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window_size).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_atr(data, window_size=14):
    """Calculate Average True Range (ATR)"""
    tr1 = data['High'] - data['Low']
    tr2 = abs(data['High'] - data['Close'].shift())
    tr3 = abs(data['Low'] - data['Close'].shift())
    tr = pd.concat([tr1, tr2, tr3], axis=1)
    true_range = tr.max(axis=1)
    atr = true_range.rolling(window=window_size).mean()
    return atr

def generate_signals(data, upper_band, lower_band, rsi, atr):
    """Generate trading signals"""
    signals = pd.DataFrame(index=data.index)
    signals['Signal'] = 0
    signals.loc[data['Adj Close'] > upper_band, 'Signal'] = -1  # Short signal
    return signals
    