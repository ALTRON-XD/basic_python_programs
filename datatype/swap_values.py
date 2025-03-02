#write a program to swap two  number without using third variable
a = int(input("Enter the first number: ")) #taking input from user
b = int(input("Enter the second number: ")) #taking input from user
a=a+b # a = 4 + 8 = 12
b=a-b # b = 12 - 8 = 4
a=a-b# a = 12 - 4 = 8
print("After swapping ", a, b)
