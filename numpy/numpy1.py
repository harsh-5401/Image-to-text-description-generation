# run below commands to install numpy
# pip install numpy
# conda install numpy

    # ways to creat numpy arrays

import numpy as np

my_list=[123]
print(my_list)

arr=np.array(my_list)

print(arr)
print(type(arr))

my_mat=[[1,2,3] , [4,5,90] , [8,9,0]]
# note no of brackes indicate dimension sof array
print(np.array(my_mat)) 

# automatically generating array
print(np.arange(0,10))

# generate array of even number
print(np.arange(0,11,2))

# genrate array of zeroes 
print(np.zeros(3))

# first represnt row and another represent col 
print(np.zeros((5,4)))

# array of ones
print(np.ones((3,4)))

# linspace
# 100 evenly space point between 0 and 5
print(np.linspace(0,5,100))

# creat identity matrix using numpy
print(np.eye(4))


# creat array of random numbeers
print(np.random.rand(5))

print(np.random.rand(5,3))
    
# return samples from normal or gaussian distribution

print(np.random.randn(2,6))

# generate random array of integers betwwen 0 and 100

print(np.random.randint(1,100,10))


arr=np.arange(25)
print("arr=" ,arr)

ranarr=np.random.randint(0,100,30)
print(ranarr)




# methods on arrays

# reshape method ->return array with same data of new shape
# note -> you will get error if you were not able to fill the matrix
print(arr.reshape(5,5))

print(ranarr)
# max value in array

print(ranarr.max())
print(ranarr.min())

# index of max and min value 

print(ranarr.argmin())
print(ranarr.argmax())

# datatype in array

newarr=[8,9,10]
print(arr.dtype)


 
