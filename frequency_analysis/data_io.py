import pandas as pd

def read_yearly_maxima(path: str, date_format: str) -> pd.Series:
    data = pd.read_csv(path)
    dates = pd.to_datetime(data.iloc[:, 0], format=date_format)
    data = data.drop(data.columns[0], axis=1)
    data = data.set_index(dates)
    data = data.resample("YE").max()
    data = data.set_index(data.index.year)
    return data.iloc[:, 0]
