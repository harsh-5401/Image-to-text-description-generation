import numpy as np

arr=np.arange(0,11)
print(arr)

# when we add two array their index get added

print(arr+arr)
print(arr*arr)

# add 100 to every element in array
# same for addition/subs/mul/divison 
print(arr+100)

# divide 0/0 give nan(not a number )
print(arr/arr)

print(1/arr)

print(arr**2)

# universal array function 

# aquare root of array
print(np.sqrt(arr))

# max number in array
print(np.max(arr))
print(arr.max())

# expoential of array
print(np.exp(arr))

# sine of every value in array
print(np.sin(arr))