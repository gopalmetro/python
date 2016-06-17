import re

fname = raw_input("Enter file name (1 for 'regex_sum_42', 2 for 'refex_sum_249666'): ")
if fname == "1" or len(fname) < 1 : fname = "regex_sum_42.txt"
if fname == "2" : fname = "regex_sum_249666.txt"

try:
    fh = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()

numList = list()
total = 0

for line in fh :
    line = line.rstrip()
    numbers = re.findall('[0-9]\S*', line)
    if len(numbers) < 1 : continue
    for number in numbers :
        numList.append(int(number))
        total = total + int(number)
# print numList #DEBUG
print "Length: " + str(len(numList))
print "Total: " + str(total)
