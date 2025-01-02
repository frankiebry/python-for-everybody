# Exercise 1 from chapter 8: Lists

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def chop(t):
    del t[0]
    del t[-1]
    
def middle(t):
    return t[1:-1]

print(list1)
print(id(list1))
chop(list1)
print(list1)
print(id(list1))
print(' ')
print(list2)
print(id(list2))
list2 = middle(list2)
print(list2)
print(id(list2))