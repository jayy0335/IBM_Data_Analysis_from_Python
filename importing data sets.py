import pandas as pd 
path=("USA_cars_datasets.csv")
df=pd.read_csv(path) #to off the header we can do (path,header=none)
headers=["id","price","brand","model","year","title_status","mileage","color","vin","lot","state","country","condition"]
df.columns = headers

# print(df.head())

# To save the data you can choose your required extension (csv,xlsx etc)
# df.to_csv("automobiles.csv")

# To find the data types of each header
# print(df.dtypes)

# To find the Statistical summary with below code
# print(df.describe(include="all"))

# To find the quick summary of your dataset
# print(df.info())
