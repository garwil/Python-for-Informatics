# Find numbers in a text file using regexp, convert to integers and print the sum.
# Use regex_sum_230942.txt

import re

try:
    handle = open("regex_sum_230942.txt")
except:
    print "Error: Invalid file name."
    exit()
total = 0
line=handle.read()
numbers = re.findall('[0-9]+',line)
for i in numbers: total = total + int(i)  

print total