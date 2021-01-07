
fruit = input("Enter a fruit name: ")
x = len(fruit)
ival = 0
count = 0
# String index with while loop
while ival < x :
#    print(" ", ival, " ",fruit[ival])
    ival = ival + 1
#String index with for loop
#for letter in fruit :
#    print(letter)

# Character count in a gven String
for letter in fruit :
    if letter == 'a' :
        count = count + 1
print(count)

if fruit < 'banana' :
    print('Your word,' + fruit + ',comes before banana.')
if fruit > 'banana' :
    print('Your word,' + fruit + ',comes After banana.')
if fruit == 'banana' :
    print("all right!")
