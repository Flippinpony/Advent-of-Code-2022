from collections import deque

elves = []
occupied = set()
movement_order = deque(["N","S","W","E"])
movement_coordinates = { "N" : ((0,-1),(-1,-1),(1,-1)), \
                         "S" : ((0,1),(-1,1),(1,1)), \
                         "W" : ((-1,0),(-1,1),(-1,-1)), \
                         "E" : ((1,0),(1,1),(1,-1))}
surround_coordinates = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
round_count = 1
equilibrium = False

class Elf:
    def __init__(self, position):
        self.position = position

def load_elves():
    file = open('input/day23input.txt', 'r')
    for y, line in enumerate(file):
        for x, char in enumerate(line):
            if char == "#":
                elves.append(Elf((x,y)))
                occupied.add((x,y))

def check_alone(elf):
    for coord in surround_coordinates:
        adjusted_coord = (elf.position[0]+coord[0], elf.position[1]+coord[1])
        if adjusted_coord in occupied:
            return False
    return True

def check_direction(elf, direction):
    coords = movement_coordinates[direction]
    for coord in coords:
        adjusted_coord = (elf.position[0]+coord[0], elf.position[1]+coord[1])
        if adjusted_coord in occupied:
            return False
    return True


def sim_step():
    global round_count, equilibrium
    # Get desired movement for each elf
    # remove any duplicates (coord as key, elf as value)
    movements = {}
    conflicted = set()
    for elf in elves:
        if not check_alone(elf):
            for direction in movement_order:
                if check_direction(elf, direction):
                    # we can move this direction
                    target = (elf.position[0] + movement_coordinates[direction][0][0], elf.position[1] + movement_coordinates[direction][0][1])
                    if target in movements:
                        movements.pop(target)
                        conflicted.add(target)
                    elif target not in conflicted:
                        movements[target] = elf
                    break
    # Process valid moves
    if len(movements) == 0:
        # we've reached equilibrium
        print(f"Equilibrium reached at round {round_count}")
        equilibrium = True
    for move in movements:
        occupied.remove(movements[move].position)
        movements[move].position = move
        occupied.add(move)
    # rotate movement order for next step
    movement_order.rotate(-1)
    round_count += 1

def get_bounds():
    min_x, min_y, max_x, max_y = 123,123,-123,-123
    for elf in elves:
        pos = elf.position
        min_x = min(min_x, pos[0])
        max_x = max(max_x, pos[0])
        min_y = min(min_y, pos[1])
        max_y = max(max_y, pos[1])
    return ((min_x, min_y), (max_x, max_y))

# driver
step_count = 1000 # 10 for part 1, something large for part 2
load_elves()
for i in range(step_count):
    if not equilibrium:
        sim_step()
bounds = get_bounds() # ((min x, min y),(max x, max y))
area = (bounds[1][0]-bounds[0][0] + 1) * (bounds[1][1]-bounds[0][1] + 1)
space = area -  len(elves)
print(f"Part 1 answer: {space}")
if equilibrium:
    print(f"Part 2 answer: {round_count-1}")