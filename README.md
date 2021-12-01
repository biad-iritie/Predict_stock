# Predicting Stock Market

In this project, you'll work with data from the S&P500 Index. [The S&P500](https://en.wikipedia.org/wiki/S%26P_500) is a stock market index. Before we get into what an index is, we'll need to start with the basics of the stock market.

Some companies are publicly traded, which means that anyone can **buy and sell their shares** on the open market. A share entitles the owner to some control over the direction of the company and to a percentage (or share) of the earnings of the company. When you buy or sell shares, it's common known as **trading a stock**. The price of a share is based on supply and demand for a given stock.

**Indexes** aggregate the prices of multiple stocks together, and allow you to see how the market as a whole performs.

You'll be using historical data on the price of the S&P500 Index to make predictions about future prices. Predicting whether an index goes up or down helps forecast how the stock market as a whole performs. Since stocks tend to correlate with how well the economy as a whole is performs, it can also help with economic forecasts.

In this project, our dataset contain index prices. Each row in the file contains a daily record of the price of the S&P500 Index from *1950* to *2015*. The dataset is stored in sphist.csv.

| Columns | Description |
| ----------- | ----------- |
| **Date** | The date of the record. |
| Open | The opening price of the day (when trading starts) |
| High |  The highest trade price during the day |
| Low | The lowest trade price during the day |
| Close | The closing price for the day (when trading is finished) |
| Volume | The number of shares traded |
| Adj Close | The daily closing price, adjusted retroactively to include any corporate actions. |

You'll be using this dataset to develop a predictive model. You'll train the model with data from *1950-2012* and try to make predictions from *2013-2015*.
