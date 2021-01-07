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
print(counts)

for a,b in counts.items() :
    print(a,b)
max_key = max(counts, key = counts.get)
print('\n'+ max_key, counts[max_key])
