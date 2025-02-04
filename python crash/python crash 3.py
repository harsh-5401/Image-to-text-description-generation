# for loop 
seq=[1,2,3,4,5,880]

for items in seq:
    print(items)

# while loop  
# 

i=1
while i < 5 :
    print("i is {}".format(i))
    i=i+1


# print natuural number using range object
# my_range=range(0,9)
for items in range(0,9) :
    print(items)

# if you want it to be list
print("hello")

# it willl include 1 but not 9
print(list(range(1,9)))


# function in python 

def addtwo_number(num1 , num2) :
    print(num1+num2)

addtwo_number(2,3)

# add deaafult value to function of not passed

def add_two_number(num1=6 , num2=7) :
    print(num1+num2)

add_two_number()

def squarenumber(num1) :
   return num1**2

print(squarenumber(8))

