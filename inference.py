from etna.core import load
from etna.analysis import plot_forecast

from data_processing.target_weather_data_processing import get_grouped_data

HORIZON = 30

def forecast_ts():
    ts = get_grouped_data()
    new_ts, test_ts = ts.train_test_split(test_size=HORIZON)

    pipeline_loaded = load("inference_data/pipeline.zip", ts=new_ts)

    transform_0_loaded = load("inference_data/transform_0.zip")

    forecast_ts = pipeline_loaded.forecast()

    return forecast_ts
