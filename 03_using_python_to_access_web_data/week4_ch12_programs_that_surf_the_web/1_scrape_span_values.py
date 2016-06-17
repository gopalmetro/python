# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program
# based on this code: http://www.pythonlearn.com/code/urllink2.py

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

numList = list()
count = 0
total = 0

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    numList.append(int(tag.contents[0]))
    # Look at the parts of a tag
    # print 'TAG:',tag
    # print 'URL:',tag.get('href', None)
    # print 'Contents:',tag.contents[0]
    # print 'Attrs:',tag.attrs
    # count += 1 # Quick and dirty
    # total = total + int(tag.contents[0]) # Quick and dirty

count = len(numList)
total = sum(numList)
print "Count " + str(count)
print "Sum(total) " + str(total)
# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program
# based on this code: http://www.pythonlearn.com/code/urllink2.py

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

numList = list()
count = 0
total = 0

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    numList.append(int(tag.contents[0]))
    # Look at the parts of a tag
    # print 'TAG:',tag
    # print 'URL:',tag.get('href', None)
    # print 'Contents:',tag.contents[0]
    # print 'Attrs:',tag.attrs
    # count += 1 # Quick and dirty
    # total = total + int(tag.contents[0]) # Quick and dirty

count = len(numList)
total = sum(numList)
print "Count " + str(count)
print "Sum(total) " + str(total)
