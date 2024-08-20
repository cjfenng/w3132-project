# from StrategyPlatform import strategy_one
import json
import tushare as ts
from StrategyPlatform import strategy_one

tushare_token = "8c905da620328be3d7c2f84fe2ce72657d35a144e7a7ebe45fa9c0c1"

def strategy_one_in(stock_pool, current_date, current_position):
    # TODO... Call logic
    return [], []

def get_trade_dates(start_date, end_date):
    # Initialize the pro API
    pro = ts.pro_api(tushare_token)
    # Fetch data
    df = pro.trade_cal(
        **{
            "exchange": "SSE",
            "cal_date": "",
            "start_date": start_date,
            "end_date": end_date,
            "is_open": "",
            "limit": "",
            "offset": ""
        },
        fields=[
            "cal_date",
            "is_open",
        ]
    )
    df['is_open'] = df['is_open'].astype(str)
    df.rename(columns={'cal_date': 'date', 'is_open': 'is_trade_date'}, inplace=True)
    df = df[df['is_trade_date'] == '1']
    return list(df['date'])

def run(stock_pool, start_date, end_date):
    # Historical positions for each day
    history_positions = {
        # Current position map for a specific date
        "date": {}
    }
    # Position information
    current_position_map = {
        "code": {
            "code": "code",
            "shares": 0,
            "buy_in_price": 0,
            "weight": 0
        }
    }

    current_money = 10000
    total_profit_percent = 0
    total_profit = 0

    # Get trade dates within the range from tushare
    trade_dates = get_trade_dates(start_date, end_date)

    for current_date in trade_dates:
        # Return the buy list and the sell list
        buy_order_list, sell_order_list = strategy_one.run(stock_pool, current_date, current_position_map)

        # Increase position if buy_order_list is encountered, recalculate the new price
        # Buy first, then sell
        if buy_order_list:
            for order in buy_order_list:
                code = order['code']
                shares = order['shares']
                price = order['price']

                current_position = {
                    "code": code,
                    "shares": shares,
                    "price": price  # Need to fetch data again, not from the strategy, but from the database
                }
                # If there is an existing position, accumulate and recalculate the price
                if order['code'] in current_position_map:
                    exist_position = current_position_map[code]
                    exist_price = exist_position['price']
                    exist_shares = exist_position['shares']

                    # Calculate the new price
                    price_new = (price * shares + exist_price * exist_shares) / (shares + exist_shares)

                    # Assign the new price
                    current_position['price'] = price_new
                    # Assign the new share count
                    current_position['shares'] = shares + exist_shares

                # Cache the updated position
                current_position_map[code] = current_position

        if sell_order_list:
            for order in sell_order_list:
                code = order['code']
                shares = order['shares']
                price = order['price']  # Need to fetch data again, not from the strategy, but from the database

                current_position = {
                    "code": code,
                    "shares": shares,
                    "price": price
                }
                # If there is an existing position, accumulate and recalculate the price
                if order['code'] in current_position_map:
                    exist_position = current_position_map[code]
                    exist_price = exist_position['price']
                    exist_shares = exist_position['shares']

                    # Calculate the new price TODO... Need to check if this is correct
                    price_new = (exist_price * exist_shares - price * shares) / (exist_shares - shares)

                    # Assign the new price
                    current_position['price'] = price_new
                    # Assign the new share count
                    current_position['shares'] = exist_shares - shares

                # Cache the updated position
                current_position_map[code] = current_position

                # TODO... Need to calculate profit and loss

        # After one loop, cache the history to avoid references (use serialization/deserialization)
        history_positions[current_date] = json.loads(json.dumps(current_position_map))

#         buy_order_list.get stock code = code
#         BUY_order_list.get shares = weight
#
#         df = tushare.get (code, date)
#
#         # Add position information
#
#         current_position.stock = code
#         current_position.buy_in_price = df['open']
#         current_position.shares = current_money * weight / df['open']
#
#
#         sell_order_list.get stock = code
#         df = tushare.getstock(code, date)
#         delete current_postion.stock = code
#
#
#         sell_price = df['close']
#
#         total_profit = total_profit + (shares * sell_price - shares * buy_in_price)
#         total_profit_percentage = total_profit / initial_money
#
# # Purchase record list.get_sell_date

if __name__ == '__main__':
    stock_pool = {"600011.SH", "600012.SH"}
    start_date = "20240701"
    end_date = "20240731"
    run(stock_pool, start_date, end_date)
