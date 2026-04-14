import pandas as pd
import numpy as np

def data_preprocessing(path):
    data = pd.read_csv(path)

    # preprocess time column
    data['time'] = pd.to_datetime(data['time']).dt.strftime('%Y-%m-%d %H:%M:%S')
    data.sort_values(by='time', inplace=True)
    data.drop_duplicates(inplace=True)
    
    return data

def mean_abs_error(y_true, y_pred):
    n = len(y_true)
    if len(y_pred) != n:
        raise ValueError('y_true and y_pred have different number of outputs')
    abs_error = np.abs((y_true - y_pred) / y_true)
    
    return np.sum(abs_error) / n * 100