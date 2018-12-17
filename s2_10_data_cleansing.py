import pandas as pd


column_names = ['App','Rating','Reviews','Size','Number of Install','Type','Price','Last Updated']
filepath =("edited_googleplaystore_dataset.csv")
df=pd.read_csv(filepath, header = None, names = column_names, na_values="-1")

#print(df)
#Find info on DataFrame
#print(df.info())
df.index=df['Last Updated']
#print(df.tail())

new_columns = ['App','Reviews']
df=df[new_columns]
#print(df)
out_csv ="Google Play Data edited"
df.to_csv(out_csv)
#Output to Excel
#Need to install openpyxl module pip install openpyxl to work this
out_xlsx = "Google Play Data EXCEL.xlsx"
df.to_excel(out_xlsx)
