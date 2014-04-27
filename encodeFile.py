
# coding: utf-8

# In[ ]:

from optparse import OptionParser

# Read cmdln args
parser = OptionParser()
parser.add_option("-o", "--out", dest="oFileName", help="Name of output file")
parser.add_option("-e", "--encoding", dest="eFileName", help="Name of encoding file")
parser.add_option("-i", "--input", dest="iFileName", help="Name of input file")

(options, args) = parser.parse_args()


# In[67]:

eFileName = options.eFileName
iFileName = options.iFileName
oFileName = options.oFileName


# In[68]:

# Open Files
eFile = open(eFileName, 'r')
iFile = open(iFileName, 'r')
oFile = open(oFileName, 'wb')


# In[69]:

# Reconstruct encoding from file
d = {}
for s in eFile.read().split(","):
    e = s.split(":")
    d[e[0]] = e[1]


# In[70]:

# Encoding (unique prefixes, no need for csv)
fstr = ""
for s in iFile.read().split(","):
    fstr += d[s]
oFile.write(fstr)


# In[71]:

eFile.close()
iFile.close()
oFile.close()

