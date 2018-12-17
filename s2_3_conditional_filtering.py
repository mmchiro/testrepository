import pandas as pd

df = pd.read_csv("intel.csv")
#my_open = df['Open']>40
#Only return true
#print(my_open)

#Print the values that are more than 40
#print(df[my_open])

#Shows values greater than 55. No need to create an additional variable
#print(df[df['Open']>55.0])
