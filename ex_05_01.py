#Counting largest number
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9,41,12,3,74,15] :
    if the_num>largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)

# Sum calculating
zork = 0
print('Before', zork)
for thing in [9,41,12,3,74,15] :
    zork = zork + thing
    print(zork, thing)
print('After', zork)

# Large number, sum, average calcution
count = 0
sum = 0
print('Before', count, sum)
for value in [9,41,12,3,74,15] :
    count = count +1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, int(sum / count))

# Loop filtering example
print('Before')
for value in [9,41,12,3,74,15] :
    if value > 20 :
        print('Large number', value)
print('After')

#Search using a boolean variable
found = False
print('Before', found)
for value in [9,41,12,3,74,15] :
    if value == 3 :
        found = True
    print(found, value)
print('After', found)

# How to find the Smallest value
smallest_so_far = None
print('Before', smallest_so_far)
for the_num in [9,41,12,3,74,15] :
    if  smallest_so_far is None :
        smallest_so_far = the_num
    elif the_num < smallest_so_far :
        smallest_so_far = the_num
    print(smallest_so_far, the_num)
print('After', smallest_so_far)
