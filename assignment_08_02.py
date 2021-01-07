
# Counting a particular word in a file
fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if line.startswith('From '):
        words = line.split()
        print(words[1])
        count = count +1
print("There were", count, "lines in the file with From as the first word")


# this is an alternative solution for the same problem. Each provide same output.
fh = open(fname)
countl = 0
for line in fh:
    line = line.rstrip()
    wrd = line.split()
    if len(wrd)<3 or wrd[0] != 'From':
        continue
    countl = countl +1
    print(wrd[1])
print("There were", countl, "lines in the file with From as the first word")
