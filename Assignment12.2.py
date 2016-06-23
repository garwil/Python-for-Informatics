# Count the number of <span> tags in an HTML document and print the sum of the numbers contained within the tags.

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
count = 0
sum = 0

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    number = int(tag.contents[0])
    count = count+1
    sum = sum + number

print count
print sum
    
    