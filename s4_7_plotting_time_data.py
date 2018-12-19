import pandas as pd
import matplotlib.pyplot as plt
stock_price=pd.read_csv("intel.csv",parse_dates=True,index_col='Date')
#print(stock_price.head())
#stock_price.loc['2017-10-16':'2017-10-20',['Open','Close']].plot(style='.-', title='Intel', subplots=True)
stock_price.loc['2017-10-16':'2017-10-20',['Open','Close']].plot(title='Intel',style=',-',subplots=True)
plt.ylabel("Closing Price (US$)")
plt.show()
