# Using a function to streamline handling valid input
def get_valid_input(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number")

# Handling overtime
def compute_pay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    elif hours > 40:
        regular_pay = 40 * rate
        overtime_hours = hours - 40
        overtime_pay = rate * overtime_hours * 1.5
        pay = regular_pay + overtime_pay
    return pay

# Get valid inputs
hours = get_valid_input("Enter Hours: ")
rate = get_valid_input("Enter Rate: ")
pay = compute_pay(hours,rate)

# Display the result to the user
print(f"Pay: ${round(pay, 2)}")