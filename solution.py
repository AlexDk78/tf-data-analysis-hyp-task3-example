import pandas as pd
import numpy as np


chat_id = 897113152 # Ваш chat ID, не меняйте название переменной

def solution(X, Y) -> bool:
    from scipy.stats import ttest_ind
    alpha = 0.07
    n1, n2 = len(X), len(Y)

    t_stat, p_value = ttest_ind(X, Y, equal_var=True)
    
    if p_value/2 < alpha and t_stat > 0:
        return True
    else:
        return False
