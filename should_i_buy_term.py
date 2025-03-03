import yfinance as yahooFinance
import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
import math
import sys
import plotext as plt
import random

if len(sys.argv) < 2:
    print("Usage: python3 should_i_pick.py <stock_ticker>")
    sys.exit(1)

stock_in = sys.argv[1]
data = yahooFinance.Ticker(stock_in)
views = [{
        "prd": "1mo",
        "ntvl": "1d",
        "title": "1 Month",
        "date": "%m-%d",
        "a": 1,
        "b": 1,
        "c": 1,
        "d": 1
    },{
        "prd": "3mo",
        "ntvl": "1d",
        "title": "3 months",
        "date": "%m-%d",
        "a": 1,
        "b": 1,
        "c": 2,
        "d": 1
    },{
        "prd": "1y",
        "ntvl": "1d",
        "title": "1 Year",
        "date": "%m-%d",
        "a": 1,
        "b": 2,
        "c": 1,
        "d": 1
    },{
        "prd": "5y",
        "ntvl": "1wk",
        "title": "5 Years",
        "date": "%y-%m",
        "a": 1,
        "b": 2,
        "c": 1,
        "d": 2
    }]

pd.set_option('display.max_rows', None)
# cols = 2
# rows = 2

# fig, axs = plt.subplots(rows, cols, figsize=(12, 4 * rows))
# axs = axs.flatten()

# for cnt, curr in enumerate(views):
#     historical_data = data.history(period=curr["prd"], interval=curr["ntvl"])
#     avg = (historical_data['High'] + historical_data['Low']) / 2 
#     axs[cnt].plot(historical_data.index, avg, label='High/Low avg.', color='green')
#     axs[cnt].set_title(f"{curr['title']}")
#     axs[cnt].set_xlabel('Date')
#     axs[cnt].set_ylabel('Price (USD)')
#     axs[cnt].grid()
#     axs[cnt].xaxis.set_major_formatter(mdates.DateFormatter(curr['date']))

# fig.suptitle(f"{data.info['shortName']}")
# plt.subplots_adjust(hspace=0.25, wspace=0.15)
# plt.tight_layout()
# plt.show()

plt.date_form('d/m/Y')
plt.clf()
plt.subplots(1, 2)
plt.subplot(1, 1).plotsize(plt.tw() // 2, None)
plt.subplot(1, 2).subplots(2, 1)
plt.subplot(1, 1).ticks_style('bold')

# for cnt, curr in enumerate(views):
#     historical_data = data.history(period=curr["prd"], interval=curr["ntvl"])
#     dates = plt.datetimes_to_strings(historical_data.index)
#     plt.subplot(curr["a"], curr["b"]).subplot(curr["c"], curr["d"])
#     plt.theme('windows')
#     # print(dates)
#     # print(historical_data["High"])
#     # print(historical_data["Low"])
#     # print(historical_data["Open"])
#     # print(historical_data["Close"])
#     plt.candlestick(dates, historical_data)
#     plt.title(curr["title"])




plt.date_form('d/m/Y')
# start = plt.string_to_datetime("11/07/2020")
# end = plt.today_datetime()
# p = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
# mp = [14, 36, 11, 8, 7, 4]
# fp = [12, 20, 35, 15, 2, 1]
# hd = [random.gauss(1, 1) for el in range(3 * 10 ** 5)]

plt.clf()
# plt.subplots(1, 2)

# plt.subplot(1, 2).subplots(2, 1)
plt.subplot(1, 1).ticks_style('bold')

plt.subplot(1, 1).subplot(1, 1)
plt.theme('windows')
historical_data = data.history(period=views[0]["prd"], interval=views[0]["ntvl"])
dates = plt.datetimes_to_strings(historical_data.index)
plt.candlestick(dates, historical_data)
plt.title(views[0]["title"])

# plt.subplot(1, 1).subplot(2, 1)
# plt.theme('dreamland')
# plt.stacked_bar(p, [mp, fp], labels = ["men", "women"])
# plt.title("Most Favored Pizzas in the World by Gender")

# plt.subplot(1, 1).subplot(3, 1)
# plt.theme('matrix')
# bins = 18
# plt.hist(hd, bins, label = "Gaussian Noise Distribution", marker = 'fhd')
# plt.yfrequency(0)
# plt.title('Histogram Plot')

# plt.subplot(1, 2).subplot(1, 1).title('Default Theme')
# plt.plot(plt.sin(periods = 3), marker = "fhd", label = "3 periods")
# plt.plot(plt.sin(periods = 2), marker = "fhd", label = "2 periods")
# plt.plot(plt.sin(periods = 1), marker = "fhd", label = "1 period")

# plt.subplot(1, 2).subplot(2, 1)
# plt.plotsize(2 * plt.tw() // 3, plt.th() // 2)
# plt.image_plot(path)
# plt.title("A very Cute Cat")

plt.show()
plt.delete_file(path)