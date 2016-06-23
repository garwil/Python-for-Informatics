# Follow the Nth link in a document X times and print the content of the final <a> tag.

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
position = raw_input("Which position?")
count = raw_input("How many times?")
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

while count > 0:
    tags = soup('a')
    link = tags[position-1]
    url = link['href']
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    count = count -1

print link.contents[0]






    
    