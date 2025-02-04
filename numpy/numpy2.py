import numpy as np

arr=np.arange(0,11)
print(arr)

print(arr[8])

# slice method on array

print(arr[1:5])

print(arr[2:])

arr[0:5]=100
print(arr)

arr=np.arange(0,11)

slice_of_array=arr[0:5]
print(slice_of_array)

# copy of array not reference 

arr_copy=arr.copy()
print(arr_copy)
arr_copy[:]=100
print(arr_copy)
print(arr)

arr_2d=np.array([[5,10,4,] , [30,40,45] , [58,46,25]])
print(arr_2d)

# fetching value from 2d array 
# grab 5
print(arr_2d[0][0])
print(arr_2d[0])
print(arr_2d[1][1])
# passing row and col method 2 
print(arr_2d[2,1])

# how to fetch portion of 2d array usinf slice

print(arr_2d[:2 , 1:])


# conditional selection 

arr=np.arange(0,11)
print(arr)

bol_arr=arr>5
print(bol_arr) 

# need portion of arrasy using codnitonal selection 

print(arr[arr>5])
print(arr[arr<3])

arr_2d=np.arange(50).reshape(5,10)
print(arr_2d)


