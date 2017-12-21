#!/usr/bin/python

# Q3: most popular

import sys

maxHits = 0
conHits = 0
maxPath = None
oldPath = None

for line in sys.stdin:
    thisPath = line.strip().split()
    if len(thisPath) != 1:
        continue

    if oldPath and oldPath != thisPath:
        if maxHits < conHits: 
            maxHits = conHits
            maxPath = oldPath

        conHits = 0

    oldPath = thisPath
    conHits += 1

if maxPath != None:
    print maxPath, "\t", maxHits
