import pandas as pd
import numpy as np
import scipy.stats as stats

chat_id = 897113152 # Ваш chat ID, не меняйте название переменной

def solution(x, y) -> bool:
    return stats.ttest_ind(x, y)[1] < 0.07
