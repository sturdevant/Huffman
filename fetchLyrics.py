#!/usr/bin/env python
import urllib2
from bs4 import BeautifulSoup
from optparse import OptionParser

# Read cmdln args
parser = OptionParser()
parser.add_option("-i", "--in", dest="artistName", help="Name of artist")
parser.add_option("-o", "--out", dest="outFileName", help="Name of output file")
(options, args) = parser.parse_args()


# In[221]:

class song(object):
    def __init__(self, url):
        # Fetch lyrics from given url
        page = urllib2.urlopen(url).read()
	print "fetching lyrics from " + url
        soup = BeautifulSoup(page)
        # make sure url exists
        try:
           result = soup.find("div", {"id" : "lyric_space"})
           text = result.getText()
        except:
           print "failed on: " + url
           self.hasLyrics = False
           return
        
        # Try-except ensures that the song has lyrics
        try:
            for i in range(len(text)):
                # Detect end of lyrics
                if (text[i] == "-") & (text[i+1] == "-") & (text[i+2] == "-"):
                    bad_end = i
                    break
            self.lyrics = text[:i]
            self.hasLyrics = True
        except:
            self.hasLyrics = False


# In[246]:

class artist(object):
    def __init__(self, name):
        # Get all songs from artist's page
        page = urllib2.urlopen("http://www.lyrics.com/" + name).read()
	print "fetching lyrics from " + "http://www.lyrics.com/" + name
        soup = BeautifulSoup(page)
        songList = soup.find("div", {"id" : "songlist"}).findAll("a")
        songs = []
        for result in songList:
            # Ignore the "add song" link
            if result.text != "+":
               songs.append(song("http://www.lyrics.com"+result.get("href")))
        # Combine all their lyrics into one string (of songs which have lyrics...)
        allLyrics = ""
        for s in songs:
            if s.hasLyrics:
                allLyrics += s.lyrics.lower()
        
        # Clean up string by stripping punctuation (maybe not so rubust since something like ",." wouldn't get fully stripped...)
        self.words = []
        for s in allLyrics.split():
            self.words.append(s.strip(".").strip(",").strip("!").strip("\"").strip("?").strip(":").strip(";").strip("(").strip(")").strip("'"))
        
    
    # Write lyrics into a csv file
    def writeFile(self, fileName):
        fstr = ""
        for s in self.words:
            fstr += s + ","
        fstr = fstr.rstrip(",")
        f = open(fileName, 'wb')
        f.write(fstr.encode('utf-8'))
        f.close()


# In[247]:

artist(options.artistName).writeFile(options.outFileName)

