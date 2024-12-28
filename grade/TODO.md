# Possible improvements

Instead of an if-elif chain, use a dictionary to map score ranges to grades?

Example:

````python
grade_mapping = {
    0.9: 'A',
    0.8: 'B',
    0.7: 'C',
    0.6: 'D',
    0.0: 'F'
}

for threshold, grade in grade_mapping.items():
    if score >= threshold:
        print(grade)
        break
````

Learn about how this works first before using it.

A simple match statement, similar to an if-elif chain, is possible too:

````python
match score:
    case score if score >= 0.9:
        print('A')
    case score if score >= 0.8:
        print('B')
    case score if score >= 0.7:
        print('C')
    case score if score >= 0.6:
        print('D')
    case _:
        print('F')
````