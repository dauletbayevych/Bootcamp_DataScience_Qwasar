import pandas as cr7

def my_pandas_journey_filtering(param_1):
    pd = cr7.DataFrame(param_1)
    return pd[pd.Index == 'A']