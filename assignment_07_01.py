# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
fcontend = fh.read()
fcontend.rstrip()
print(fcontend.upper())
