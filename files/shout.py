# Exercise 1 of Chapter 7: Files from the book Python for Everybody

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
for line in fhand:
    print(line.upper().rstrip())