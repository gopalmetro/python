import json
import urllib

#shortcut code for fixed URLs
url = raw_input('Enter location: ')
if url == 'test' :
    url = 'http://python-data.dr-chuck.net/comments_42.json'
elif len(url) < 1 :
    url = 'http://python-data.dr-chuck.net/comments_249672.json'

# define accumulator variable
acc = 0

# open and connect to the url
connection = urllib.urlopen(url)
# read all of the data from the url
data = connection.read()

# parse all of the data as JSON and store it in the 'info'
info = json.loads(data)
#print json.dumps(info, indent=4) # print as pretty JSON

# cycle through all items in the "Comments" dictionary
for item in info['comments']:
    acc = acc + item['count']
    # print 'count', item['count']
    # print 'name', item['name']

print "Retrieving",url # print URL accessed
print "Retrieved",len(data),"characters" # print total number of characters retrieved
print 'Count:',len(info['comments']) # count the number of entries
print "Total:",acc # print accumulated total
