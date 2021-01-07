# read a file and print its contend in upper case
fname = input('Enter a file name: ')
fhand = open(fname)
#fcontend = fhand.read()
for line in fhand :
    line = line.rstrip()
    print(line.upper())
