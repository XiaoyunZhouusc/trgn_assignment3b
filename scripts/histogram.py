import re
import sys
import numpy as np

from matplotlib import pyplot as plt

inputFile = str(sys.argv[1])
col = 2

data = []

if inputFile[:2] == "-f":
    col = int(inputFile[-1])
    inputFile = str(sys.argv[2])

with open(inputFile) as f:
    isFirst = True
    for line in f:
        if not isFirst:
            original = re.findall("(\S+)\s", line)[col - 1]
            original = re.findall("[^\"\s]+", original)[0]
            
            # Assume only have floats
            data.append(float(original))
        

        isFirst = False

# Creating dataset
dataSource = np.array(data)
 
# Creating histogram
fig, ax = plt.subplots() 
ax.hist(dataSource)
 
# Save fig
plt.savefig("histogram.png")
