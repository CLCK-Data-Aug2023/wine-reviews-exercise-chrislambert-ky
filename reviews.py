# add your code here

#Complete code - works as intended.
import zipfile
import pandas as pd

with zipfile.ZipFile("data/winemag-data-130k-v2.csv.zip", "r") as zip_ref:
    zip_ref.extractall("data/")

df = pd.read_csv("data/winemag-data-130k-v2.csv")
temp_df = df.groupby('country').agg({'title': 'count', 'points': 'mean'})
temp_df['points'] = temp_df['points'].round(1)
temp_df.to_csv("data/reviews-per-country.csv")