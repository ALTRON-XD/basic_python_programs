#check whether a string is palindrome or not
str = input("enter your string :")#taking input from user
str1 = str[::-1]#reversing the string
if str == str1:#checking whether the string is palindrome or not
	print("your string is palindrome")
else :
	print("your string isn't a palindrome")
