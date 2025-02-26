n = int(input("Enter a number: ")) # take input from user
a, b = 0, 1 # assign values to a and b
while a <= n: # loop
    print(a) # print the series
    temp = a
    a = b
    b = temp + b
