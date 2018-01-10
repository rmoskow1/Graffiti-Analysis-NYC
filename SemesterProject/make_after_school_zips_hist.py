
""" For the after school activites data set, a zipcode field and a location field exist. However, more often, the location field will be used while zipcode is left empty. Better results come from using the location field.
The way the data is stored, newlines exist within the location field; for every location field, zipcode is before and after a newline. Instead of changing the data to make the RS consistent, and then parsing through the location field, the following regex is effective. Any newline containing only 5 numbers is always the zipcode of a location field, and only one exists per record (or there's simply no location listed) 
The following code tallies the zipcodes found, thus giving the number of available after school activities per NYC zipcode"""

import re
from collections import defaultdict
global tally
# file containing all after school activity data in NY
input = "after_school"
# output file to store histogram
output = open('after_school_zips_hist','w')

# use a defaultdict to keep track of how many times each zip code occured
tally = defaultdict(int)
f = open(input)
zip_pattern = re.compile(r'^([0-9]{5})$') # parse all of the zipcodes. It's known to be a zipcode if there's 5 numbers independantly on a line
line = f.readline()
while line:
    if re.match(zip_pattern,line) is not None:
        tally[line.strip()]+=1
    line = f.readline()

# close input file
f.close()

# generate the histogram by printing zip key and count value to the output file
for key,value in sorted(tally.items()):
    print(key,value,file = output)

# close output file
output.close()



    


    
