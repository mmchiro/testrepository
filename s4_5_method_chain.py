import pandas as pd
sales_data = pd.read_csv("sales_data.csv",parse_dates=True,index_col='InvoiceDate')

#Find the maximum of weekly sales data
#weekly_max = sales_data.resample('W').sum().max()
#print(weekly_max)
#weekly_mean = sales_data.resample('W').mean()
#print(weekly_mean)
#biweekly_mean = sales_data.resample('2W').mean()
#print(biweekly_mean)
weekly_mean = sales_data.loc[:,'Quantity'].resample('W').sum()
print(weekly_mean)
