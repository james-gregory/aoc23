import time

def mapping(file, source):
    with open(file) as f:
        for line in f:
            vals = line.split()
            if source >= int(vals[1]) and source < int(vals[1]) + int(vals[2]):
                return int(vals[0]) + (source - int(vals[1]))
        print("failed to convert during " + file)
        return source
    
def full_mapping(seed):
    soil = mapping("seed-soil.txt", seed)
    fert = mapping("soil-fertilizer.txt", soil)
    water = mapping("fertilizer-water.txt", fert)
    light = mapping("water-light.txt", water)
    temp = mapping("light-temp.txt", light)
    humidity = mapping("temp-humidity.txt", temp)
    return mapping("humidity-location.txt", humidity)

def a():
    with open("inputs.txt") as f:
        locations = []
        for line in f:
            seeds = line.split()

        for seed in seeds:
            locations.append(full_mapping(int(seed)))

        return min(locations)

# print(a())

def create_mapping(file):
    m = []
    with open(file) as f:
        for line in f:
            vals = line.split()
            m.append([int(vals[0]), int(vals[1]), int(vals[2])])

    
    def inner_mapping(source):
        for row in m:
            if source >= row[1] and source < row[1] + row[2]:
                return row[0] + (source - row[1])
        return source

    return inner_mapping

def import_data(file):
    m = []
    with open(file) as f:
        for line in f:
            vals = line.split()
            m.append([int(vals[0]), int(vals[1]), int(vals[2])])
    return m


# General method for part b) is to take an input region in the domain
# and split into multiple regions in the codomain. We map the lower bound
# then find the upper bound of that region, then track back to the domain
# and check if we are done. If not we add one, then map back to codomain
# and continue until we have large set of location regions which our initial
# seed range could map to. Then we take the smallest.

def forward_mapping(m, source):
    for row in m:
        if source >= row[1] and source < row[1] + row[2]:
            return [row[0], row[0] + row[2], row[0] + (source - row[1])]
 
    closest_start = 1e12
    closest_end = 0
    for row in m:
        if row[1] > source and row[1] < closest_start:
            closest_start = row[1]
        if row[1] + row[2] < source and row[1] + row[2] > closest_end:
            closest_end = row[1] + row[2]

    return [closest_end, closest_start, source]
    
def inverse_mapping(m, source):
    for row in m:
        if source >= row[0] and source < row[0] + row[2]:
            return [row[0], row[0] + row[2], row[1] + (source - row[0])] 

    closest_start = 1e12
    closest_end = 0
    for row in m:
        if row[1] > source and row[1] < closest_start:
            closest_start = row[1]
        if row[1] + row[2] < source and row[1] + row[2] > closest_end:
            closest_end = row[1] + row[2]

    return [closest_end, closest_start, source]


def split_region(m, a, b):
    start = a
    end = b
    bounds = []
    while 1:
        f = forward_mapping(m, start)
        i = inverse_mapping(m, f[1] - 1)   # map the end of the region back

        if i[2] >= end:
            bound = [f[2], forward_mapping(m, end)[2]]
            bounds.append(bound)
            return bounds
        else:
            bound = [f[2], f[1]]
            bounds.append(bound)

        start = i[2] + 1
    return bounds

def b(a, b):
    maps = [
        import_data("seed-soil.txt"),
        import_data("soil-fertilizer.txt"),
        import_data("fertilizer-water.txt"),
        import_data("water-light.txt"),
        import_data("light-temp.txt"),
        import_data("temp-humidity.txt"),
        import_data("humidity-location.txt")
    ]

    bounds = [[a, b]]
    i = 1
    for m in maps:
        # print("map " + str(i))
        new_bounds = []
        for bound in bounds:
            new_bounds += split_region(m, bound[0], bound[1])
        bounds = new_bounds
        i += 1
    
    min = bounds[0][0]
    for bound in bounds:
        if bound[0] < min:
            min = bound[0]

    return min

def bfull():
    with open("inputs.txt") as f:
        for line in f:
            seeds = line.split()

    min = 10e12
    i = 0
    while i < len(seeds) - 1:
        loc = b(int(seeds[i]), int(seeds[i]) + int(seeds[i+1]))
        if loc < min:
            min = loc
        i += 2
    
    return min

start = time.time()
print(bfull())
print(time.time() - start)
    