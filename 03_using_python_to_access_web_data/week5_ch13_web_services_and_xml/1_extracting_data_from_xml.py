import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')
if url == 'test' :
    url = 'http://python-data.dr-chuck.net/comments_42.xml'
elif len(url) < 1 :
    url = 'http://python-data.dr-chuck.net/comments_249668.xml'

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)
counts = tree.findall('.//count')
print 'Count: ', len(counts)

total = 0

for countValue in counts:
    total = total + int(countValue.text)

print 'Sum: ', total
