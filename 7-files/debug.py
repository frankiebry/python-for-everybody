# Exercises 2 & 3 from Chapter 8: Lists

fhand = open('files/break-test.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) < 3 or words[0] != 'From' : continue
    print(words[2])