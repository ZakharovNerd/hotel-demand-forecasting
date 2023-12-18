import pandas as pd
from etna.datasets import TSDataset
from utils.weather_utils import weather_encoding

def get_regressor_df():
    regressor_df = pd.read_csv("data/nordics_weather.csv")

    regressor_df['timestamp'] = pd.to_datetime(regressor_df['date'])
    regressor_df.drop(columns=["date"], inplace=True)

    regressor_df['country'] = regressor_df.apply(weather_encoding, axis=1)

    regressor_df['segment'] = regressor_df['country'] # Convert order_date to datetime
    regressor_df.drop(columns=["country"], inplace=True)

    return TSDataset.to_dataset(regressor_df)