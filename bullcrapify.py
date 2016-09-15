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
for line in lines:
    words = line.split()
    for word in words:
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
    outfile.write("\n")
print "I:Cleaning up"
file.close()
outfile.close()