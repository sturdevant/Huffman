#!/usr/bin/env python
from optparse import OptionParser

# Read cmdln args
parser = OptionParser()
parser.add_option("-o", "--out", dest="outFileName", help="Name of output file")
(options, args) = parser.parse_args()


# In[1]:

outFileName = options.outFileName
inFileName = args


# In[100]:

# Using set to avoid multiple entries of same word
s = frozenset()
for fileName in inFileName:
    f = open(fileName, 'r')
    s = s.union(f.read().split(","))
    f.close()


# In[101]:

# Write set to file, in csv format
fstr = ""
for e in s:
    fstr += e + ","
fstr = fstr.strip(",")
f = open(outFileName, 'wb')
f.write(fstr)
f.close()

