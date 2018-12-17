import pandas as pd

counties = ['Antrim','Armagh','Carlow','Cavan','Clare','Cork','Derry','Donegal','Down','Dublin','Fermanagh','Galway',
            'Kerry','Kildare','Kilkenny','Laois','Leitrim','Limerick','Longford','Louth','Mayo','Meath','Monaghan',
            'Offaly','Roscommon','Sligo','Tipperary','Tyrone','Waterford','Westmeath','Wexford','Wicklow']


#Use broadcasting to assign a list to a value and create a dataframe

# Create a string with the value 'Ireland'
country = "IRELAND"
#Create a new dictionary
ireland = {'Country':country, 'county':counties}
#Create a dataframe from the dictionary
df=pd.DataFrame(ireland)
print(df)
