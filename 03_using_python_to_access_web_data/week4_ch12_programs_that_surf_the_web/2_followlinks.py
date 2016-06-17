# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

# get starting URL (with lazy code for testing and running the program)
url = raw_input('Enter URL: ')
if url == 'test' :
    url = 'http://python-data.dr-chuck.net/known_by_Fikret.html '
elif len(url) < 1 :
    url = 'http://python-data.dr-chuck.net/known_by_Phillipa.html'

# get Count value (with lazy code for testing and running the program)
count = raw_input('Enter Count: ')
if count == 'test':
    count = 4
elif len(count) < 1 :
    count = 7

# get Position value (with lazy code for testing)
pos = raw_input('Enter Position: ')
if pos == 'test' :
    pos = 3
elif len(pos) < 1 :
    pos = 18

# convert position to integer and offset for 0 index
pos = int(pos)-1

# 'while loop' iteration variable
i = 0

# perform a "while" loop 'count' times
while i <= count :
    print "Retrieving: " + url # print url. placed at beginning of loop to include original url
    html = urllib.urlopen(url).read() # open socket, establish connection and read entire html document into the 'html' list
    soup = BeautifulSoup(html) # parse html list with BeautifulSoup library and store it in the 'soup' list
    tags = soup('a') # locate all link elements in the 'soup' list and store in tags
    tag = tags[pos] # store the tag data (this should be a link url) located at the 'pos' position in the tags list into the tag list
    url = tag.get('href', None) # extract the href content from the tag list and store it in the 'url' variable
    i += 1 # increment loop iteration variable
