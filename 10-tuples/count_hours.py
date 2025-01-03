# Exercise 2 of Chapter 10

# Open the file
fhand = open('txt-files\mbox.txt')

# Initialize frequency dictionary
frequency = dict()

hours = list()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) < 6 or words[0] != 'From' : continue
    hours.append(words[5][:2])


for hour in hours:
    if hour not in frequency:
        frequency[hour] = 1
    else:
        frequency[hour] += 1
        
lst = list()
for key, val in list(frequency.items()):
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key, val)