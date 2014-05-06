#!/usr/bin/env python
# Read cmdln args
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-o", "--orig", dest="origFileName", help="Name of original file")
parser.add_option("-d", "--deco", dest="decoFileName", help="Name of decoded file")

(options, args) = parser.parse_args()

origFileName = options.origFileName
decoFileName = options.decoFileName


# In[73]:

origFile = open(origFileName)
decoFile = open(decoFileName)


# In[75]:

oList = origFile.read().split(",")
dList = decoFile.read().split(",")
for o, d in zip(oList, dList):
    if o != d:
        print "O", o, "D", d


# In[66]:

origFile.close()
decoFile.close()


# In[ ]:



