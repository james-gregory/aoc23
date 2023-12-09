def a():
    total = 0
    with open("input.txt") as f:
        for line in f:
            line = line.split(":")[1].split("|")
            winning = line[0].split()
            numbers = line[1].split()
            print(winning)
            m = {}
            matches = 0
            for w in winning:
                if int(w) not in m:
                    m[int(w)] = True
            for n in numbers:
                if int(n) in m:
                    matches += 1
            if matches > 0:
                total += pow(2, matches-1)
        return total
    
print(a())

def b():
    extra = [1 for _ in open("input.txt")]
    idx = 0
    with open("input.txt") as f:
        for line in f:
            line = line.split(":")[1].split("|")
            winning = line[0].split()
            numbers = line[1].split()
            m = {}
            matches = 0
            for w in winning:
                if int(w) not in m:
                    m[int(w)] = True
            for n in numbers:
                if int(n) in m:
                    matches += 1
            for i in range(matches):
                if idx + i + 1 < len(extra):
                    print("hello")
                    print(extra[idx])
                    extra[idx + i + 1] += extra[idx]

            idx += 1

        return sum(extra)
    
print(b())