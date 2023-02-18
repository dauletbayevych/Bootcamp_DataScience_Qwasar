import numpy as np 
import pandas as pd 
from sklearn.metrics import mean_absolute_error 
 
def my_model_evaluation_journey_mean_absolute_error(asl, lsa): 
    df1 = pd.read_csv(asl) 
    df2 = pd.read_csv(lsa) 
 
    y1 = df1.select_dtypes(include = np.number) 
    y2 = df2.select_dtypes(include = np.number) 
     
    y2new = y2[0:len(y1)] 
 
    return mean_absolute_error(y1, y2new)