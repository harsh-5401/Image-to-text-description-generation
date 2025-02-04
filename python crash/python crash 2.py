# creat dictionary in python 

dictionary={
    "key1" : "value",
    "key2" : 123,
    "key3" : "harsh"
}

print(dictionary['key2'])

print(dictionary)

# once we creat new dictionary with same name all the data of all dictionary will be lost
dictionary={
    "k1" : [1 , 55 , 9]
}

print(dictionary)

print(dictionary['k1'][1])

# nested dictionary
nesteddictionary={
    "k1" : {
        "innerkey" : [1,88,99]
    }
}

print(nesteddictionary["k1"]["innerkey"][1])

# booleans in python 


# note : tuple are immutable and they do not support  item assignment 

mylist=[1,2,3]

mmy_tuople=(1,2,3)
print(mmy_tuople[0])

# same useing slice opeations 
print(mmy_tuople[1:])


# sets in python 
# set is a collection of unique element

my_set={1,2,3,3,3,1}
# we only get each element once 
print(my_set)

# another way of using set 
print(set([1,1,1,1,5,6,6,6,8]))

# add element to set 
my_set.add(9)
print(my_set)

# comparing elements
print(1>2)
print(1==1)

print((1>2) and (2>3))

print(True and False)

# if else statement 
if(1<2) :
    print("its is true")

    

if 1==2 :
    print("print first")
else :
    print("last")        
