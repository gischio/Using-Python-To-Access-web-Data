import urllib
import xml.etree.ElementTree as ET

#url = 'http://python-data.dr-chuck.net/comments_42.xml'


url = raw_input('Enter location: ')


print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)
counts = tree.findall('.//count')
print 'Count: ' , len(counts)
sum = 0
for item in counts:
    sum = sum + int(item.text)
print "Sum: ", sum