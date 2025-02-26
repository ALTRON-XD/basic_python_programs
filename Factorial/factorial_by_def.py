def factorial(a):
    result = 1
    for i in range(1, a + 1):
        result *= i
    print(result)
    return result

factorial(int(input("Enter a number: ")))
