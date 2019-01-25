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