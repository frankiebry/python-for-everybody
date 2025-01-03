# For exercises 1 chapter 10: Tuples

def email_to_domain(string):
    return string.split('@')[1]

fhand = open('txt-files\mbox.txt')
email_dict = dict()

for line in fhand:
    words = line.split()
    if len(words) < 1 or words[0] != 'From' : continue
    if words[1] not in email_dict:
        email_dict[words[1]] = 1
    else:
        email_dict[words[1]] += 1
        
domain_dict = dict()
for key in email_dict:
    domain = email_to_domain(key)
    domain_dict[domain] = email_dict[key]

new_lst = list()
for key, val in list(domain_dict.items()):
    new_lst.append((val, key))

print(f'The person with the most emails is {new_lst[0][1]} with {new_lst[0][0]} emails')