# Write a python program to find the middle index in a list.
num = list(map(int, input("Enter numbers: ").split()))#user input
num.sort()#sortiong of numbers
print(num)
middle_index = len(num) // 2 #logic

if len(num) % 2 == 0:#condition
    print("Middle index is:", num[middle_index], num[middle_index - 1])

else:
    print("Middle index is:", middle_index)
