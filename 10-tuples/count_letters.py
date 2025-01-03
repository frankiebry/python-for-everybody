import string

with open('10-tuples/wiki-saturn-japanese.txt', encoding='utf-8') as fhand: # Open the file
    # Create a dictionary to store the counts of each letter 
    counts = dict() # Create an empty dictionary
    for line in fhand: # Loop through each line in the file
        line = line.rstrip() # Remove the newline character at the end of the line
        line = line.translate(str.maketrans('', '', string.punctuation)) # Remove punctuation
        line = line.lower() # Convert all characters to lowercase
        for char in line: # Loop through each character in the line
            if char != ' ':
                if char not in counts:
                    counts[char] = 1
                else:
                    counts[char] += 1

# Sort the dictionary by value                
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))
    
lst.sort(reverse=True)

for key, val in lst:
    print(f'The character {val} appears {key} times')
