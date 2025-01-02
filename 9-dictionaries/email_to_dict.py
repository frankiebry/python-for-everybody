# For exercise 2 of chapter 9

fhand = open('txt-files\mbox-short.txt')
email_dict = dict()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From' : continue
    if words[2] not in email_dict:
        email_dict[words[2]] = 1
    else:
        email_dict[words[2]] += 1
        
print(email_dict)