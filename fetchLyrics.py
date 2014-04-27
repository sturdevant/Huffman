import urllib2
from bs4 import BeautifulSoup
from optparse import OptionParser

class song(object):
    def __init__(self, url):
        # Fetch lyrics from given url
        self.url = url
        page = urllib2.urlopen(url).read()
        soup = BeautifulSoup(page)
        result = soup.find("div", {"id" : "lyric_space"})
        text = result.getText()
        print "Fetching lyrics from: " + url
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

class artist(object):
    def __init__(self, name):
        # Get all songs from artist's page
	base = "http://www.lyrics.com"
        page = urllib2.urlopen(base + "/" + name).read()
        soup = BeautifulSoup(page)
        songList = soup.find("div", {"id" : "songlist"}).findAll("a")
        songs = []
        for result in songList:
            # Ignore the "add song" link
            if result.text != "+":
                songs.append(song(base+result.get("href")))
        
        # Combine all their lyrics into one string 
	#(of songs which have lyrics...)
        allLyrics = ""
        for s in songs:
            if s.hasLyrics:
                allLyrics += s.lyrics.lower()
        
        # Clean up string by stripping punctuation
	#(maybe not so rubust since something like "s.s" wouldn't get 
	#fully stripped...)
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

# Get artist & output file name from commandline
parser = OptionParser()
parser.add_option("-n", "--artist", dest="artistName", help="Name of artist whose lyrics you want to fetch")
parser.add_option("-o", "--out", dest="outFile", help="Destination file for artist's lyrics")
(options, args) = parser.parse_args()
artist(options.artistName).writeFile(options.outFile)
