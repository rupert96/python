import twitter
import datetime
import urllib
import urllib2
#importing libraries

user = 238760074
#My Twitter user ID

file = open("twitter credentials.txt")
creds = file.read().split('\n')
file.close()
#My Twitter credentials in a text file - loading into python file and splitting by line

cHistoryFile = open("/Users/rjhawkins/Library/Application Support/Google/Chrome/Default/Current Session")
cHistoryContents = cHistoryFile.read()
#Variable named "cHistoryContents" containing the file of HTML of my chrome search history being loaded and read into python file

cHistorySearch = cHistoryContents.rfind("http")
eIndex = cHistoryContents.find(chr(0),cHistorySearch)
cHistoryURL = cHistoryContents[cHistorySearch:eIndex]
#Variable called cHistorySearch that searches cHistoryContents for "http" as its the beginning of any web address - rFind searches the file from end to start rather than start to end.
#Variable eIndex searches cHistoryContents for the binary code "0" as in chrome this is the end of most links before invisible code - this is to leave us with a short link rather than entire link.
#cHistoryURL cuts off the link where the 0 is

response = urllib2.urlopen(cHistoryURL)
html = response.read()
sIndex = html.find("<title>")
eIndex = html.find("</title>")
title = html[sIndex+7:eIndex]
#variable response uses urllib to access the internet for the history
#sIndex and eIndex find the first and 2nd <title> tags. the sIndex (first tag) is found from the first character so the +7 skips the search to the end of the title tag (+ 7 characters)

api = twitter.Api(creds[0], creds[1], creds[2], creds[3])
#loading in the list of my twitter credentials

response = api.PostUpdate("I've just viewed " + str(title) + " " + str(cHistoryURL))
#posting update of "ive just viewed", the variable "title" and variable cHistoryURL to my twitter feed

