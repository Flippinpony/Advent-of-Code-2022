class Node:
    def __init__(self, parent, name, size):
        self.name = name
        self.parent = parent
        self.size = size
        self.children = {}

    def PrintTree(self):
        print(self.name + ":" + str(self.size))
        for key in self.children:
            self.children[key].PrintTree()

    def IsDir(self):
        return len(self.children) != 0
    
    def FindChild(self, name):
        return self.children[name]

    def AddChild(self, parent, name, size):
        self.children[name] = Node(self, name, size)
        file_ancestor = self
        while file_ancestor != None:
            file_ancestor.size += size
            file_ancestor = file_ancestor.parent

def recursive_pt1(current_node):
    total = 0
    for key in current_node.children:
        total += recursive_pt1(current_node.children[key])
    if(current_node.IsDir() and current_node.size <= 100000):
        total += current_node.size
    return total

def recursive_pt2(current_node, target_size, candidate):
    new_candidate = candidate
    for key in current_node.children:
            new_candidate = recursive_pt2(current_node.children[key], target_size, new_candidate)
    if(current_node.IsDir() and current_node.size > target_size and current_node.size <= new_candidate.size):
        new_candidate = current_node
    return new_candidate


filesys = Node(None, "/", 0)
dir = filesys

with open("input/day7input.txt") as file:
    
    for line in file:
        current_line = line.strip().split(' ') 
        if current_line[0] == "$":
            cmd = current_line[1]
            if cmd == "cd":
                target = current_line[2]
                if (target == "/"):
                    dir = filesys
                elif(target == ".."):
                    dir = dir.parent
                else:
                    dir = dir.FindChild(target)
            elif cmd == "ls":
                # do nothing
                continue
        elif current_line[0] == "dir":
            # dir found
            dir.AddChild(dir, current_line[1], 0)
        else:
            # file info found
            dir.AddChild(dir, current_line[1], int(current_line[0]))

# tree built, iterate to find directory size
print(str(recursive_pt1(filesys)))

# calc space we need to delete
total_size = 70000000
free_needed = 30000000
remaining_space = total_size - filesys.size
space_to_reclaim = free_needed - remaining_space

# recurse to find closest candidate
candidate = recursive_pt2(filesys, space_to_reclaim, filesys)
print(str(candidate.size))

# print(filesys.PrintTree())
