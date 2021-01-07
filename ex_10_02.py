
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

tmp = list()
for k,v in di.items():
    #print(k,v)
    newtup = (v,k)
    tmp.append(newtup)

tmp = sorted(tmp,reverse=True)
#print(tmp[:5])

for v,k in tmp[:5]:
    print(k,v)
