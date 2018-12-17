import pandas as pd
import matplotlib.pyplot as plt

#Import data file
stock_prices = pd.read_csv("intel_amd_stock_prices.csv")
  

#Print data frame
print(stock_prices)


#Create y column
y_columns=['intel','amd']


# Assign axis
stock_prices.plot(x='month',y=y_columns)


#Create plot tilte
plt.title('Monthly Stock Prices')


#Create a title for y axis
plt.ylabel('Prices (US$)')


#Show the pyplot
plt.show()
