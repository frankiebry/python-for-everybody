# Exercise 4 from Chapter 8 of the book "Python for Everybody" by Charles Severance

fhand = open('files/romeo.txt')
word_list = list() # create an empty list
for line in fhand:
    word_list += line.split()
    
unique_words = list()
for word in word_list:
    if word not in unique_words:
        unique_words.append(word)
        
print(sorted(unique_words))