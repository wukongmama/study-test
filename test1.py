import sys
import re

r = r'(<img\s+src=")(\S){2}(\S+)(")'
for line in sys.stdin:
    searchobj=re.search(r,line)
    if not searchobj:
        continue
    print(searchobj.group(3))