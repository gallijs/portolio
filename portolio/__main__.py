import argparse
import matplotlib.pyplot as plt
import pandas as pd
from yahoo_finance import Share

from . import plotting
from .__version__ import __version__


def construct_parser():
    parser = argparse.ArgumentParser(
        description='Portolio is a portfolio optimizer.')
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='%(prog)s {version}'.format(version=__version__))
    parser.add_argument('sd', help='start date', metavar='start_date')
    parser.add_argument('ed', help='end date', metavar='end_date')
    parser.add_argument('symbols',
                        nargs='+',
                        help='stock symbols in the portfolio',
                        metavar='symbol')
    parser.add_argument('-n',
                        '--normalize',
                        help='normalize stock prices',
                        action='store_true')
    return parser


def cli():
    parser = construct_parser()
    args = vars(parser.parse_args())

    stock_data = [Share(symbol).get_historical(args['sd'], args['ed'])
                  for symbol in args['symbols']]

    dates = pd.date_range(args['sd'], args['ed'])

    stock_prices = plotting.get_prices(stock_data, dates)
    plotting.fill_incomplete(stock_prices)

    if args['normalize']:
        stock_prices = plotting.normalize_price(stock_prices)

    stock_prices.plot()
    plt.show()


if __name__ == '__main__':
    cli()
