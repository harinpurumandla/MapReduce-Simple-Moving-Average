#!/usr/bin/env python
#Author : Harin Purumandla 
import sys
from collections import deque #importing queue data structure
if len(sys.argv) == 2: # check if command line arguments are provided
    window = int(sys.argv[1]) #store the argument in the window variable
else :
    window = 3 # if arguments are not provided window is initialised to 3
prevcompany = None #variable to store the previous company name
queue = deque() # declare dequeue
smm = 0.0 #moving average 
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from SMMapper.py
    key, value = line.split('\t')
    company, date = key.split('|') # split the key into company and date
    if prevcompany == company: # if the company from the Mapper equals to the prevcompany
        queue.append(float(value)) # append the queue with the value from the mapper
    else: # if the company from the Mapper is not equal to the prevcompany
        prevcompany = company 
        queue.clear() #clear the queue
        queue.append(float(value)) # append the queue with the value from the mapper 
    if len(queue) >= window:
        smm = 0.0
	#for all the values in queue
        for val in queue: 
            smm += float(val) # add the values of the queue to smm
        print '%s, %s, %s' % (company, date, smm)  # print the SMM as required
        queue.popleft() # pop the value from the left (header of the queue)
