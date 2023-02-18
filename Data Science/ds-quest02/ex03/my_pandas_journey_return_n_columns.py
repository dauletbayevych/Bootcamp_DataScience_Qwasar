import pandas as pd
def my_pandas_journey_return_n_columns(param_1, param_2):
    df = pd.DataFrame(param_1)
    return df.iloc[:, :param_2]