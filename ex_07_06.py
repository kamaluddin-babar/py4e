#user input file handling
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except Exception as e:
    if fname == 'na na boo boo' :
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else :
        print("There was no such a file named", fname)

    exit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count +1
print('There were', count, 'Subject line in', fname)
