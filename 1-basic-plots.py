import matplotlib as plt
import pandas as pd

input_file_path = "/Users/mac/python/jack-dies/data/train.csv"

df = pd.read_csv(input_file_path)
print "\n loading CSV file Train.csv"
df.head(10)
df.dtypes
