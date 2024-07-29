import pandas as pd
import numpy as np

# Load your stock data for the given period
# This should be a DataFrame with columns: 'date', 'stock', 'open', 'close', etc.

# Define your stock pool
stock_pool = ['AAPL', 'MSFT', 'GOOGL']  # Example stock tickers

# Define the trading period
start_date = '2023-01-01'
end_date = '2023-12-31'


# Function to predict the next day's closing price using the past 10 days of data
def predict_next_day_close(past_10_days):
    # Implement your prediction model here
    # This is a placeholder for the actual model
    predicted_close = past_10_days['close'].mean()
    return predicted_close


# Prepare a DataFrame to store results
results = []

# Iterate over each stock in the pool
for stock in stock_pool:
    # Filter data for this stock and trading period
    stock_data = data[(data['stock'] == stock) & (data['date'] >= start_date) & (data['date'] <= end_date)]

    # Iterate through the stock data to make predictions
    for i in range(len(stock_data) - 10):
        # Get the past 10 days of data
        past_10_days = stock_data.iloc[i:i + 10]

        # Predict the 11th day's closing price
        predicted_close = predict_next_day_close(past_10_days)

        # Record the prediction
        date_11th_day = stock_data.iloc[i + 10]['date']
        results.append({'stock': stock, 'date': date_11th_day, 'predicted_close': predicted_close})

# Convert results to a DataFrame
predictions_df = pd.DataFrame(results)

# Save the predictions to an Excel file
predictions_df.to_excel('stock_predictions.xlsx', index=False)

# Simple trading strategy: Buy the stock with the highest predicted close
initial_capital = 10000

# Get the predictions for the 11th day
trading_day_predictions = predictions_df[predictions_df['date'] == '2023-01-11']

# Select the stock with the highest predicted closing price
best_stock_prediction = trading_day_predictions.loc[trading_day_predictions['predicted_close'].idxmax()]

# Get the open price for this stock on the trading day
best_stock_data = stock_data[(stock_data['stock'] == best_stock_prediction['stock']) &
                             (stock_data['date'] == '2023-01-11')]

open_price = best_stock_data['open'].values[0]

# Calculate the number of shares to buy
shares_to_buy = initial_capital // open_price

# Get the closing price on the next day
closing_price_next_day = stock_data[(stock_data['stock'] == best_stock_prediction['stock']) &
                                    (stock_data['date'] == '2023-01-12')]['close'].values[0]

# Calculate the profit
profit = shares_to_buy * (closing_price_next_day - open_price)

# Calculate the return
return_on_investment = (profit / initial_capital) * 100

print(f"Profit: ${profit:.2f}")
print(f"Return on Investment: {return_on_investment:.2f}%")


