import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

# Connect to Google Trends
Trending_topics = TrendReq(hl='en-US', tz=360)

# Define the keyword and build the payload
kw_list = ["Cloud Computing"]
Trending_topics.build_payload(kw_list, cat=0, timeframe='today 12-m')

# Interest Over Time
data_time = Trending_topics.interest_over_time()
data_time = data_time.sort_values(by="Cloud Computing", ascending=False)
data_time = data_time.head(10)
print("Interest Over Time:\n", data_time)

# Interest By Region
data_region = Trending_topics.interest_by_region()
data_region = data_region.sort_values(by="Cloud Computing", ascending=False)
data_region = data_region.head(10)
print("\nInterest By Region:\n", data_region)

# Visualize Interest By Region
data_region.reset_index().plot(x='geoName', y='Cloud Computing',
                               figsize=(10, 5), kind="bar")
plt.style.use('fivethirtyeight')
plt.show()

# Top Charts for 2023
df_top_charts = Trending_topics.top_charts(2023, hl='en-US', tz=300, geo='GLOBAL')
print("\nTop Charts of 2023:\n", df_top_charts.head(10))
