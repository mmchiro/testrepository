import pandas as pd
sales_data=pd.read_csv("sales_data.csv",parse_dates=True,index_col='InvoiceDate')

#To look on specific the quantity on 1st Dec 2010
morning_sales=sales_data['Quantity']['2010-12-01']

#To examine the max sold during the hours on 1st Dec 2010
high_quantity = morning_sales.resample('H').max()
print(high_quantity)
