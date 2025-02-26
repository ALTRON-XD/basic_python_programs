n = int(input("Enter a number: "))
a, b = 0, 1
while a <= n:
    print("The Fibonacci series for", n, "number is :", a)
    temp = a
    a = b
    b = temp + b
