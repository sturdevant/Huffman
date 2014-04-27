
# coding: utf-8

# In[98]:

import glob
from optparse import OptionParser

# Read cmdln args
parser = OptionParser()
parser.add_option("-o", "--out", dest="outFileName", help="Name of output file")
(options, args) = parser.parse_args()


# In[99]:

outFileName = options.outFileName


# In[100]:

# Using set to avoid multiple entries of same word
s = frozenset()
for fileName in glob.glob("*.lyrics"):
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


# In[ ]:



