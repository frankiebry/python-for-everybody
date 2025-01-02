def calculate_exponent(base, exponent):
    # Handle edge cases
    if exponent == 0:
        return 1
    elif exponent < 0:
        # Handle negative exponents
        base = 1 / base
        exponent = -exponent

    # Calculate positive exponents
    result = 1
    for _ in range(exponent):
        result *= base

    return result

# Input from the user
num = int(input("Enter a number: "))
exp = int(input("Enter an exponent: "))

# Call the function and display the result
result = calculate_exponent(num, exp)
print(f"{num} raised to the power of {exp} is {result}")