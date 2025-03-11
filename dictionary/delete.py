# Remove a key-value pair from a dictionary.
dic ={
    input("enter key1 : ") : input("enter value1 : "),
    input("enter key2 : ") : input("enter value2 : "), 
}
i = input("enter the key to be deleted : ")
del dic[i]
print("key is deleted")
print(dic)
