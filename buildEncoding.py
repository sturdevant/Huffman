#!/usr/bin/env python
import heapq as hp
from optparse import OptionParser

# Read cmdln args
parser = OptionParser()
parser.add_option("-o", "--out", dest="oFileName", help="Name of output file")
parser.add_option("-d", "--dict", dest="dFileName", help="Name of dictionary file")
parser.add_option("-i", "--input", dest="aFileName", help="Name of input file")

(options, args) = parser.parse_args()


# In[379]:

class node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    # Print out tree, not a nice format, but you can at least reconstruct it...
    def printNode(self, level = 0):
        if (self.left != None):
            self.left.printNode(level + 1)
        if (self.value != None):
            print str(self.value) + ":  level: " + str(level)
        if (self.right != None):
            self.right.printNode(level + 1)
    
    # Encode recursively, left branch prefixed w/ "0", right branch w/ "1"
    def encode(self):
        if (self.left == None):
            if (self.right == None):
                return {self.value : ""}
            else:
                d = self.right.encode()
                for e in d:
                    d[e] = "1" + d[e]
                return d
        else:
            dl = self.left.encode()
            dr = {}
            if (self.right != None):
                dr = self.right.encode()
            for e in dl:
                dl[e] = "0" + dl[e]
            for e in dr:
                dr[e] = "1" + dr[e]
            # return left & right dictionaries
            return dict(dl, **dr)
            


# In[380]:

# File names from commandline args
dFileName = options.dFileName
aFileName = options.aFileName
oFileName = options.oFileName


# In[381]:

# Open files
dFile = open(dFileName, 'r')
aFile = open(aFileName, 'r')
oFile = open(oFileName, 'wb')


# In[382]:

# Initialize dictionary from file
d = {}
for s in dFile.read().split(','):
    d[s] = 1

# Fill entries from aFile, adding 1 to them everytime the word is run into
for s in aFile.read().split(','):
    try:
        d[s] += 1
        print s
    except:
        print aFileName

# In[383]:

# Initialize heap w/ leafnodes
h = []
for e in d:
    hp.heappush(h, (d[e], node(e)))


# In[384]:

# Build tree
while (len(h)>1):
    n, small = hp.heappop(h)
    N, big = hp.heappop(h)
    new = node(n+N, big, small)
    hp.heappush(h, (n+N, new))


# In[385]:

# Build encoding dictionary from root node & save in oFile
fstr = ""
v, root = h[0]
d = root.encode()
for e in d:
    fstr += e + ":" + d[e] + ","
fstr = fstr.strip(",")
oFile.write(fstr)


# In[386]:

# Close all files
dFile.close()
aFile.close()
oFile.close()

