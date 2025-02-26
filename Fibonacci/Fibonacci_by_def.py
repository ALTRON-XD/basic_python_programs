def Fibonacci(n): # function definition
    a, b = 0, 1 # multiple assignment
    while a <= n: # while loop
        print(a)
        temp = a
        a = b
        b = a + temp
    return a # return statement

Fibonacci(int(input("Enter a number: "))) # function call
