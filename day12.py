import collections

max_x =  61
max_y =  41
heightmap = [[0 for i in range(max_y)] for j in range(max_x)]
start_x = 0
start_y = 0
dest_x = 0
dest_y = 0

def is_end(coord):
    global dest_x, dest_y
    return coord[0] == dest_x and coord[1] == dest_y

def import_heightmap():
    global heightmap, start_x, start_y, dest_x, dest_y
    with open("input/day12input.txt") as file:
        x, y = 0, 0
        for line in file:
            for char in line:
                if char == 'S':
                    heightmap[x][y] = 1
                    start_x = x
                    start_y = y
                elif char == 'E':
                    heightmap[x][y] = 26
                    dest_x = x
                    dest_y = y
                elif char == '\n':
                    # ignore new line char
                    pass
                else:
                    heightmap[x][y] = ord(char) - 96
                x += 1
            x = 0
            y += 1

def bfs(start):
    global max_x, max_y
    visited = set([start])
    queue = collections.deque([(start[0], start[1], 0)])

    while queue:
        x, y, dist = queue.popleft()
        if is_end((x,y)):
            return dist

        for new_position in [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]:
            if 0 <= new_position[0] < max_x and 0 <= new_position[1] < max_y:
                if is_end(new_position) and 26 - heightmap[x][y] <= 1:
                    queue.append((new_position[0], new_position[1], dist + 1))
                elif not is_end(new_position) and new_position not in visited and heightmap[new_position[0]][new_position[1]] - heightmap[x][y] <= 1:
                    visited.add((new_position[0], new_position[1]))
                    queue.append((new_position[0], new_position[1], dist + 1))


import_heightmap()

# part 1
print("Starting search. Start: " + str(start_x)+", "+str(start_y)+" End: "+str(dest_x)+", "+str(dest_y))
distance = bfs((start_x, start_y))
print("Found in " + str(distance))

# part 2
best_result = float('inf')
for x in range(len(heightmap)):
    for y in range(len(heightmap[x])):
        if heightmap[x][y] == 1:
            dist = bfs((x,y))
            if dist and dist < best_result:
                best_result = dist
print("Part two best result: " + str(best_result))
