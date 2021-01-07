# finding hours in mbox-short file with number of times it present
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhand = open(name)
counts = dict()
names = list()
for line in fhand :
    line.rstrip()
    if not line.startswith('From ') :
        continue
    words = line.split()
    #for word in words :
    words = words[5].split(':')
    counts[words[0]] = counts.get(words[0], 0) + 1
#print(counts)

lst = list()
for key, val in counts.items():
    newtup = (key, val)
    lst.append(newtup)
lst = sorted(lst, reverse=False)
#print(lst)
for key, val in lst:
    print(key, val)
