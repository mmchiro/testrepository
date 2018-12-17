import pandas as pd


#course_sales = {'course':['Python','Ruby','Excel','C++'], 'day':['Mon','Tue','Wed','Tue'],'price':[5,10,15,20],'sale':[2,3,5,7]}

#print(course_sales)
#Converting dictionary into a dataframe. The keys of the dictionary become the dataframe columns.
#df=pd.DataFrame(course_sales)
#print(df)
course = ['Python','Ruby','Excel','C++']
day = ['Mon','Tue','Wed','Tue']
price = [5,10,15,20]
sales = [2,3,5,7]
Labels = ['Course','Day','Price','# Sales']

cols = [course,day,price,sales]

master_list = list(zip(Labels,cols))
print(master_list)

data=dict(master_list)
df_sales = pd.DataFrame(data)
print(df_sales)

#Add new column 'New Price'
df_sales['New Price']=2
print(df_sales)
