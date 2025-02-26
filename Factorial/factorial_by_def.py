def factorial(a): #function defined
    result = 1
    for i in range(1, a + 1): #loop  with range
        result *= i
    print(result)
    return result

factorial(int(input("Enter a number: "))) # function calling
