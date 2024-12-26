# # handling input
# while True:
#     hours = input("Enter Hours: ")
#     try:
#         hours = float(hours)
#         break
#     except ValueError:
#         print("Please enter a valid number")
        
# while True:
#     rate = input("Enter Rate: ")
#     try:
#         rate = float(rate)
#         break
#     except ValueError:
#         print("Please enter a valid number")

# using a function to streamline handling input
def get_valid_input(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number")

# Get valid inputs
hours = get_valid_input("Enter Hours: ")
rate = get_valid_input("Enter Rate: ")

# handling overtime
if hours <= 40:
    pay = hours * rate
elif hours > 40:
    regular_pay = 40 * rate
    overtime_hours = hours - 40
    overtime_pay = rate * overtime_hours * 1.5
    pay = regular_pay + overtime_pay
print(f"Pay: ${round(pay, 2)}")