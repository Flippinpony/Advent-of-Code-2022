import re
import copy
import time

class Inventory:
    def __init__(self):
        self.ore = 0
        self.clay = 0
        self.obsidian = 0
        self.geode = 0
        self.ore_robot = 1
        self.clay_robot = 0
        self.obsidian_robot = 0
        self.geode_robot = 0
        self.queue = ""

    def process_queue(self):
        match self.queue:
            case "ore":
                self.ore_robot += 1
            case "clay":
                self.clay_robot += 1
            case "obsidian":
                self.obsidian_robot += 1
            case "geode":
                self.geode_robot += 1
        self.queue = ""

    def tick(self):
        self.ore += self.ore_robot
        self.clay += self.clay_robot
        self.obsidian += self.obsidian_robot
        self.geode += self.geode_robot
        self.process_queue()



def load_blueprints():
    blueprints = []
    with open("input/day19input.txt") as file:
        for line in file:
            nums = [int(n) for n in re.findall(r'-?\d+', line)]
             # tack on the max ore cost
            max_ore = max(nums[1], nums[2], nums[3], nums[5])
            blueprints.append([nums[1], nums[2], (nums[3], nums[4]), (nums[5], nums[6]), max_ore])
    return blueprints
            
def sim(blueprint, time_left, inventory, results):
    # if queue is loaded, we need to tick first
    if inventory.queue != "":
        inventory.tick()
        time_left -= 1

    # enough time to build a bot
    if time_left >= 2:
        # sim all possible choices
        # build ore next
        if  inventory.ore_robot < blueprint[max_ore]:
            time = 0
            new_inv = copy.deepcopy(inventory)
            while new_inv.ore < blueprint[ore]:
                new_inv.tick()
                time+= 1
            new_inv.ore -= blueprint[ore]
            new_inv.queue = "ore"
            if time_left - time >= 2:
                sim(blueprint, time_left - time, new_inv, results)
        # build clay next
        if inventory.clay_robot < blueprint[obsidian][1]:
            time = 0
            new_inv = copy.deepcopy(inventory)
            while new_inv.ore < blueprint[clay]:
                new_inv.tick()
                time+= 1
            new_inv.ore -= blueprint[clay]
            new_inv.queue = "clay"
            if time_left - time >= 2:
                sim(blueprint, time_left - time, new_inv, results)
        # build obsidian next
        if  inventory.obsidian_robot < blueprint[geode][1] and inventory.clay_robot > 0:
            time = 0
            new_inv = copy.deepcopy(inventory)
            while new_inv.ore < blueprint[obsidian][0] or new_inv.clay < blueprint[obsidian][1]:
                new_inv.tick()
                time+= 1
            new_inv.ore -= blueprint[obsidian][0]
            new_inv.clay -= blueprint[obsidian][1]
            new_inv.queue = "obsidian"
            if time_left - time >= 2:
                sim(blueprint, time_left - time, new_inv, results)
        # build geode next
        if inventory.obsidian_robot > 0:
            time = 0
            new_inv = copy.deepcopy(inventory)
            while new_inv.ore < blueprint[geode][0] or new_inv.obsidian < blueprint[geode][1]:
                new_inv.tick()
                time+= 1
            new_inv.ore -= blueprint[geode][0]
            new_inv.obsidian -= blueprint[geode][1]
            new_inv.queue = "geode"
            if time_left - time >= 2:
                sim(blueprint, time_left - time, new_inv, results)
        

    else:
    # we're done, process last tick(s)
        while time_left > 0:
            inventory.tick()
            time_left -= 1
        results.append(inventory.geode)


# driver
start_time = time.time()
starting_robots = [1,0,0,0]
ore, clay, obsidian, geode, max_ore = 0,1,2,3,4
blueprints = load_blueprints()
# part 1
max_time = 24
total_quality = 0
for i, blueprint in enumerate(blueprints):
    print(f"Simming blueprint {i}")
    results = []
    sim(blueprint, max_time, Inventory(), results)
    total_quality += sorted(results)[len(results)-1] * (i+1)
print(f"Part 1 answer: {total_quality}")

# part 2
# using my part 1 algorithm as-is takes about an hour and a half to run but.. it works!
max_time = 32
total_quality = 1
for i in range(3):
    print(f"Simming blueprint {i}")
    results = []
    sim(blueprints[i], max_time, Inventory(), results)
    total_quality *= sorted(results)[len(results)-1]
print(f"Part 2 answer: {total_quality}")

end_time = time.time()
print(f"Runtime: {end_time-start_time}")