import tushare as ts
from sklearn.preprocessing import MinMaxScaler

def get_train_data():
    codes = "300624.SZ"
    start_date = "20220401"
    end_date = "20240619"
    train_window_size = 30
    target_window_size = 2
    train_dimension = ["close", "open", "ma_5"]
    target_dimension = ["pct_chg"]
    train_data = []
    train_mark_data = []

    target_data = []
    target_mark_data = []


    pro = ts.pro_api()
    df = pro.daily(ts_code=codes, start_date=start_date, end_date=end_date)


    df = df.iloc[::-1]

    df['vol_pct_change'] = df['vol'].pct_change().fillna(0)

    df['ts_code'] = df['ts_code'].str.replace(r'\.SZ|\.SH', '', regex=True)

    print(len(df))

    for start_idx in range(len(df) - train_window_size):
        end_idx = start_idx + train_window_size

        train_window_data = df[start_idx:end_idx]
        target_window_data = df[end_idx:end_idx + 1]
        current_train_data = train_window_data[['pct_chg', 'vol_pct_change']].values.tolist()
        current_train_mark_data = train_window_data[['ts_code', 'trade_date']].astype(float).values.tolist()

        current_target_data = target_window_data[['pct_chg', 'vol_pct_change']].values.tolist()
        current_target_mark_data = train_window_data[['ts_code', 'trade_date']].astype(float).values.tolist()

        train_data.append(current_train_data)
        train_mark_data.append(current_train_mark_data)

        target_data.append(current_target_data)
        target_mark_data.append(current_target_mark_data)
    return train_data, train_mark_data, target_data, target_mark_data


def get_multiple_stock_data():
    codes = ["300624.SZ", "300625.SZ" ]
    start_date = "20160401"
    end_date = "20240619"
    train_window_size = 10
    train_data = []
    target_data = []

    for code in codes:
        pro = ts.pro_api()
        df = pro.daily(ts_code=code, start_date=start_date, end_date=end_date)
        df = df.iloc[::-1]

        scaler = MinMaxScaler()
        df[['open', 'high', 'low', 'close', 'vol']] = scaler.fit_transform(df[['open', 'high', 'low', 'close', 'vol']])
        print(df)

        for start_idx in range(len(df) - train_window_size):
            end_idx = start_idx + train_window_size

            train_window_data = df[start_idx:end_idx]
            target_window_data = df[end_idx:end_idx + 1]
            current_train_data = train_window_data[['open', 'high', 'low', 'close', 'vol']].values.tolist()
            current_target_data = target_window_data[['close']].values.tolist()

            train_data.append(current_train_data)
            target_data.append(current_target_data)

    return train_data, target_data

def get_test_stock_data():
    code = "300625.SZ"
    start_date = "20240401"
    end_date = "20240619"
    test_window_size = 10
    test_data = []
    actual_data = []

    pro = ts.pro_api()
    df = pro.daily(ts_code=code, start_date=start_date, end_date=end_date)
    df = df.iloc[::-1]

    scaler = MinMaxScaler()
    df[['open', 'high', 'low', 'close', 'vol']] = scaler.fit_transform(df[['open', 'high', 'low', 'close', 'vol']])
    for start_idx in range(len(df) - test_window_size):
        end_idx = start_idx + test_window_size

        train_window_data = df[start_idx:end_idx]
        target_window_data = df[end_idx:end_idx + 1]
        current_test_data = train_window_data[['open', 'high', 'low', 'close', 'vol']].values.tolist()
        current_actual_data = target_window_data[['close']].values.tolist()

        test_data.append(current_test_data)
        actual_data.append(current_actual_data)

    return test_data, actual_data


def get_past_data(stock_code, predict_date, days=10):
    """
    Retrieve stock data for the past specified number of days.
    """
    pro = ts.pro_api()

    # Get the most recent trading days
    trade_cal = pro.trade_cal(exchange='', start_date='20100101', end_date=predict_date)
    trade_cal = trade_cal[trade_cal['is_open'] == 1]  # Filter out trading days
    trade_cal = trade_cal.sort_values(by='cal_date', ascending=False)  # Sort by date in descending order

    # Get the days+1 trading days before the predict_date, including predict_date
    past_dates = trade_cal[trade_cal['cal_date'] <= predict_date].iloc[:days+1]
    start_date = past_dates.iloc[-1]['cal_date']  # Get start_date
    end_date = past_dates.iloc[0]['cal_date']  # Get end_date

    # Retrieve stock data from Tushare
    df = pro.daily(ts_code=stock_code, start_date=start_date, end_date=end_date)
    df.sort_values('trade_date', inplace=True)  # Sort by trading date

    return df