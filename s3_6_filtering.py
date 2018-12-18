import pandas as pd
import matplotlib.pyplot as plt

#Get the data
#play_data = pd.read_csv("googleplaystore.csv")
stock_data = pd.read_csv("tesla.csv")
#Print data to show it is Working
#print(play_data.head())

#Print all rows with reviews greater than 5
#print(play_data[play_data['Rating']>=5.0])
#Create a conditional filter to find Arcade with the Genres column
#arcade_data = play_data[play_data['Genres']=='Arcade']
#Print arcade play_data
#print(arcade_data.head())
#Print stock price of Tela if opening is 315
print(stock_data[stock_data['Open']=315])
