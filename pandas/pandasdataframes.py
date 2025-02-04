import numpy as np
import pandas as pd
from numpy.random import randn

# main tool for working wwith pandas

np.random.seed(101)

# creating dataframe

# pass- dataargument , index , column 
# what we have is list of col w, x, y ,z and rows as a, b, c, d, e 
# all column are  panda series that share a common index 
df=pd.DataFrame(randn(5,4) , ['a' , 'b' , 'c' ,'d' , 'e'] , ['w' , 'x' , 'y' , 'z'])
print(df)
print(".")
print(df['w'])

# get multiple col from dataframe 

print(df[['w' , 'x']])
print(df['w']['a'])

print(type(df))

# we can see that 'w' is a seeries 
print(type(df['w']))

# creating new col 
df['new']= df['w'] + df['x']
print(df)

# delting column 

# use axis=1 to refer to column and inplace = true so that changes is made to original
# dataframe otherwise it will return new dataframe 
# my deafult axis=0
df.drop('new' , axis=1 , inplace=True)
print(df)

# to delete colum 
df.drop("a" , inplace=True)
print(df)

print("..................")
# fetch rows in dataframe
# rows are also series as weel
print(df.loc['b'])

# // fetching row on basing of row index 
print(df.iloc[2])

# get subset of row and col  from dataframe

print("df=" , df)

print(df['x']['b'])
print(df.loc['b']['x'])


print(df.loc[['b' , 'c'], ['w' , 'y']])

