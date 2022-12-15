import re, math

def manhattan(a, b):
    return sum(abs(x-y) for x, y in zip(a,b))

def get_beacon_pairs(pairs):
    with open("input/day15input.txt") as file:
        for line in file:
            pairs.append([int(n) for n in re.findall(r'-?\d+', line)])

def get_exclusions(pairs, line):
    exclusion_set = set()
    beacons_in_target_line = set()
    for pair in pairs:
        sensor, beacon = (pair[0],pair[1]), (pair[2],pair[3])
        if beacon[1] == line:
            beacons_in_target_line.add(beacon[0])
        reach = manhattan(sensor, beacon)
        start = reach - abs(line - sensor[1])
        for x in range(sensor[0] - start, sensor[0] + start + 1):
            if x not in beacons_in_target_line:
                exclusion_set.add(x) 
    return exclusion_set

def find_signal(coords, pairs):
    dist_sensor_pair = set()
    for pair in pairs:
        sensor, beacon = (pair[0],pair[1]), (pair[2],pair[3])
        dist = manhattan(sensor,beacon)
        dist_sensor_pair.add((dist, sensor))
    index = 0
    for coord in coords.copy():
        index += 1
        for dist_pair in dist_sensor_pair:
            if dist_pair[0] >= manhattan(dist_pair[1],coord): # coord found
                coords.remove(coord)
                break
    print(f"Remaining coords: {len(coords)}")
    return coords.pop()


def get_exclusions_2d(pairs, min_coord, max_coord):
    candidates = set()
    for pair in pairs:
        sensor, beacon = (pair[0],pair[1]), (pair[2],pair[3])
        reach = manhattan(sensor, beacon)
        for x in range(max(sensor[0] - reach,min_coord),min(sensor[0] + reach,max_coord) + 2):
            y = reach - abs(sensor[0] - x) + 1
            if sensor[1]+y < max_coord:
                candidates.add((x, sensor[1]+y))
            if sensor[1]-y > min_coord:
                candidates.add((x, sensor[1]-y))
    signal = find_signal(candidates, pairs)
    return signal


# driver
target_line = 2000000
pairs = []
get_beacon_pairs(pairs)
exclusion_set = get_exclusions(pairs, target_line)
print(f"Part 1 answer: {len(exclusion_set)}")

# part 2 (this took like ten minutes to run but I'm tired so ship it)
min_coord = 0
max_coord = 4000000
distress_coord = get_exclusions_2d(pairs, min_coord, max_coord)
print(distress_coord)
tuning_freq = (distress_coord[0] * max_coord) + distress_coord[1]
print(f"Part 2 answer: {tuning_freq}")