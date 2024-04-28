def grid_search_parameter(data, parameter_values, strategy_function, evaluate_function):
    """Grid search optimization of strategy parameters"""
    results = {}
    for value in parameter_values:
        signals = strategy_function(data, value)
        portfolio_value = backtest_strategy(data, signals)
        daily_returns = portfolio_value.pct_change().dropna()
        performance_metric = evaluate_function(daily_returns)
        results[value] = performance_metric
    return results
