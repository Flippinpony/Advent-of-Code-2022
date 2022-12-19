
import collections
x, y, z = 0, 1, 2
max_coord = 22

adjacents = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1)
]

def get_voxels():
    voxels = set()
    with open("input/day18input.txt") as file:
        for line in file:
            voxels.add(tuple(int(n) for n in line.split(',')))
    return voxels
    
def get_empty(voxels, max_coord):
    grid = {(x, y, z) for x in range(max_coord) for y in range(max_coord) for z in range(max_coord)}
    return list(grid - voxels)

def get_faces(voxels):
    # brute force neighbor-counting
    total_faces = 0
    for voxel in voxels:
        faces = 6
        for x1,y1,z1 in adjacents:
            if (voxel[x]+x1, voxel[y]+y1, voxel[z]+z1) in voxels:
                faces -= 1
        total_faces += faces
    return total_faces

def get_gaps(voxels, empty_space):
    gaps = []
    while empty_space:
        to_visit = [empty_space[0]]
        bubble = set()
        while len(to_visit):
            next = to_visit.pop()
            if next in empty_space:
                bubble.add(next)
                empty_space.remove(next)
                for x1,y1,z1 in adjacents:
                    to_visit.append((next[x]+x1, next[y]+y1, next[z]+z1))
        if (0,0,0) not in bubble:
            gaps.append(bubble)

    return gaps

# driver
voxels = get_voxels()
faces = get_faces(voxels)
print(f"Part 1: {faces}")

empty_space = get_empty(voxels, max_coord)
gaps = get_gaps(voxels, empty_space)
internal_faces = [get_faces(gap) for gap in gaps]
print(f"Part 2: {faces - sum(internal_faces)}")
