# Exercise 5 from Chapter 8 of the book "Python for Everybody" by Charles Severance

fhand = open('txt-files/mbox-short.txt')

count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) < 2 or words[0] != 'From' : continue
    print(words[1])
    count += 1
    
print('There were', count, 'lines in the file with From as the first word')