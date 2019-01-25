import sys

for line in sys.stdin:
    if 'a' in line:
        print(line)
    if 'A' in line:
        print(line)
