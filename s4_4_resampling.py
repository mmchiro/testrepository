import pandas as pd

sales_data = pd.read_csv("resampling_sales_data.csv", parse_dates = True, index_col='InvoiceDate')
#print(sales_data.info())
#print(sales_data.head())
#Downsampling - from days to week

weekly_mean = sales_data.resample('w').sum()
print(weekly_mean)
#monthly_mean = sales_data.resample('M').mean()
#print(monthly_mean)
#
