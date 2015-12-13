import urllib
from BeautifulSoup import *

html = urllib.urlopen('http://www.schiochet.it').read()
soup = BeautifulSoup(html)
x = soup('a')
print x,"\n"