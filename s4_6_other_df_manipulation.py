import pandas as pd
sales_data=pd.read_csv("sales_data.csv",parse_dates=True,index_col='InvoiceDate')
#print(sales_data.head())

search = sales_data['Description'].str.contains('POPPY')

total_poppy_sales = search.resample('H').sum()

print(total_poppy_sales)
