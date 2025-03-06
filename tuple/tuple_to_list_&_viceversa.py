#write a python program to convert a tuple into a list and vice versa.
name = input("Enter the name: ") #input the name
a= tuple(name.split())#convert the name into tuple
b = list(a)#convert the tuple into list
c = tuple(b)#convert the list into tuple
print(b)
print(c)
