import pandas as pd

def get_dataframe_shape(file_path):
    df = pd.read_csv(file_path, encoding='utf-8')
    return df.shape

def get_dataframe_dtypes(file_path):
    df =  pd.read_csv(file_path)
    return df.dtypes

def get_dataframe_columns(file_path):
    df = pd.read_csv(file_path)
    return df.columns