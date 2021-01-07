
fname = input('Enter a file name: ')
if len(fname) <1 :
    fname = 'clown.txt'
fhand = open(fname)

di = dict()
for line in fhand:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        # idiom: retrive/create/update counter
        di[w] = di.get(w,0) + 1

#print(di)

# now we want to find the most common word
largest = -1
theword = None
for key, value in di.items():
    print(key,value)
    if value > largest:
        theword = key
        largest = value

print(theword,largest)
