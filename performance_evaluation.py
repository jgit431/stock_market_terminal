def calculate_sharpe_ratio(daily_returns):
    """Calculate Sharpe ratio"""
    return (daily_returns.mean() / daily_returns.std()) * (252 ** 0.5)

def calculate_sortino_ratio(daily_returns, target_return=0):
    """Calculate Sortino ratio"""
    downside_returns = daily_returns[daily_returns < target_return]
    downside_deviation = downside_returns.std()
    return (daily_returns.mean() - target_return) / downside_deviation

def calculate_calmar_ratio(daily_returns, max_drawdown):
    """Calculate Calmar ratio"""
    return daily_returns.mean() / abs(max_drawdown)
