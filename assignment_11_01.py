# counting all number from a file and calculate their sum.
#Use these three file as sample data
# number-extraction.txt  regex_sum_42.txt  regex_sum_1096400.txt
import re
hand = open('regex_sum_1096400.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('([0-9]+)',line)
    for i in stuff:
        num = int(i)
        numlist.append(num)
print(sum(numlist))
