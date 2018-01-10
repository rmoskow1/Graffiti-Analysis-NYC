#! /usr/bin/env python3

import matplotlib.pyplot as plt

# create list of zips and populations from zipcode population file
population_zips = "./population_zips_hist"
f = open(population_zips)
line = f.readline()
zips = {}
while line:
    fields = line.split()
    # each zips entry will be key: zipcode, value: estimated population
    zips[int(fields[0])] = int(fields[1])
    line = f.readline()
f.close()
# zips now contains each NYC zipcode and it's population


# create list of zips and count of after school activities from after school historgram file
after_school_zips = "./after_school_zips_hist"
f = open(after_school_zips)
line = f.readline()
after_schools = {}
while line:
    fields = line.split()
    after_schools[int(fields[0])] = int(fields[1])
    line = f.readline()
f.close()
# after_schools now contains NYC zip codes and their number of after school activities available

# create list of zipcodes and number of graffiti calls from graffiti calls histogram file
graffiti_zips = "./graffiti_zips_hist"
f = open(graffiti_zips)
line = f.readline()
graffiti = {}
while line:
    fields = line.split()
    graffiti[int(fields[0])] = int(fields[1])
    line = f.readline()
f.close()
# graffiti now contains NYC zips codes and their number of graffiti call complaints made

# normalize data for graffiti before plotting
# each normalized graffiti entry will be the graffiti count divided by the population of that zipcode
norm_graffiti = {}
for zipc in graffiti:
    # if the population count for the region is not 0 (several of these exist, due to changes in the US census. None of the zip regions with populations of 0 have after school entries either. These are removed from the normalized list)
    pop_count = zips[zipc]
    if pop_count !=0:
        norm_graffiti[zipc] = graffiti[zipc]/pop_count*100

# first plot the normalized graffiti
fig1 = plt.figure(1)
keys = list(norm_graffiti.keys())

x = [] # will be the school_zips count = independant
y = [] # will be the graffiti_zips count = dependant
for each in keys:
    x.append(after_schools[each]) if each in after_schools else x.append(0)
    y.append(norm_graffiti[each])

plt.scatter(x,y)
plt.title("Per NYC Zipcode: After-School Activities vs. Graffiti Complaints")
plt.xlabel("Total number of after school activites available")
plt.ylabel("Normalized number of graffiti complaints, %")
fig1.savefig("norm_count_comparison.pdf")

fig2 = plt.figure(1)
# This plot will be of the after-school activities compared to the total number of graffiti complaints. This is the equivalent of "normalizing" the number of available art activities per region
y2 = []

# y2 will now be the regular graffiti, total number.
# the same x array, the number of after school activities, can be used
for each in keys:
    y2.append(graffiti[each])
plt.scatter(x,y2, c = 'r')
plt.title("Per NYC Zipcode:Total After-School Activities vs. Total Number of Graffiti Complaints")
plt.xlabel("Number of after school activities available")
plt.ylabel("Total number of graffiti complaints")
plt.savefig("total_count_comparison.pdf")




