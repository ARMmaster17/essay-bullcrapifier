#!/usr/bin/python

import sys
import os
from PyDictionary import PyDictionary
dictionary=PyDictionary()

print "I:Starting up."
print "I:Loading blacklist"
fileblacklist = open("blacklist.txt", "r")
blacklist = []
for item in fileblacklist.readlines():
    blacklist.append(item.replace("\n", ""))
fileblacklist.close()
if os.path.isfile("output.txt"):
    print "W:Existing output file found."
    os.remove("output.txt")
filepath = sys.argv[1]
file = open(filepath, "r")
print "I:Opened file " + file.name
outfile = open("output.txt", "w+")
print "I:Reading file"
lines = file.readlines()
linecounter = 1
linemax = len(lines)
for line in lines:
    print linecounter, "/", linemax, " ", round((float(linecounter)/float(linemax)) * 100, 1), "%"
    words = line.split()
    wordcounter = 1
    wordmax = len(words)
    for word in words:
        print "\t", wordcounter, "/", wordmax, " ", round((float(wordcounter)/float(wordmax)) * 100, 1), "%"
        newword = ""
        newwords = dictionary.synonym(word)
        if word.lower() in blacklist or newwords is None:
            newword = word
        else:
            for nword in newwords:
                if len(nword) > len(word):
                    newword = nword
                    break
            if newword == "":
                newword = word
        outfile.write(newword + " ")
        wordcounter += 1
    outfile.write("\n")
    linecounter += 1
print "I:Cleaning up"
file.close()
outfile.close()