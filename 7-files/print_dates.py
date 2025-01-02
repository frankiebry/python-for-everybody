# this code throws an index out of range error

fhand = open('files/mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    # print(f"Processing line: {line}")  # Debugging print
    if not line.startswith('From '): continue
    words = line.split()
    # print(f"Words: {words}")  # Debugging print
    if len(words) < 3: continue
    print(words[2])