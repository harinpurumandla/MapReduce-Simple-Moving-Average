#!/usr/bin/env python
#Author : Harin Purumandla 
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    #concatenate company with date as make it a key
    key = line.split(",")[0]+"|"+line.split(",")[1]
    price = line.split(",")[2]
    print('%s\t%s' % (key, price)) # return the key value pair
