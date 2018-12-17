import pandas as pd
import matplotlib.pyplot as plt
#Import data
stock_prices = pd.read_csv("tesla.csv")

#Print stock price dataframe for ref
#print(stock_prices.describe())

#Print the minimum stock price for open
#print(stock_prices['Open'].min())
#Print the max stock price for Open
#print(stock_prices['Open'].max())
#Print the mean stock price for Open
#print(stock_prices['Open'].mean())

x_row = stock_prices['Date'].values
stock_prices['Open'].plot(x=x_row,y=open,kind='box')
plt.title('Tesla Opening Stock Prices')
plt.xlabel('Time')
plt.ylabel('Prices(US$)')
plt.show()
