import pandas as pd

def backtest_strategy(data, signals):
    """Backtest trading strategy"""
    
    capital = 10000  # Initial capital
    position = 0  # Initial position
    portfolio_value = []  # Portfolio value over time

    for index, signal in signals.iterrows():
        if signal['Signal'] == -1:  # Short signal
            if position == 0:  # Open short position
                position = -1
                capital += data.loc[index, 'Adj Close'] * 100  # Assume shorting 100 shares
        else:  # No signal or long signal
            if position == -1:  # Close short position
                position = 0
                capital -= data.loc[index, 'Adj Close'] * 100  # Cover short position

        # Update portfolio value
        portfolio_value.append(capital)

    return pd.Series(portfolio_value, index=signals.index)


def calculate_drawdown(portfolio_value):
    """Calculate maximum drawdown"""
    rolling_max = portfolio_value.cummax()
    drawdown = (portfolio_value - rolling_max) / rolling_max
    return drawdown
