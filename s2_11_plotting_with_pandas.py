import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv("intel.csv", index_col = 'Date', parse_dates = True)

#print(df.info())
#print(df.head())
close_value = df['Close'].values
#print(type(close_value))

#plt.plot(close_value)
#plt.show()

# Only show the close pricing values pyplot
#df['Close'].plot (color = 'g', style ='-', legend = True)
#plt.axis(('2017','2018',0,60))
df.plot(color='blue')
plt.title('Stock Price')
plt.xlabel('Date Range')
plt.ylabel('Price($)')
#plt.show()
#Save the graph to a picture
plt.savefig('df.pdf')
