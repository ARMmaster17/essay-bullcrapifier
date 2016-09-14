#!/usr/bin/python

import sys
from PyDictionary import PyDictionary
dictionary=PyDictionary()

print "Starting up."
filepath = sys.argv[1]
file = open(filepath, "r")
print "Opened file " + file.name
outfile = open("output.txt", "w+")
print "Reading file"
lines = file.readlines()
for line in lines:
    words = line.split()
    for word in words:
        newword = ""
        newwords = dictionary.synonym(word)
        if newwords is None:
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
file.close()
outfile.close()