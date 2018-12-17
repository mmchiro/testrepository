import pandas as pd
import matplotlib.pyplot as plt
#import datafile
life = pd.read_csv("irish_life_expec.csv")

print(life.head())


# Scatter plot with x axis as year and y axis as life expec
life.plot(kind='scatter',x='year',y='life expec')
#Plot title,x label, y label

plt.title('Irish Life Expectancy')
plt.xlabel('Age')
plt.ylabel('Life Expectancy')
#Show Plot
plt.show()
