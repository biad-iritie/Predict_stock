import pandas as pd
from datetime import datetime
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
# Read our data
df = pd.read_csv("sphist.csv")
# Convert the Date column into a Pandas date type
df["Date"] = pd.to_datetime(df["Date"])

df.sort_values(by="Date", ascending=True, inplace=True)

indicators = [5, 365]

for index, row in df.iterrows():
    size = len(df[df['Date'] < row['Date']])
    for indicator in indicators:
        column = "Day_{}".format(indicator)
        new_column = "Volume_Day_{}".format(indicator)
        # print(column)
        if size < indicator:
            df.loc[index, column] = 0
            df.loc[index, new_column] = 0
        else:
            df.loc[index, column] = np.mean(
                df.loc[index+indicator:index-1, "Close"])
            df.loc[index, new_column] = np.mean(
                df.loc[index+indicator:index-1, "Volume"])
df["ratio_5_365"] = df["Day_5"]-df["Day_365"]
# Ratio volume between 5 and 365 days
df["r_v_5_365"] = df["Volume_Day_5"]-df["Volume_Day_365"]

# using Pandas

# Remove data before 1951-01-03
df.drop(df[(df["Day_365"] == 0) | (df["Volume_Day_365"] == 0)].index,
        axis=0, inplace=True)
df.dropna(axis=0, inplace=True)
# print(df.head(10))
# Generate the train and test dataset
train = df[df["Date"] < datetime(year=2013, month=1, day=1)]
test = df[df["Date"] > datetime(year=2013, month=1, day=1)]

target = "Close"
features = ["Day_5", "Day_365", "ratio_5_365",
            "Volume_Day_5", "Volume_Day_365"]

lr = LinearRegression()
lr.fit(train[features], train[target])

predictions = lr.predict(test[features])
mae = mean_absolute_error(test['Close'], predictions)
print(mae)
# We'll pick the error metric : Mean Absolute Error

# print(df.head(20))
