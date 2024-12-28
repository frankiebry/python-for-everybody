def get_valid_input(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number")

def compute_grade(score):
    if score >= 0.9:
        grade = 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    elif score < 0.6:
        grade = 'F'
    return grade
    

while True:
    score = get_valid_input("Enter a score between 0.0 and 1.0: ")
    if 0.0 <= score <= 1.0:
        break
    else:
        print("Out of range")
        
print(compute_grade(score))