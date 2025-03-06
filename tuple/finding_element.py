#create a tuple with five elements and print its second and last elements 
subject = input("Enter the elements of the tupple : ").split() # input
subject = tuple(subject)
print (subject)
print("second element of the tupple is : ", subject[1])# print 2nd element
print("fourth element of the tupple is :", subject[-1])# print last
