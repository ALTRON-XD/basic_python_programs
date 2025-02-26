# factorial of a number using recursion

def factorial(n): #function defined
    if n == 0 or n == 1:
        return 1
    return  n * factorial(n - 1)   # function calling itself

print(factorial(int(input("enter number :")))) #taking input from user and printing the output
