# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

#url = 'http://python-data.dr-chuck.net/comments_42.html'
url = 'http://python-data.dr-chuck.net/comments_204515.html'
#raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
count = 0
sum = 0 
tags = soup('span')
for tag in tags:
   # Look at the parts of a tag
   count += 1
   sum = sum + int(tag.contents[0])

print "Count ", count
print "Sum ", sum
