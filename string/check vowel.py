# Check how many vowels are in a string
q = input("Enter a word: ")#input
vowels = "a","e","i","o","u"
count = sum(1 for char in q if char in vowels)#counting the vowels
print(count)
