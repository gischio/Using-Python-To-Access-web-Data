import json
import urllib

url = raw_input('Enter location: ')
#url = 'http://python-data.dr-chuck.net/comments_42.json'

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

info = json.loads(data)
print "Count:", len(info["comments"])

i = 0
sum = 0
while i < len(info["comments"]):
  sum += info["comments"][i]['count']
  i += 1
print "Sum:", sum
