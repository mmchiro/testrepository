import pandas as pd

df = pd.read_csv("intel.csv")
open = df['Open']

#print(open)
#Shows that it is a series. When column extract from dataframe, it is a series.
#print(type(open))

new_open = open.values
print(new_open)

#Show that it is a numpy array
print(type(new_open))
#A panda series is actually a one dimensional 
