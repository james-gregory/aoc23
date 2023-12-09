import math

def quad(inputs):
    total = 1
    for input in inputs:
        x1 = 0.5*(input[0] + math.sqrt(input[0]*input[0] - 4*input[1]))
        x2 = 0.5*(input[0] - math.sqrt(input[0]*input[0] - 4*input[1]))
        total *= 1 + math.floor(x1) - math.ceil(x2)
    return total

print(quad([[55, 401], [99, 1485], [97, 2274], [93, 1405]]))
print(quad([[55999793, 401148522741405]]))