# Top 10 most common word in a file
fname = input('Enter a file name: ')
if len(fname) < 1:
    fname = 'romeo.txt'
fhand = open(fname)
counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
#print(lst)
for val, key in lst[:10]:
    print(key,val)
