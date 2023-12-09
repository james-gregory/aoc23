import re

def a():
    with open("input.txt") as f:
        total = 0
        idx = 0
        prev = ""
        current = ""
        next = ""
        lines = f.readlines()
        while idx < len(lines) + 2:
            for match in re.finditer("[0-9]+", current):
                for row in [prev, current, next]:
                    if bool(re.search("[^0-9\.]", row[max(match.span()[0] - 1, 0) : min(match.span()[-1] + 1, len(row) - 1)])):
                        total += int(match.group())
                        break

            prev = current
            current = next
            if idx < len(lines):
                next = lines[idx]
            else:
                next = ""
            idx += 1

        return total

print(a())

def b():
    with open("input.txt") as f:
        total = 0
        idx = 0
        prev = ""
        current = ""
        next = ""
        m = {}
        lines = f.readlines()
        # gross
        while idx < len(lines) + 2:
            for match in re.finditer("[0-9]+", current):
                for count, row in enumerate([prev, current, next]):
                    start = max(match.span()[0] - 1, 0)
                    end = min(match.span()[-1] + 1, len(row) - 1)
                    for starmatch in re.finditer("[\*]", row[start:end]):
                        starpos = start + (idx - 4 + count) * len(current) + starmatch.span()[0]
                        print(match.group())
                        print("pos of star:" + str(starpos))
                        if starpos not in m:
                            m[starpos] = [match.group()]
                        else:
                            m[starpos].append(match.group())
                        print(m[starpos])
                        break

            print("\n")
            prev = current
            current = next
            if idx < len(lines):
                next = lines[idx]
            else:
                next = ""
            idx += 1

        for star in m:
            if len(m[star]) == 2:
                total += int(m[star][0])*int(m[star][1])
        return total
    
print(b())