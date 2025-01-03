import string # Import the string module

fhand = open('txt-files/romeo-full.txt') # Open the file
counts = dict() # Create an empty dictionary

for line in fhand: # Loop through the lines in the file
    line = line.translate(str.maketrans('', '', string.punctuation)) # Remove punctuation
    line = line.lower() # Convert to lowercase
    words = line.split() # Split the line into a list of words
    for word in words: # Loop through the words in each list
        if word not in counts: # If the word is not in the dictionary
            counts[word] = 1 # Add the word to the dictionary with a value of 1
        else: # If the word is in the dictionary
            counts[word] += 1 # Increment the value of the word by 1

# Sort the dictionary by value

lst = list() # Create an empty list
for key, val in list(counts.items()): # Loop through the items in the dictionary
    lst.append((val, key)) # Append the value and key to the list

# lst is now a list of tuples

# Sort the list in reverse order
lst.sort(reverse=True)

for key, val in lst[:10]: # Loop through the first 10 items in the list
    print(key, val) # Print the amount and the word