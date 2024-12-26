def get_valid_input(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number")

while True:
    score = get_valid_input("Enter a score between 0.0 and 1.0: ")
    if 0.0 <= score <= 1.0:
        break
    else:
        print("Out of range")
        
if score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
elif score < 0.6:
    print('F')