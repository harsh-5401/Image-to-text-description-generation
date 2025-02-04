# map function 
seq=[1,5,8,6]

def times2(var):
    return var*2


print(list(map(times2 , seq)))

mapped=list(map(times2 , seq))
print(mapped)

# filter function  in python 

seq2=[-1, 8, 9 ,1 ,-4]

def postivenumber(var):
    # for items in var :
        if (var>0) :
            return var
        
filter(postivenumber , seq2)
# get all postive number
print(list(filter(postivenumber , seq2)))


# methods in pyhton

s="my name is #Harsh" 
print(s.lower())
print(s.upper())
# split all the white space 
print(s.split())
print(s.split("#"))
print(s.split("#")[1])

d={
     "k1" : "harsh",
     "k2" : "singh"
}

print(d.keys())
print(d.items())

mylist=[1,9,7,10]

# removing items from list 
mylist.pop()
print(mylist)


print(mylist.index(7))

# search items inside list 

print(9 in mylist)

# tuple unpacking

# list of tuple 

x=[(1,5) , (7,8) , (2, 6)]

for items in x:
    print(items)

for (a,b) in x :
     print(a)

for (a,b) in x :
     print(b)
    
