# average calculating of some number using loop
total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done' :
        break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print('Average:', average)

# average calculating of some number using list
numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done' :
        break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average:', average)
