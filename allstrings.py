data = "Data science"
print(type(data))
print(len(data))
a=data.replace("science","Tech")
print(f'{a}')
list= ["a",1,23,"Miju","Bangladesh"]
print(list)
#accessing list values in start to end point
for i in range(0,5):
    print(list[i])
#accessing list values in end to start point
for i in range(4,-1,-1):
    print(list[i])
#%%
import pandas as pd
df= pd.read_excel(r"C:\Users\HP\Downloads\Crime Rate Dataset.xlsx")
print(df.head()) 