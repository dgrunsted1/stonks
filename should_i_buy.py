import yfinance as yahooFinance
import pandas as pd
import matplotlib.pyplot as plt
import math
import sys

if len(sys.argv) < 2:
    print("Usage: python3 should_i_pick.py <stock_ticker>")
    sys.exit(1)

stock_in = sys.argv[1]
data = yahooFinance.Ticker(stock_in)
views = [{
    "prd": "1y",
    "ntvl": "1wk",
    "title": "1 Year"
},{
    "prd": "3mo",
    "ntvl": "1d",
    "title": "3 months"
},{
    "prd": "1mo",
    "ntvl": "1d",
    "title": "1 Month"
},{
    "prd": "5y",
    "ntvl": "1mo",
    "title": "5 Years"
}]

pd.set_option('display.max_rows', None)
cols = 2
rows = 2

fig, axs = plt.subplots(rows, cols, figsize=(12, 4 * rows))
axs = axs.flatten()

for cnt, curr in enumerate(views):
    historical_data = data.history(period=curr["prd"], interval=curr["ntvl"])
    avg = (historical_data['High'] + historical_data['Low']) / 2 
    axs[cnt].plot(historical_data.index, avg, label='High/Low avg.', color='green')
    axs[cnt].set_title(f"{curr['title']}")
    axs[cnt].set_xlabel('Date')
    axs[cnt].set_ylabel('Price (USD)')
    axs[cnt].grid()

fig.suptitle(f"{data.info['shortName']}")
plt.subplots_adjust(hspace=0.25, wspace=0.15)
plt.tight_layout()
plt.show()