import pandas as pd
df = pd.read_csv("intel.csv")

#Print data to show that it work
#print(df)

#Print to check data type
#print(type(df))

#Help to check dataframe shape
#print(df.shape)

#Print column name
#print(df.columns)

#Print first 5 rows of the data
#print(df.head())

#Inspect bottom 5 rows of the data
#print(df.tail())

#Inspect last 2 rows of data
#print(df.tail(2))

#View summary of dataframe info
#print(df.info())

#Juest print Open column
#open = df['Open']
#print(open)
#print(open.head())

#Print the first 5 rows of Open and Close column
#print (df[['Open','Close']].head())

#Using the describe method - mean, std, min, max etc
#print(df.describe())
