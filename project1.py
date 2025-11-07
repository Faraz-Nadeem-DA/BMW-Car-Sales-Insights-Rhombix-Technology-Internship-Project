import pandas as pd
data=pd.read_csv("BMW sales data.csv")
print(data.head(5))


#Quick Overview of Dataset Info
print(data.info())

#Missing Values per Column
print(data.isnull().sum())

#Remove Duplicate Rows from dataset using remove duplicate
data=data.drop_duplicates()
#Handle Missing Values by fill numeric columns with median 
for col in data.select_dtypes(include="number").columns:
    data[col].fillna(data[col].median(),inplace=True)


#Correcting formation 
data.columns=data.columns.str.strip()
for col in data.select_dtypes(include="object").columns:
    data[col]=data[col].str.strip()



#describe the dataset 
print("Describe the dataset",data.describe())


#Save Cleanded dataset to create visuals
data.to_csv("BMW_clean_data.csv",index=False)


