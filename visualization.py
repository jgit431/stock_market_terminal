import matplotlib.pyplot as plt

def plot_signals(data, signals, upper_band=None, lower_band=None, rsi=None, atr=None):
    """Plot stock data and trading signals"""
    plt.figure(figsize=(12, 8))
    plt.plot(data.index, data['Adj Close'], label='Adjusted Close Price')
    if upper_band is not None and lower_band is not None:
        plt.plot(data.index, upper_band, label='Upper Band', linestyle='--')
        plt.plot(data.index, lower_band, label='Lower Band', linestyle='--')
    if rsi is not None:
        plt.plot(data.index, rsi, label='RSI', color='purple')
        plt.axhline(y=70, color='r', linestyle='--', label='Overbought Threshold')
        plt.axhline(y=30, color='g', linestyle='--', label='Oversold Threshold')
    if atr is not None:
        plt.plot(data.index, atr, label='ATR', color='blue')
    plt.scatter(data.index, data['Adj Close'], marker='o', color='red', label='Short Signal')
    plt.title('Stock Data and Trading Signals')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

def plot_backtest_results(portfolio_value, drawdown):
    """Plot backtest results"""
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(portfolio_value, label='Portfolio Value', color='blue')
    plt.title('Portfolio Value')
    plt.xlabel('Date')
    plt.ylabel('Portfolio Value')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(drawdown, label='Drawdown', color='red')
    plt.title('Maximum Drawdown')
    plt.xlabel('Date')
    plt.ylabel('Drawdown')
    plt.legend()

    plt.tight_layout()
    plt.show()
