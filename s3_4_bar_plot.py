import pandas as pd
import matplotlib.pyplot as plt
#Import datafile

stock_prices = pd.read_csv("intel_stock_price.csv")
print(stock_prices)
#Bar plot with x axis and y axis


stock_prices.plot(kind='bar',x='month', y='price',color='blue')
#Plot title, x label, y label

plt.title('Intel Stock Prices')
plt.xlabel('Months')
plt.ylabel('Price(US$)')

#show plot
plt.show()
