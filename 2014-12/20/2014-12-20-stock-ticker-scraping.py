#!/usr/bin/env python
#
# Load and display some stock market data
#

import urllib2
import csv
import matplotlib.pyplot as plt
import datetime


class BadDataError(Exception):
    pass


def make_ticker_url(symbol):
    base_url = "http://ichart.finance.yahoo.com/table.csv?s="
    ticker_url = base_url + symbol.upper()
    return ticker_url


def get_csv_for_stock(symbol):
    response = urllib2.urlopen(make_ticker_url(symbol))
    response_reader = csv.DictReader(response)
    return response_reader

stocks_to_get = [
    'AAPL',
    'MSFT'
]

stock_readers = [get_csv_for_stock(symbol) for symbol in stocks_to_get]
# stock_data = [list(reader) for reader in stock_readers]

dates = []
prices = []
# zip(*stock_readers) creates a series containing one row of data
# for each date -- thus I can pair up corresponding dates for the
# stocks
try:
    for date_info in zip(*stock_readers):
        # Here, date info is a tuple containing info about each stock,
        # grouped up by date, e.g. (AAPL, MSFT, etc)
        date = date_info[0]['Date']
        date_parts = date.split('-')
        dates.append(datetime.datetime(int(date_parts[0]), int(date_parts[1]),
                                       int(date_parts[2])))
        for stock in date_info:
            if stock['Date'] != date:
                raise BadDataError("Incomplete or badly ordered data!")
        prices.append([s['Close'] for s in date_info])
except BadDataError:
#     print "Oh dear!"
    pass

series1 = [x[0] for x in prices]
series2 = [x[1] for x in prices]

plt.plot(dates, series1)
plt.plot(dates, series2)

plt.show()
