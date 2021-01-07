
fhand = open('mbox-short.txt')
count = 0
for cheese in fhand :
    count = count+1
print('Line Counter:',count)

fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])

khand = open('kamal-info.txt')
kread = khand.read()
print(len(kread))
print(kread[:154])


khandsearch = open('kamal-info.txt')
#kreadsearch = khandsearch.read()
for line in khandsearch :
    if line.startswith('the') :
        print(line)

fhand = open('mbox-short.txt')
for line in fhand :
    line = line.rstrip()
    if line.startswith('From:') :
        print(line)
