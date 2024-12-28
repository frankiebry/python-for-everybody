"""
This solution does not use a list or the append method
which has not yet been taught by the book at this point
surprisingly it's fewer lines too
"""

# Initialize variables
total = 0
count = 0
min_value = None
max_value = None

# Handling input
while True:
    response = input('Enter a number (enter "done" to quit): ')
    if response.lower() == 'done':  # Use .lower() to handle case insensitivity
        break
    else:
        try:
            number = int(response)  # Convert to integer
            total += number
            count += 1
            
            # Update minimum and maximum values
            if min_value is None or number < min_value:
                min_value = number
            if max_value is None or number > max_value:
                max_value = number
        except ValueError:
            print('Please enter a valid number.')

# Calculate the average
if count > 0:  # Avoid division by zero error
    average = total / count
else:
    average = None

# Output
print(f'Total: {total}')
print(f'Count: {count}')
print(f'Average: {average if average is not None else "N/A"}')
print(f'Minimum: {min_value if min_value is not None else "N/A"}')
print(f'Maximum: {max_value if max_value is not None else "N/A"}')