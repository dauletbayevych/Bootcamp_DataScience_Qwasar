import numpy as np 
import pandas as pd 

from sklearn.metrics import f1_score 
 
def my_model_evaluation_journey_f_one(asl, lsa): 
 
    return f1_score(asl, lsa, average=None)