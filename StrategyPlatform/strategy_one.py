import numpy as np
from scipy.optimize import minimize
import torch

def get_past_data(stock_code, current_date, days=10):
    """
    Retrieve stock data for the past specified number of days.
    """
    pro = ts.pro_api(tushare_token)
    end_date = current_date
    start_date = (pd.to_datetime(current_date) - pd.Timedelta(days=days)).strftime('%Y%m%d')

    df = pro.daily(ts_code=stock_code, start_date=start_date, end_date=end_date)
    df.sort_values('trade_date', inplace=True)

    return df

def predict_return(model, data):
    """
    Use the model to predict returns.
    """
    # Assuming the model accepts input with shape (days, features) and returns expected returns
    return model.predict(data)

def optimize_portfolio(returns, risks, current_position):
    """
    Use mean-variance optimization to determine the weight of each stock.
    """
    num_assets = len(returns)

    def portfolio_variance(weights):
        return np.dot(weights.T, np.dot(risks, weights))

    def portfolio_return(weights):
        return np.dot(weights, returns)

    def objective(weights):
        return -portfolio_return(weights) + portfolio_variance(weights)

    constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}
    bounds = [(0, 1) for _ in range(num_assets)]
    initial_guess = np.array([1 / num_assets for _ in range(num_assets)])

    result = minimize(objective, initial_guess, bounds=bounds, constraints=constraints)

    return result.x

def run(stock_pool, current_date, current_position):
    buy_order_list = []
    sell_order_list = []

    # Expected returns predicted by the model
    expected_returns = []
    risks = []

    # Load model
    path = 'C:\\Users\\ROG\\PycharmProjects\\w3132-project\\Seed\\transformer_model.pth'
    model = torch.load(path)
    model.eval()

    for stock_code in stock_pool:
        past_data = get_past_data(stock_code, current_date)
        expected_return = model(past_data)

        # First, calculate the expected return
        expected_returns.append(expected_return)

        """
        Here, you can use multiple models to calculate a comprehensive expected return.
        """

        # Calculate the risk of each stock (e.g., historical volatility)
        risks.append(np.var(past_data['close']))

    # Select stocks with high expected returns and calculate how much of each stock should be sold based on their expected returns and volatility.
    risks_matrix = np.diag(risks)

    """
    The result returned here should be a portfolio indicating the weight of each stock:
    1. STOCK A 0.33
    2. STOCK B 0.34
    3. STOCK C 0.35
    4. Cash
    """
    weights = optimize_portfolio(expected_returns, risks_matrix, current_position)

    for i, stock_code in enumerate(stock_pool):
        if stock_code not in current_position:
            # If there is no position, buy
            buy_order_list.append({
                "code": stock_code,
                "shares": int(weights[i] * current_money / past_data['close'].iloc[-1]),
                "price": past_data['close'].iloc[-1]
            })
        else:
            current_shares = current_position[stock_code]['shares']
            target_shares = int(weights[i] * current_money / past_data['close'].iloc[-1])
            if target_shares > current_shares:
                buy_order_list.append({
                    "code": stock_code,
                    "shares": target_shares - current_shares,
                    "price": past_data['close'].iloc[-1]
                })
            elif target_shares < current_shares:
                sell_order_list.append({
                    "code": stock_code,
                    "shares": current_shares - target_shares,
                    "price": past_data['close'].iloc[-1]
                })

    return buy_order_list, sell_order_list