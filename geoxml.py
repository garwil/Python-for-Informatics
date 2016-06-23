# Parse XML for a list of numbers, count the entries and print a sum of all the numbers in the list

import urllib
import xml.etree.ElementTree as ET

xmlfile = raw_input('XML File: ')
data = urllib.urlopen(xmlfile)
tree = ET.parse(data)


count = 0
sum = 0
counts = tree.findall('.//count')

for i in counts:
    print i.text
    sum = sum + int(i.text)
    count = count + 1

print sum
print count