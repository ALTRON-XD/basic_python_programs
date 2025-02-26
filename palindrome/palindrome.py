word = input("Enter a word: ") # input from user
if word == word[::-1]: # check if the word is palindrome
    print("Palindrome") # print if it is palindrome
else: 
    print("Not a palindrome") # print if it is not palindrome
