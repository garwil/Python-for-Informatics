# Parse JSON for a list of numbers, count the entries and print a sum of all the numbers in the list

import urllib
import json

jsonfile = raw_input('JSON File: ')
urlhandle = urllib.urlopen(jsonfile)
data = urlhandle.read()
info = json.loads(data)
count = 0
sum = 0

for i in info['comments']:
    number = int(i['count'])
    sum = sum + number
    count = count+1

print sum
print count