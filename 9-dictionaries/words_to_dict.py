fhand = open('dictionaries/words.txt')

my_dictionary = dict()
for line in fhand:
    words = line.split()
    for word in words:
        my_dictionary[word] = 'definition'
    
if 'apple' in my_dictionary:
    print('apple is in the dictionary')
else:
    print('apple is not in the dictionary')
    
if 'program' in my_dictionary:
    print('program is in the dictionary')