import requests
import pandas as pd

def get_stock_ticker_df(ticker):
    response = requests.get('https://www.quandl.com/api/v3/datasets/WIKI/%s.json?api_key=Xasu25Hmku9A-cxcryrY' % ticker)
    parsed = response.json()

    if 'dataset' in parsed:
        column_names = parsed["dataset"]["column_names"]
        data = parsed["dataset"]["data"]

        df = pd.DataFrame(data, columns=column_names)
        return df

    else:
        print('invalid tick, try again!')

        return None

def get_high(ticker):
    df = get_stock_ticker_df(ticker)
    return df['High'].max()

def get_low(ticker):
    df = get_stock_ticker_df(ticker)
    return df['High'].min()

def get_close_price_data_1_mo(ticker):
    df = get_stock_ticker_df(ticker)
    return list(df['Close'].head(30))

def get_open_price_data_1_mo(ticker):
    df = get_stock_ticker_df(ticker)
    return list(df['Open'].head(30))

def get_adj_close_price_data_1_mo(ticker):
    df = get_stock_ticker_df(ticker)
    return list(df['adj_close'].head(30))

def get_adj_open_price_data_1_mo(ticker):
    df = get_stock_ticker_df(ticker)
    return list(df['adj_open'].head(30))