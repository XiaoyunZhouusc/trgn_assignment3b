import re 
import sys

file = str(sys.argv[1])
mobile_list=[]
with open(file) as f:
    for line in f:
        for groups in re.findall("[+]{0,1}[0-9]{2,3}-[0-9]{2,4}-[0-9]*[-]{0,1}[0-9]*", line):
            isFirst = True
            ans=""
            for g in groups.split("-"):
                if isFirst and g[0] == "+":
                    ans = g
                    continue
                if isFirst:
                    ans += "("+g+")"
                    isFirst = False
                    continue
                ans+=g
            mobile_list.append(ans)

for pnum in mobile_list:
    print(pnum)
