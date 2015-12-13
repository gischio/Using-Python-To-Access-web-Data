# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

#url = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html'
url = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Rebekkah.html'
#url = raw_input('Enter - ')
count = int(raw_input('Enter count: '))
position = int(raw_input('Enter position: '))

taglist = list()
urllist = list()
urllist.append(url)

print 'Retrieving: ', urllist[0]


for i in range(count):
    html = urllib.urlopen(urllist[-1]).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    taglist = list()
    for tag in tags:
        taglist.append(tag)
    url = taglist[position-1].get('href', None)
    print 'Retrieving: ', url
    urllist.append(url)
print 'Last Url: ', urllist[-1]
	