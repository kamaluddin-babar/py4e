#writing in a file
fname = input('Enter a file name: ')
fout = open(fname,'w')
#print(fout)
print("Please write what you want below:\n")
while True:
    inptext = input()
    if inptext == 'done':
        break
    fout.write(inptext + '\n')
#    print(inptext)
fout.close()
