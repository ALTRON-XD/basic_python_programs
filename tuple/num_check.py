#check if a given number exists in a given tuple of numbers
num = tuple(map(int, input("Enter the numbers: ").split()))
n = int(input("Enter the number to check: "))
if n in num:
    print("number exists at index", num.index(n))
else:
    print("Number does not exist")
