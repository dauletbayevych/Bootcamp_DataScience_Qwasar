import pandas as utd

def my_pandas_journey_drop_columns(param_1, param_2):
    pd = utd.DataFrame(param_1)
    return pd.drop(param_2, axis=1)