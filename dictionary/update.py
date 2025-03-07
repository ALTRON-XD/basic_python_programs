# Write a Python program to update a dictionary value for a given key
num = { input("Enter the key: ") : input("Enter the value: "), 
    input("enter the 2nd key:") : input("enter the 2nd value: "),
    input("enter the 3rd key: ") : input("enter the 3rd value: ")
}#input
print(num)
key = input("enter key to change: ")#input key to change
value = input("enter new value : ")#input new value
num[key] = value
print("change : ", num)
