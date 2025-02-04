import numpy as np
import pandas as pd

#   series in pandas


labels=['a' , 'b' , 'c']

my_data=[10,20,30]

arr=np.array(my_data)

d={'a' : 10 , 'b' :20 , 'c' :30}

# creating series in python 

pd.Series(data = my_data)
print(pd.Series(data = my_data))

# to see index give index as labels 
# we see a as label and 10 as datapoint for that index  
print(pd.Series(data = my_data , index=labels))
# unlike numpy array i have datapoints that are labelled and i can call these
# datapoints using labels 

# simple way to define series 
print(pd.Series(my_data ,labels))

# another way of creating series

print(pd.Series(arr))

print(d)
# passing dictionary in seriees 

print(pd.Series(d))

print("labels =" , labels)
# sereis can hold variet of object types

print(pd.Series(data=[sum , print , len]))

# grap information from series using labels

ser1=pd.Series([1,2,3,4] , ['usa' , 'germany' , 'india' , 'italy'])

ser2=pd.Series([1,2,5,4] , ["usa" , 'germo' , 'italy' , 'india'])

print(ser1 )
print(ser2)

print(ser1['usa'])

# these type of operation is done on basis on label is same label is find operation is 
# performed or else return Nan
# performation arithmeric operation in series 
# our integer is converted in float so you dont loose any info

print(ser1 + ser2)






