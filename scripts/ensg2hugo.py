import re
import sys

homo = "Homo_sapiens.GRCh37.75.gtf"
inputFile = str(sys.argv[1])
col = 1

if inputFile[:2] == "-f":
    col = int(inputFile[-1])
    inputFile = str(sys.argv[2])

ensg2hugo = {}

with open(homo) as f:
    for line in f:
        for myMatch in re.findall("gene_id\s\"(\S+)\".*gene_name\s\"(\S+)\"", line):
            ensg2hugo[myMatch[0]] = myMatch[1]

with open(inputFile) as f:
    isFirst = True
    for line in f:
        if not isFirst:
            original = re.findall("([^,]+),", line)[col - 1]
            original = re.findall("[^\"\s]+", original)[0]
            toSub = re.findall("[^\.]+", original)[0]
            
            # Don't use re.sub() but use this instead, because in case if a row has more than one columns contain Ensembl name we don't want to replace columns other than what user specified. 
            splitted = line.split(",")
            splitted[col - 1] = splitted[col - 1].replace(original, ensg2hugo.get(toSub, original))
            line = ",".join(splitted)
        print(line)
        isFirst = False
