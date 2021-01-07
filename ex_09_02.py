# Counting words in a file
fname = input('Enter a file name: ')
fhand = open(fname)
counts = dict()
names = list()
for line in fhand :
    line.rstrip()
    words = line.split()
    for word in words :
        counts[word] = counts.get(word, 0) + 1
#print(counts)

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount :
        bigword = word
        bigcount = count
print(bigword, bigcount)
