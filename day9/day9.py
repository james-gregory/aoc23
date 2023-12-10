# nice taylor series
# could also get the eqn of the polynomial and plug in N+1 and -1 to get a) and b)?
def a():
    total = 0
    with open("input.txt") as f:
        for line in f:
            s = [int(i) for i in line.split()]
            f = s[-1]
            while sum(s) != 0 or max(s) != 0:
                new = []
                for i in range(len(s) - 1):
                    new.append(s[i+1] - s[i])
                s = new
                f += s[-1]
            total += f
    return total
                
def b():
    total = 0
    with open("input.txt") as f:
        for line in f:
            s = [int(i) for i in line.split()]
            f = [s[0]]
            while sum(s) != 0 or max(s) != 0:
                new = []
                for i in range(len(s) - 1):
                    new.append(s[i+1] - s[i])
                s = new
                f.append(s[0])
 
            g = [0]
            i = 0
            while len(g) < len(f):
                g.append(f[len(f) - (i + 2)] - g[i])
                i += 1
            total += g[-1]
    return total

print(a())
print(b())