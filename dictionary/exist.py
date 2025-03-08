# Check if a specific key exists in a dictionary.

# Define a dictionary with some key-value pairs
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Specify the key to check in the dictionary
key_to_check = 'b'

# Check if the specified key exists in the dictionary
if key_to_check in my_dict:
    # If the key exists, print a message indicating its presence
    print(f"Key '{key_to_check}' exists in the dictionary.")
else:
    # If the key does not exist, print a message indicating its absence
    print(f"Key '{key_to_check}' does not exist in the dictionary.")
