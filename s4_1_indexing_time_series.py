import pandas as pd
sales_data=pd.read_csv("sales_data.csv",parse_dates=True,index_col='InvoiceDate')
#Print sales data to ensure it is working

#print(sales_data.tail())
#print(sales_data.info())
#Use the .loc accessor to access sales from 8.30 am to 9 am
morning_sale = sales_data.loc['2010-12-01 08:30:00':'2010-12-01 09:00:00','Description']
print(morning_sale)
