import pandas as pd
def my_pandas_journey_return_n_rows(param_1, param_2):
    df = pd.DataFrame(param_1)
    return df.head(param_2)