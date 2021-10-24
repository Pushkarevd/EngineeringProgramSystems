import pandas as pd
from statsmodels.tsa.arima_model import ARIMA


def predict(data: dict, obj_name: str) -> pd.DataFrame:
    values = [value[obj_name] for value in data]
    timestamps = [value['created_on'] for value in data]
    series = pd.Series(
        values,
        index=timestamps
    )

    model = ARIMA(series, order=(5, 1, 0))
    model_fit = model.fit()
    predictions = model_fit.forecast(steps=5)[0]
    return [value for value in predictions]
