#! /usr/bin/env python3
"""Here, a histogram of NY zipcodes and the number of graffit complaints they've recieved are listed. The input_file contains all 311 calls for graffiti in NYC. A tally dictionary is then made with zipcode (of a given complaint) as they key and the number of occurences as value."""

from collections import defaultdict
global tally

# file containing all the graffiti calls from the 311 data
input_file = "./311_graffiti"
f = open(input_file)
line = f.readline()
tally = defaultdict(int)
# 7th field is the zipcode of the 311 incident

while line:
    fields = line.split('\t')
    zipcode = fields[8] 
    if zipcode:
        tally[zipcode]+=1
    line = f.readline()
f.close()

# write the sorted list of zipcodes and the number of graffiti complaints they've had to a new file
output = open("graffiti_zips_hist",'w')
    
for key,value in sorted(tally.items()):
    print(key,value,file = output)
output.close()
    

    



