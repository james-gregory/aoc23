import re
import math

def create_map(file):
    m = {}
    with open(file) as f:
        for line in f:
            s = re.findall("\w+", line)
            m[s[0]] = {'L': s[1], 'R': s[2]}

    return m

def a():
    s = "AAA"
    m = create_map("input.txt")
    path = "LRLRLLRLRLRRLRLRLRRLRLRLLRRLRRLRLRLRLLRRRLRRRLLRRLRLRLRRRLRRLRRRLRLRLRRLRLLRLRLRRLRRRLRLRRLRRRLLRLRLRRRLRRRLRLRRRLRLRRRLLRRLLLRRRLLRRRLRRRLRRRLRLRLRLLRLRRLRLRLLLRRLRRLRRLRLRRLRRLLRRLRLRRRLRLRLLRRRLRRRLRRRLLLRRRLRLRLRRLRRRLRRRLRLRRRLRRLRRRLRLRRLLRRRLRRRLLLRRLRLRLRRLRRRLRRLRRLRLRRRR"
    i = 0
    count = 0
    while s != "ZZZ":
        s = m[s][path[i]]
        count += 1
        if i == len(path) - 1:
            i = 0
        else:
            i += 1
    return count

print(a())


def b():
    m = create_map("input.txt")
    s = []
    for k in m:
        if k[-1] == 'A':
            s.append(k)

    path = "LRLRLLRLRLRRLRLRLRRLRLRLLRRLRRLRLRLRLLRRRLRRRLLRRLRLRLRRRLRRLRRRLRLRLRRLRLLRLRLRRLRRRLRLRRLRRRLLRLRLRRRLRRRLRLRRRLRLRRRLLRRLLLRRRLLRRRLRRRLRRRLRLRLRLLRLRRLRLRLLLRRLRRLRRLRLRRLRRLLRRLRLRRRLRLRLLRRRLRRRLRRRLLLRRRLRLRLRRLRRRLRRRLRLRRRLRRLRRRLRLRRLLRRRLRRRLLLRRLRLRLRRLRRRLRRLRRLRLRRRR"
    counts = []
    count = 0
    i = 0
    for j in range(len(s)):
        count = 0
        while s[j][-1] != 'Z':
            s[j] = m[s[j]][path[i]]
            count += 1
            i = (i + 1) % len(path)
        
        counts.append(count)

    return math.lcm(*counts)

print(b())
