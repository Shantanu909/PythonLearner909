import numpy as np
import pandas as pd
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

# Basic data structures in pandas
# Series:- One dimentional labeled array, Dataframe two dimentional , for Multidimentional labeled array

# # Task 1: Object creation using Series
# s = pd.Series([1,2,3,np.nan,7])
# print(s) 

# # Task 2: Object creation using DataFrame
# dates = pd.date_range("20230926",periods=4)
# print(dates)
# df = pd.DataFrame(np.array([[1,2],[3,4],[5,6],[7,8]]), index=dates, columns = list("AB"))
# print(df)

#Task3: Using Data Structue, Pass dictionsry
d = pd.DataFrame({1:"Tesla",2:"Pagani",3:"Mercedes",4:pd.Series("Buggati",index=list(range(5)))}, dtype="string")
print(d)
dic2 = {"A":100,"B":200,"C":500,"D":[1,2,3,4]}
df2= pd.DataFrame(dic2,dtype="float32")
print(df2)


#Task4 Data Analysis
print(d.head(2))
print(d.tail(2))
print(d.index)
print(d.columns)




#Post Lab
#1. NumPy representation of the underlying data with DataFrame.to_numpy()
print(d.to_numpy())
#2.describe() shows a quick statistic summary of your data
print(d.describe)
#3. Transposing your data:
print(d.transpose())
#4. Sorting your data (using DataFrame.sort_index()&DataFrame.sort_values())
print(df2.sort_index())
print("---------------------------------------------")
print(df2.sort_values(C))
#5. Selection (getitem[],slice:,label, position) 
print(d.get(2))
print(d.position)

