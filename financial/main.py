from yahoofinancials import *
from matplotlib.pyplot import *
import matplotlib.pyplot as plt

from matplotlib.dates import DateFormatter, WeekdayLocator,\
    DayLocator, MONDAY


# (Year, month, day) tuples suffice as args for quotes_historical_yahoo
date1 = (2004, 2, 1)
date2 = (2004, 4, 12)


mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
alldays = DayLocator()              # minor ticks on the days
weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
dayFormatter = DateFormatter('%d')      # e.g., 12

quotes = quotes_historical_yahoo_ohlc('INTC', date1, date2)
if len(quotes) == 0:
    raise SystemExit

fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)
#ax.xaxis.set_minor_formatter(dayFormatter)

#plot_day_summary(ax, quotes, ticksize=3)
candlestick_ohlc(ax, quotes, width=0.6)

ax.xaxis_date()
ax.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

plt.show()
"""
{
    "WFC": {
        "prices": [
            {
                "volume": 260271600,
                "formatted_date": "2017-09-30",
                "high": 55.77000045776367,
                "adjclose": 54.91999816894531,
                "low": 52.84000015258789,
                "date": 1506830400,
                "close": 54.91999816894531,
                "open": 55.15999984741211
            }
        ],
        "eventsData": [],
        "firstTradeDate": {
            "date": 76233600,
            "formatted_date": "1972-06-01"
        },
        "isPending": false,
        "timeZone": {
            "gmtOffset": -14400
        },
        "id": "1mo15050196001507611600"
    }
}
"""

yahoo_financials = YahooFinancials('WFC')
# print(yahoo_financials.get_historical_price_data("2019-01-15", "2019-01-15", "daily"))
print(yahoo_financials.get_stock_price_data(reformat=True))