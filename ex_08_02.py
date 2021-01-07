# example of spliting string
fhand = open('words.txt')
for line in fhand :
    line = line.rstrip()
    words = line.split()
    print(words)
