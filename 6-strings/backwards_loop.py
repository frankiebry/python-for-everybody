# for exercise 1 in chapter 6

fruit = 'bananas'
length = len(fruit)
index = length - 1

while index >= 0:
    letter = fruit[index]
    print(letter)
    index -= 1

# exercise 2
print(fruit[:])