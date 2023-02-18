import numpy as np 

import pandas as pd 

from sklearn.metrics import r2_score 
 
 
def my_model_evaluation_journey_r2_score(param_1, param_2): 
 
    df1 = pd.read_csv(param_1) 
    df2 = pd.read_csv(param_2) 
 
    y1 = df1.select_dtypes(include = np.number) 
    y2 = df2.select_dtypes(include = np.number) 
 
    y2new = y2[0:len(y1)] 
 
    return r2_score(y1, y2new)