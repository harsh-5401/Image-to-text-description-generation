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

# conditional selection 

print(df>0)

booldf=df>0
print(df[booldf])
print(df[df>0])

print(df)

print(df['w']>0)
# we only get rows that happen to be true 
print(df[df['w']>0])

# get all rows where z<0
print(df[df['y']<0])

print("...")
print(df[df['y']<0]['x'])

print(df[df['y']<0][['x' , 'y']])

booldf=df['w']>0
result=df[booldf]
print("result=" , result)
mycols=['x' ,'y']
print(result[mycols])

# // multiple condition

print([])


