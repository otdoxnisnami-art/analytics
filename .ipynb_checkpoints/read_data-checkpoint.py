import sys
import os
repo_dir = os.path.expanduser('~/analytics')

sys.path.append(repo_dir)

from data_maining import get_dataframe_shape

file_path = '/Users/sulejmannahmedov/Desktop/JupiterNotebook/Курсы Карпова ч.1/2_taxi_nyc.csv'
data_shape = get_dataframe_shape(file_path)

print(data_shape)