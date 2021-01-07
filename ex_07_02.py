#user input file handling
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except Exception as e:
    print("There was no such a file named", fname)
    exit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count +1
print('There were', count, 'Subject line in', fname)
