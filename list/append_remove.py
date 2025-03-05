#Append a new element to a list and remove a specific element from it.
word = input("enter the number : ").split() #split() is used to split the string into list
word.append (input("enter the word to be append : ")) #append() is used to add the element to the list
word.remove (input("enter the word to be removed : ")) #remove() is used to remove the element from the list
print(word) #print the list
