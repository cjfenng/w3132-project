import pandas as pd
import numpy as np

# Load stock data for the given time period
# This should be a DataFrame containing columns: 'date', 'stock', 'open', 'close', etc.

# Define the stock pool
stock_pool = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']  # Example stock codes

# Define the trading time period
start_date = '2023-07-01'
end_date = '2023-08-31'

# Simulate backtesting for August
backtest_start_date = '2023-08-01'

# Function to predict the return for the next two days using past 10 days' data
def predict_future_two_days_return(past_10_days):
    # Implement your prediction model here
    # This is a placeholder for the actual model
    # Assuming the predicted return is the simple moving average
    predicted_return = (past_10_days['close'].iloc[-1] - past_10_days['close'].iloc[0]) / past_10_days['close'].iloc[0]
    return predicted_return

# Prepare a DataFrame to store the results
results = []

# Iterate through each stock in the stock pool
for stock in stock_pool:
    # Filter the data for this stock and the trading period
    stock_data = data[(data['stock'] == stock) & (data['date'] >= start_date) & (data['date'] <= end_date)]

    # Iterate through the stock data to make predictions
    for i in range(10, len(stock_data) - 1):
        # Get the past 10 days of data
        past_10_days = stock_data.iloc[i - 10:i]

        # Predict the return for the next two days
        predicted_return = predict_future_two_days_return(past_10_days)

        # Record the prediction result
        date_11th_day = stock_data.iloc[i]['date']
        results.append({'stock': stock, 'date': date_11th_day, 'predicted_return': predicted_return})

# Convert the results to a DataFrame
predictions_df = pd.DataFrame(results)

# Save the prediction results to an Excel file
predictions_df.to_excel('stock_predictions_august.xlsx', index=False)

# Simple trading strategy: Buy the stock with the highest predicted return
initial_capital = 10000

# Simulate each trading day
current_date = pd.to_datetime(backtest_start_date)

while current_date <= pd.to_datetime(end_date) - pd.Timedelta(days=1):
    # Get the prediction results for the current day
    trading_day_predictions = predictions_df[predictions_df['date'] == current_date.strftime('%Y-%m-%d')]

    # Select the stock with the highest predicted return
    if not trading_day_predictions.empty:
        best_stock_prediction = trading_day_predictions.loc[trading_day_predictions['predicted_return'].idxmax()]

        # Get the opening price for the selected stock
        best_stock_data = stock_data[(stock_data['stock'] == best_stock_prediction['stock']) &
                                     (stock_data['date'] == current_date.strftime('%Y-%m-%d'))]

        open_price = best_stock_data['open'].values[0]

        # Calculate the number of shares to buy
        shares_to_buy = initial_capital // open_price

        # Get the closing price for the next day
        next_day = current_date + pd.Timedelta(days=1)
        closing_price_next_day = stock_data[(stock_data['stock'] == best_stock_prediction['stock']) &
                                            (stock_data['date'] == next_day.strftime('%Y-%m-%d'))]['close'].values[0]

        # Calculate the profit
        profit = shares_to_buy * (closing_price_next_day - open_price)

        # Calculate the return on investment
        return_on_investment = (profit / initial_capital) * 100

        print(f"Trading Date: {current_date.strftime('%Y-%m-%d')}")
        print(f"Bought Stock: {best_stock_prediction['stock']}")
        print(f"Profit: ${profit:.2f}")
        print(f"Return on Investment: {return_on_investment:.2f}%")

    # Move to the next trading day
    current_date += pd.Timedelta(days=1)
