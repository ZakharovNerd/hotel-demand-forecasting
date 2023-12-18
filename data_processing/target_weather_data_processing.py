import pandas as pd
from etna.datasets import TSDataset

from utils.db_connect import connect_to_postgres
from weather_data_processing import get_regressor_df
from utils.target_utils import target_encoding

def get_grouped_data():
    df = connect_to_postgres()

    df['hotel_id'] = df.apply(target_encoding, axis=1)

    # Convert 'order_date' to datetime and ensure it's the index alongside 'hotel_id'
    df['order_date'] = pd.to_datetime(df['order_date'])

    df['order_date'] = df['order_date'] - pd.Timedelta(days=2*365 + 180)

    grouped = df.groupby(['order_date', 'hotel_id']).size().reset_index(name='target')

    grouped['segment'] = grouped['hotel_id'] # Convert order_date to datetime
    grouped.drop(columns=["hotel_id"], inplace=True)

    grouped['timestamp'] = pd.to_datetime(grouped['order_date'])
    grouped.drop(columns=["order_date"], inplace=True)

    # Convert the grouped DataFrame to a TSDataset
    ts_dataset = TSDataset.to_dataset(grouped)

    # Create a date range from the min to max of your existing dates
    date_range = pd.date_range(start=grouped['timestamp'].min(), end=grouped['timestamp'].max())

    # Get a list of unique segments
    segments = grouped['segment'].unique()

    # Create a MultiIndex with all combinations of date and segment
    full_index = pd.MultiIndex.from_product([date_range, segments], names=['timestamp', 'segment'])

    # Reindex your DataFrame
    grouped = grouped.set_index(['timestamp', 'segment']).reindex(full_index, fill_value=0).reset_index()

    # The 'target' column now has NaN where data was missing, fill these with 0
    grouped['target'] = grouped['target'].fillna(0)

    HORIZON = 30

    ts_dataset = TSDataset.to_dataset(grouped)

    regressor_df = get_regressor_df()

    return TSDataset(df=ts_dataset, freq="D", df_exog=regressor_df, known_future="all")

