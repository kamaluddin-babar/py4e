# Find all unique word in a file
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
#    print(words)
    for i in words:
        if i in lst:
            continue
        lst.append(i)
lst.sort()
print(lst)
