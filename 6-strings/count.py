# Chapter 6 Exercise 3

def count(string, char):
    word = string
    count = 0
    for letter in word:
        if letter == char:
            count = count + 1
    print(f'The character "{char}" appears in the string "{string}" {count} times.')
    
string = input('Enter a string: ')
char = input('Enter the character you want to count in the string: ')
count(string,char)

# fruit = 'banana'
# print(fruit.count('a'))