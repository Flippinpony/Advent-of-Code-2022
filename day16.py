from itertools import permutations

class Node:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
        self.connections = []
        self.routes = {}
    
    def add_connection(self, connection):
        self.connections.append(connection)

def load_nodes():
    nodes = {}
    with open("input/day16input.txt") as file:
        for line in file:
            args = line.strip().replace('=', ' ').replace(';',' ').split()
            new_node = Node(args[1], int(args[5]))
            for x in range(10,len(args)):
                new_node.add_connection(args[x].replace(',',''))
            nodes[new_node.name] = new_node
    return nodes

def bfs(nodes, frontier, end):
    dist = 1
    while True:
        next_frontier = set()
        for x in frontier:
            if x == end:
                return dist
            for y in nodes[x].connections:
                next_frontier.add(y)
        frontier = next_frontier
        dist += 1

# took some inspiration here from liampwll - https://gist.github.com/liampwll/351fb848f05e8efd257ac87c7d09d1b0
def find_best_recursive(opened, score, current, time_left):
    global best, nodes
    if score > best : best = score
    if time_left <= 0 : return
    if current not in opened:
        # open valve in current room and proceed
        find_best_recursive(opened.union([current]), score + nodes[current].rate * time_left, current, time_left - 1)
    else:
        # try for each unvisited valve
        for k in [x for x in nodes[current].routes.keys() if x not in opened]:
             find_best_recursive(opened, score, k, time_left - nodes[current].routes[k])

def find_best_recursive_two_runners(opened, score, current, time_left, me):
    global pt_2_best, nodes, start_node
    if score > pt_2_best : pt_2_best = score
    if time_left <= 0 : return
    if current not in opened:
        # open valve in current room and proceed
        find_best_recursive_two_runners(opened.union([current]), score + nodes[current].rate * time_left, current, time_left - 1, me)
        # I will open first valve, so elephant can run one ahead
        if me:
            # kick off second iteration, with initial valve already opened. Don't subtract from time since elephant isn't stopping
            find_best_recursive_two_runners(set([current]).union(opened), score + nodes[current].rate * time_left, start_node, 25, False)
    else:
        # try for each unvisited valve
        for k in [x for x in nodes[current].routes.keys() if x not in opened]:
             find_best_recursive_two_runners(opened, score, k, time_left - nodes[current].routes[k], me)




# driver
nodes = load_nodes()
start_node = 'AA'
# get mapping of distance between each important node and the others so we can forget about the liminal nodes
open_valves = sorted([x for x in list(nodes.keys()) if nodes[x].rate != 0])
for k in open_valves + [start_node]:
    for k2 in nodes:
        if k2 != k:
            nodes[k].routes[k2] = bfs(nodes, nodes[k].connections, k2)
time_left = 29
best = 0
find_best_recursive(set([start_node]), 0, start_node, time_left)
print(f"Part 1: {best}")

pt_2_best = 0
find_best_recursive_two_runners(set([start_node]), 0, start_node, time_left-4, True)
print(f"Part 2: {pt_2_best}")