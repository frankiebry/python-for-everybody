# Exercises 2 and 3 of Chapter 7: Files from the book Python for Everybody

fname = input('Enter the file name: ')
if fname == 'na na boo boo':
    print('NA NA BOO BOO TO YOU - You have been punk\'d!')
    exit()
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
    
count = 0
sum = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        number = float(line[line.find(':')+1:])
        sum += number
        count += 1

print('Average spam confidence:', sum/count)