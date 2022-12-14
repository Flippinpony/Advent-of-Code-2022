def make_map(in_rocks, add_floor):
    depth = 0
    with open("input/day14input.txt") as file:
        for line in file:
            # getting spicier with list comprehension
            points = [(int(x.split(',')[0]),int(x.split(',')[1])) for x in line.strip().split(' -> ')]
            start = points.pop(0)
            while points:
                end = points.pop(0)
                if start[0] == end[0]:
                    # vert line
                    a, b = start[1], end[1]
                    if(a > b): a, b = b, a
                    for n in range(a,b+1):
                        in_rocks.add((start[0],n))
                        if n > depth:
                            depth = n
                elif start[1] == end[1]:
                    # horizontal line
                    a, b = start[0], end[0]
                    if(a > b): a, b = b, a
                    for n in range(a,b+1):
                        in_rocks.add((n,start[1]))
                        if start[1] > depth:
                            depth = start[1]
                else:
                    print("Malformed coordinates")
                start = end
        if add_floor:
            # create long horizontal line for pt 2
            depth += 2
            for n in range(0,1000):
                in_rocks.add((n,depth))
    return depth

def simulate_sand(in_rocks, in_depth):
    sand_count = 0
    while True:
        sand_count += 1
        sand_pos = (500,0)
        while sand_pos[1] < in_depth:
            if (sand_pos[0],sand_pos[1]+1) not in in_rocks:
                # move down
                sand_pos = (sand_pos[0],sand_pos[1]+1)
            elif (sand_pos[0]-1,sand_pos[1]+1) not in in_rocks:
                # move down-left
                sand_pos = (sand_pos[0]-1,sand_pos[1]+1)
            elif (sand_pos[0]+1,sand_pos[1]+1) not in in_rocks:
                # move down-right
                sand_pos = (sand_pos[0]+1,sand_pos[1]+1)
            else:
                # come to rest
                in_rocks.add(sand_pos)
                break
        # check if sand passed max depth
        if sand_pos[1] == in_depth:
            sand_count -= 1
            break
        # check if sand clogged hole
        elif sand_pos == (500,0):
            break
    return sand_count

# driver
rocks = set()
max_depth = make_map(rocks, False)
sand = simulate_sand(rocks, max_depth)
print("Part 1 answer: " + str(sand))

rocks_2 = set()
max_depth_2 = make_map(rocks_2, True)
sand_with_floor = simulate_sand(rocks_2, max_depth_2)
print("Part 2 answer: " + str(sand_with_floor))