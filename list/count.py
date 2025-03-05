# Write a python script to count the occurrence of a given element in a list

# Input the list of elements
elements = input("Enter the elements of the list separated by space: ").split()

# Input the element to count
element_to_count = input("Enter the element to count: ")

# Count the occurrences of the element
count = elements.count(element_to_count)

# Print the count
print(f"The element '{element_to_count}' occurs {count} times in the list.")
