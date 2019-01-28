'''
import sys

size = 0

def get_size(word):
    v1 = float (word [:-1])
    if word [-1] == "B":
        return v1
    elif word [-1] == "K":
        return v1 * 1024
    elif word [-1] == "G":
        return v1 * 1024 * 1024
    else:
        return v1 * 1024* 1024 * 1024

for line in sys.stdin:
    print(line)
    sp = line.split()
    print(sp)
    if len(sp) < 5:
        continue
    word = sp[4]
    v1 = get_size(word)
    print(v1)
    size = size + v1
    print(size)
'''

'''
import sys
import re

sum=0
r = r'(\S+\s+){4}(\S+)'

for line in sys.stdin:
    searchobj = re.search (r,line)
    if not searchobj:
        continue
    size = searchobj.group(2)
    num = float (size [:-1])
    if size [-1] == "B":
        sum = sum + num
    elif size [-1] == "K":
        sum = sum +num * 1024
    elif size [-1] == "G":
        sum = sum + num * 1024 * 1024
    else:
        sum = sum + num* 1024* 1024 * 1024

print(sum)
'''

import sys
import re

sum=0
r = r'(\S+\s+){4}(\S+)'
dict = {'B':1, 'K':1024,'G':1048576,'T':1073742e9}

for line in sys.stdin:
    searchobj = re.search (r,line)
    if not searchobj:
        continue
    size = searchobj.group(2)
    num = float (size [:-1])
    unit = dict.get(size [-1])  # a unit, or None
    if unit:
        sum = sum + num * unit

print(sum)