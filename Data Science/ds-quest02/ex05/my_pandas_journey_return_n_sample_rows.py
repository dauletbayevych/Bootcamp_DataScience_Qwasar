import pandas as cr7

def my_pandas_journey_return_n_sample_rows(param_1, param_2):
    utd = cr7.DataFrame(param_1)
    return utd.sample(n = param_2)