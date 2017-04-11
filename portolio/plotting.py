import os
import pandas as pd


def dic_to_df(stock):
    symbol = stock[0]['Symbol']
    df = pd.DataFrame(stock, columns=['Adj_Close', 'Date'])
    df.set_index('Date', inplace=True)
    df = df.rename(columns={'Adj_Close': symbol})
    df.index = pd.to_datetime(df.index)
    return df


def get_prices(stock_paths, dates):
    df = pd.DataFrame(index=dates)

    for stock in stock_paths:
        df_temp = dic_to_df(stock)
        df = df.join(df_temp)

    most_traded = (df.isnull().sum()).idxmin()
    df = df.dropna(subset=[most_traded])
    df = df.apply(lambda x: pd.to_numeric(x, errors='ignore'))

    return df


def fill_incomplete(df):
    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)


def normalize_price(df):
    return df / df.ix[0, :]
