# // assign variabel
var =5
print(var)

x=4
x=x+x
print("printing x =" , x)

name_of_var=9


# strings

str1='this is a string'
print(str1)

str2="this is also a string"
print(str2)

# using variable value in string 
special_string="my number is {} and my name is {}".format(var , str1)
print(special_string)

myname="harsh"
# type 2
print("my name is {name} and my age is {age}".format(name=myname , age=var ))

string="shivam"
print(string[2])

# slice in string
# printing including 1th index and later index till end 
print(string[1:])

# printing everyhting upto but not including index3
print(string[:3])

# list/conside it as array 

arr=[1,2,3,"abc"]
print(arr)

# add itsms to list
arr.append(125)
print(arr)

# note we can apply slice methids on list same as string 


# list inside list 

nest=[1,2,[6,"abc"]]
print(nest)

print([nest[2]])

nestedlist=[1,2,[6,"abc" , [45 , 89 , "def"]]]
# get items from nested list 
print(nestedlist[2][2][1])

