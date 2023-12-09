
def day1():
    total = 0
    with open("input.txt") as f:
        for line in f:
            # find and replace substrings
            digits = [int(s) for s in line if s.isdigit()]
            if len(digits) == 0:
                continue
            total += 10*digits[0] + digits[-1]
    return total

# horrid :)
def findReplace(line):
    line = line.replace("one", "one1one")
    line = line.replace("two", "two2two")
    line = line.replace("three", "three3three")
    line = line.replace("four", "four4four")
    line = line.replace("five", "five5five")
    line = line.replace("six", "six6six")
    line = line.replace("seven", "seven7seven")
    line = line.replace("eight", "eight8eight")
    line = line.replace("nine", "nine9nine")
    return line 

def day1_2():
    total = 0
    with open("input.txt") as f:
        for line in f:
            print(line)
            line = findReplace(line)
            print(line)
            digits = [int(s) for s in line if s.isdigit()]
            print(10*digits[0] + digits[-1])
            if len(digits) == 0:
                continue
            total += 10*digits[0] + digits[-1]
    return total

print(day1())
print(day1_2())