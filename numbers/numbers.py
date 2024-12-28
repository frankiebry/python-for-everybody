"""
This solution uses a list and the append method which has not yet been taught by the book at this point
So I don't think they want you to do it this way
"""

# Initializing our list
number_list = []

# Handling input
while True:
    response = input('Enter a number (enter "done" to quit): ')
    if response.lower() == 'done': # Use .lower() to handle case insensitivity
        break
    else:
        try:
            number_list.append(int(response)) # Convert to integer and append to the list
        except ValueError:
            print('Please enter a valid number.')

# Math loops and calculations
count = 0
for number in number_list:
    count += 1

total = 0
for number in number_list:
    total += number
 
min = None
for number in number_list:
    if min == None or number < min:
        min = number
    
max = None
for number in number_list:
    if max == None or number > max:
        max = number 
        
# Calculate the average
if count > 0: # Avoid division by zero error
    average = total / count
else:
    average = None

# Output
print(number_list)
print(f'Total: {total}')
print(f'Count: {count}')
print(f'Average: {average if average is not None else "N/A"}')
print(f'Minimum: {min if min is not None else "N/A"}')
print(f'Maximum: {max if max is not None else "N/A"}')