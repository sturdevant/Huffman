Note: All .ipynb files are primarily for testing phase, final versions will be .py files that can accept commandline arguments

fetchLyrics.py: fetches lyrics from all songs written by given artist from lyrics.com, outputs them into a csv formatted file
	cmdln args: "-a" for artist name & "-f" for output file name

buildDictionary.py: builds a list of all the words in files w/ ".lyrics" extension
buildEncoding.py: builds a Huffman encoding dictionary from specified word list file & .lyric file
encodeFile.py: encodes file given encoding dictionary & input file
decodeFile.py: decodes encoded file, given encoding dictionary & input encoded file

