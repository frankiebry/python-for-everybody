# For exercises 3 and 4 of chapter 9: Dictionaries

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

print(domain_dict)

# most_messages = None
# most_messages_count = None
# for key in email_dict:
#     if most_messages is None or email_dict[key] > most_messages_count:
#         most_messages = key
#         most_messages_count = email_dict[key]
        
# print(f'The email address with the most messages is {most_messages} with {most_messages_count} messages')