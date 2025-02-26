def palindrome(n): # define a function palindrome with a parameter n
    if n == n[::-1]: # check if the string is equal to its reverse
        print ("True")
    else:
        print ("False")
    return n # return the value of n

palindrome(input("Enter a string : ")) # Enter a string : madam
