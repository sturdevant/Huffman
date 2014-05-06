#!/usr/bin/env python
from optparse import OptionParser

# Read cmdln args
parser = OptionParser()
parser.add_option("-o", "--out", dest="oFileName", help="Name of output file")
parser.add_option("-e", "--encoding", dest="eFileName", help="Name of encoding file")
parser.add_option("-i", "--input", dest="iFileName", help="Name of input file")

(options, args) = parser.parse_args()


# In[119]:

eFileName = options.eFileName
iFileName = options.iFileName
oFileName = options.oFileName


# In[120]:

# Open Files
eFile = open(eFileName, 'r')
iFile = open(iFileName, 'r')
oFile = open(oFileName, 'wb')


# In[121]:

# Build Reverse dictionary from encoding file
d = {}
for s in eFile.read().split(","):
    e = s.split(":")
    d[e[1]] = e[0]


# In[123]:

# Decoding (not quite as easy as encoding, can't split by comma!)
fstr = ""
temp = ""
for c in iFile.read():
    temp += c
    try:
        fstr += d[temp] +","
        temp = ""
    except:
        temp +=""# do nothing, need some statement here though...

oFile.write(fstr)

