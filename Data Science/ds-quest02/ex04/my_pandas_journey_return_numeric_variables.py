import pandas as cr7

def my_pandas_journey_return_numeric_variables(param_1):
    real = cr7.DataFrame(param_1)
    return real.select_dtypes(['float64', 'float32', 'int64', 'int32'])