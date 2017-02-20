import glob
import ntpath
import os
import pandas as pd


def get_paths(path):
    return glob.glob(os.path.join(os.getcwd(), '{}/*.csv'.format(path)))


def csv_to_df(stock):
    symbol = (ntpath.basename(stock)).split('.')[0]
    df = pd.read_csv(stock,
                     index_col='Date',
                     parse_dates=True,
                     usecols=['Date', 'Adj Close'],
                     na_values=['nan'])
    df = df.rename(columns={'Adj Close': symbol})
    return df


def get_prices(stock_paths, dates):
    df = pd.DataFrame(index=dates)

    for stock in stock_paths:
        df_temp = csv_to_df(stock)
        df = df.join(df_temp)

    most_traded = (df.isnull().sum()).idxmin()
    df = df.dropna(subset=[most_traded])

    return df


def fill_incomplete(df):
    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)


def normalize_price(df):
    return df / df.ix[0, :]
