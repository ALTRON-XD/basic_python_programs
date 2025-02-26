def Fibonacci(a):
    a, b = 0, 1
    while a <= 0:
        print(a)
        temp = a
        a = b
        b = temp + b
    return a

Fibonacci(int(input("Enter a number: ")))
