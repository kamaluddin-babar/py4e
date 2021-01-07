# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count +1
    x = line.find('.')
    y = line[x-1:]
    total = total + float(y)
#    print(line)
#print(count)
#print(total)
result = (total/count)
a = "%.12f" % result
print("Average spam confidence:", a)
