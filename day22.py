import re

movement_mask = {
    0 : (1, 0), # right
    1 : (0, 1), # down
    2 : (-1, 0), # left
    3 : (0, -1), # up
}

def make_map():
    file = open("input/day22input.txt", "r")
    input = file.read().split('\n\n')
    map = {}
    path = re.findall('(\d+|[A-Za-z]+)', input[1])
    start = None
    for y, line in enumerate(input[0].splitlines(), start = 1):
        for x, char in enumerate(line, start=1):
            if char in '#.':
                if not start:
                    start = (x,y)
                map[x,y]=char
                
    
    return map, path, start

def get_wrapped_coord(map, coord, dir):
    # could probably be clever about this, but would rather just do it per-directoion for clarity
    new_coord = None
  
    match dir:
        case 0:
            # right
            x, y = 0, coord[1]
            while not new_coord:
                x += 1
                if (x,y) in map and map[(x,y)] != "":
                    new_coord = (x,y)
        case 1:
            # down
            x, y = coord[0], 0
            while not new_coord:
                y += 1
                if (x,y) in map and map[(x,y)] != "":
                    new_coord = (x,y)

        case 2:
            # left
            x, y = width + 1, coord[1]
            while not new_coord:
                x -= 1
                if (x,y) in map and map[(x,y)] != "":
                    new_coord = (x,y)
        case 3:
            # up
            x, y = coord[0], height + 1
            while not new_coord:
                y -= 1
                if (x,y) in map and map[(x,y)] != "":
                    new_coord = (x,y)
    return new_coord

def get_face(coord):
    x,y = 0,1
    if coord[x] <= 100 and coord[y] <= 50:
        return 0
    elif coord[x] > 100:
        return 1
    elif coord[y] > 50 and coord[y] <= 100:
        return 2
    elif coord[x] <= 50 and coord[y] <= 150:
        return 3
    elif coord[x] > 50 and coord[y] <= 150:
        return 4
    elif coord[y] > 150:
        return 5
    else:
        print(f"no face found, bad coordinate! {coord}")

def get_wrapped_coord_cube(pos, coord, dir):
    x,y = 0,1
    right, down, left, up = 0, 1, 2, 3
    new_facing = None
    new_coord = None
    face = get_face(pos)
    match face:
        case 0:
            if dir == left:
                new_facing = right
                new_coord = (1, 151 - coord[y])
            elif dir == up:
                new_facing = right
                new_coord = (1, 100 + coord[x])
        case 1:
            if dir == right:
                new_facing = left
                new_coord = (100, 151 - coord[y])
            elif dir == down:
                new_facing = left
                new_coord = (100, coord[x]-50)
            elif dir == up:
                new_facing = up
                new_coord = (coord[x]-100,200)
        case 2:
            if dir == right:
                new_facing = up
                new_coord = (50 + coord[y],50)
            elif dir == left:
                new_facing = down
                new_coord = (coord[y] - 50,101)
        case 3:
            if dir == left:
                new_facing = right
                new_coord = (51, 151-coord[y])
            elif dir == up:
                new_facing = right
                new_coord = (51, 50 + coord[x])
        case 4:
            if dir == right:
                new_facing = left
                new_coord = (150, 151-coord[y])
            elif dir == down:
                new_facing = left
                new_coord = (50, 100 + coord[x])
        case 5:
            if dir == right:
                new_facing = up
                new_coord = (coord[y] - 100,150)
            elif dir == down:
                new_facing = down
                new_coord = (100 + coord[x],1)
            elif dir == left:
                new_facing = down
                new_coord = (coord[y] - 100,1)
    if not new_coord:
        print(f" Issue detected at coordinate {coord} facing {dir}, leaving face {face}!")

    return new_coord, new_facing


def sim_path(map, path, start, part1):
    pos = start
    facing = 0
    target_facing = -1
    step_count = 0
    for step in path:
        step_count += 1
        if step.isdigit():
            count = int(step)
            for i in range(count):
                if pos == (17,105):
                    print("here")
                target = tuple(sum(n) for n in zip(pos, movement_mask[facing]))
                if target not in map or map[target] == "":
                    # need to loop
                    if part1:
                        target = get_wrapped_coord(map, target, facing)
                    else:
                        # print(f"Resolving move from {pos} to {target}")
                        target, target_facing = get_wrapped_coord_cube(pos, target, facing)
                if map[target] == ".":
                    # safe to move
                    #print(f"Moving to {target}")
                    print((pos[0],pos[1]))
                    pos = target
                    if target_facing >= 0:
                        facing = target_facing
                        target_facing = -1
                elif map[target] == "#":
                    # hit a wall
                    target_facing = -1
                    break
                else:
                    # invalid character?
                    print(f"Invalid character found.. {map[target]}")
        else:
            if step == 'R':
                facing = (facing + 1) % 4
            elif step == 'L':
                facing = (facing - 1) % 4
    return pos, facing


# driver
width, height = 150, 200
map, path, start = make_map()
#part1 = True
#pos, facing = sim_path(map, path, start, part1)
#print(f"Ended at {pos} facing direction {facing}")
#print(f"Part 1 answer: {1000*pos[1] + 4 * pos[0] + facing}")
part1 = False
pos, facing = sim_path(map, path, start, part1)
print(f"Ended at {pos} facing direction {facing}")
print(f"Part 2 answer: {1000*pos[1] + 4 * pos[0] + facing}")