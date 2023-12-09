import re

def a():
    with open("input.txt") as f:
        total = 0
        idx = 0
        for line in f:
            idx += 1
            greens = re.findall("([0-9]+)\sgreen", line)
            greens = [int(g) for g in greens]
            if max(greens) > 13:
                continue
            blues = re.findall("([0-9]+)\sblue", line)
            blues = [int(b) for b in blues]
            if max(blues) > 14:
                continue
            reds = re.findall("([0-9]+)\sred", line)
            reds = [int(r) for r in reds]
            if max(reds) > 12:
                continue
            total += idx
        return total
            
            

print(a())

def b():
    with open("input.txt") as f:
        total = 0
        for line in f:
            power = 1
            greens = re.findall("([0-9]+)\sgreen", line)
            greens = [int(g) for g in greens]
            if max(greens) > 0:
                power *= max(greens)
            blues = re.findall("([0-9]+)\sblue", line)
            blues = [int(b) for b in blues]
            if max(blues) > 0:
                power *= max(blues)
            reds = re.findall("([0-9]+)\sred", line)
            reds = [int(r) for r in reds]
            if max(reds) > 0:
                power *= max(reds)
            total += power
        return total
    
print(b())

