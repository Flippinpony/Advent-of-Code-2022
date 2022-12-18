from collections import deque
import time

class Block:
    def __init__(self, type):
        self.type = type

    def get_width(self):
        return len(self.type)
        # see what I did there?
    
    def get_height(self):
        match self.type:
            case "wide":
                return 1
            case "exe":
                return 3
            case "ell":
                return 3
            case "i":
                return 4
            case "sq":
                return 2
    def get_block_coords(self):
        match self.type:
            case "wide":
                return ((0,0), (1,0), (2,0), (3,0))
            case "exe":
                return ((0,0), (1,0), (1,-1), (1,1), (2,0))
            case "ell":
                return ((0,0), (1,0), (2,0), (2,1), (2,2))
            case "i":
                return ((0,0), (0,1), (0,2), (0,3))
            case "sq":
                return ((0,0), (1,0), (1,1), (0,1))

# we'll define a block's coordinate as the bottom left part of it
start_x = 2
start_y = 4 # 3 units above the floor for now
chamber_width = 7
block_count = 1_000_000_000_000
flow_index = 0
# initial ground layer and headroom
layers = [[True, True, True, True, True, True, True],
        [False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False]]
jets = deque()
block_types = deque([Block("wide"), Block("exe"), Block("ell"), Block("i"), Block("sq")])
# import jet pattern
with open("input/day17input.txt") as file:
    jets = deque([*file.readline()])

def update_layers(block_coord, block_type):
    global layers
    # print(f"Block resting at {block_coord}")
    for block_coord_local in block_type.get_block_coords():
        new_block_coord = (block_coord_local[0] + block_coord[0], block_coord_local[1] + block_coord[1])
        if new_block_coord[1] >= len(layers) - 7:
            # add new layer
            layers.append([False, False, False, False, False, False, False])
        layers[new_block_coord[1]][new_block_coord[0]] = True
    return True

def drop_block(block_type):
    global start_x, start_y, chamber_width, jets, flow_index
    block_coord = (start_x, start_y)
    # ugly exception for exe since I want to track by left edge and not bottom
    if block_type.type == "exe": block_coord = (block_coord[0], block_coord[1]+1)
    while True:
        # jet movement
        direction = jets[0]
        jets.rotate(-1)
        if direction == '<':
            if can_move(block_coord, (block_coord[0] - 1,block_coord[1]), block_type):
                block_coord = (block_coord[0]-1, block_coord[1])
        elif direction == '>':
            if can_move(block_coord, (block_coord[0] + 1,block_coord[1]), block_type):
                block_coord = (block_coord[0]+1, block_coord[1])
        else: 
            print("Invalid direction!")
        flow_index = (flow_index + 1) % len(jets)
        # descent
        target_coord = (block_coord[0], block_coord[1] - 1)
        if can_move(block_coord, target_coord, block_type):
             block_coord = target_coord
        else:
            # rested, update start_y and grid
            update_layers(block_coord, block_type)
            start_y = len(layers) - 4
            break

def can_move(coord, new_coord, block_type):
    global layers
    global chamber_width
    for block_coord_local in block_type.get_block_coords():
        block_coord = (block_coord_local[0] + new_coord[0], block_coord_local[1] + new_coord[1])
        if block_coord[0] < 0 or block_coord[1] < 0 or block_coord[0] >= chamber_width or layers[block_coord[1]][block_coord[0]]:
            return False
    return True

def print_grid():
    global layers
    layer_rev = layers.copy()
    layer_rev.reverse()
    for layer in layer_rev:
        for x in range(chamber_width):
            if layer[x]:
                print("#", end="")
            else:
                print(".", end="")
        print('')
    

# driver
start_time = time.time()
history = {}
for i in range(block_count):
    drop_block(block_types[0])
    # print(f"Step {i}")
    # print_grid()
    block_types.rotate(-1)
    # save state for cycle detection
    rock_type = i % 5
    key = (rock_type, flow_index)
    if key in history:
        prev_rock, prev_height = history[key]
        period = i - prev_rock
        if i % period == block_count % period:
            cycle_height = start_y - 4 - prev_height
            rocks_remaining = block_count - i
            cycles_remaining = (rocks_remaining // period) + 1
            print(f"Part 2 answer: {prev_height + (cycle_height * cycles_remaining) - 1}") 
            break
    else:
        history[key] = (i, start_y-4)
    
print(f"Pat 1 Answer: {start_y - 4}")
end_time = time.time()
print(f"Runtime: {end_time-start_time}")