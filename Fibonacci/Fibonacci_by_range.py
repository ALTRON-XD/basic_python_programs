num = int(input("Enter a number: ")) # take input from the user
a, b = 0, 1 # assign 0 to a and 1 to b
for i in range(num): # loop through the range of the number
    print(a) 
    temp = a
    a = b
    b = temp + b
