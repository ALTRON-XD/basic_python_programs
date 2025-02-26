# factorial of a number using range function

num = int(input("enter number :")) # input from user
fact = 1 # initial value of fact
for i in range(1, num + 1): # range function
    fact = fact * i 
print("factorial of number is :", fact) 
