empty = set()
blizzards = []
start = (-1,-1)
end = (-1,-1)
height = 0
width = 0

directions = {"^" : (0, -1), ">" : (1, 0), "v" : (0, 1), "<" : (-1, 0)}

def load_map():
    global start, end, height, width
    file = open('input/day24input.txt', 'r')
    lines = file.readlines()
    height = len(lines)
    for y, line in enumerate(lines):
        if y == 0:
            # save off the start coord
            start = (line.rfind("."), 0)
            width = len(line)-1
        elif y == len(lines)-1:
            # save off the end coord
            end = (line.rfind("."), y)
        # add to grid
        for x, char in enumerate(line):
            if char == ".":
                empty.add((x,y))
            elif char in directions:
                blizzards.append(((x,y),directions[char]))
                empty.add((x,y))
        

def step_storm(blizzards):
    new_blizzards = []
    for blizzard in blizzards:
        curr = blizzard[0]
        next = (curr[0] + blizzard[1][0], curr[1] + blizzard[1][1])
        if next[0] == 0:
            next = (width-2, next[1])
        elif next[0] == width-1:
            next = (1, next[1])
        elif next[1] == 0:
            next = (next[0], height - 2)
        elif next[1] == height-1:
            next = (next[0], 1)
        new_blizzards.append((next,blizzard[1]))
    return new_blizzards


def get_directions(pos):
    options = set()
    options.add(pos)
    for dir in directions:
        options.add((pos[0] + directions[dir][0], pos[1] + directions[dir][1]))
    return options

# driver
load_map()
time = 0
not_done = True
possible = set()
possible.add(start)
step = 0
while not_done:
    
    time += 1
    blizzards = step_storm(blizzards)
    next_step = set()
    blocked = {x[0] for x in blizzards}
    for poss in possible:
        for direction in get_directions(poss):
            if direction in empty and direction not in blocked:
                next_step.add(direction)
   
    match step:
        case 0:
            if end in next_step:
                print(f"Reached goal after {time} minutes!")
                start, end = end, start
                step += 1
                next_step = set([start])
        case 1:
            if end in next_step:
                print(f"Returned to start after {time} minutes!")
                start, end = end, start
                step += 1
                next_step = set([start])
        case 2:
             if end in next_step:
                print(f"Reached goal (again) after {time} minutes!")
                not_done = False
        
    possible = next_step
    