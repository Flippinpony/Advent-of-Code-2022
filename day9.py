import math
knot_count = 10 # use 2 for part 1, 10 for part 2
knots = [[0 for i in range(2)] for j in range(knot_count)]
tail_history = {(0,0)}
allowed_dist = math.sqrt(2)

def update_knot(index):
    global knots
    if(math.dist((knots[index - 1][0],knots[index - 1][1]),(knots[index][0],knots[index][1])) > math.sqrt(2)):
        x_dist = abs(knots[index - 1][0] - knots[index][0])
        y_dist = abs(knots[index - 1][1] - knots[index][1])
        # straight movement
        if knots[index - 1][0] > knots[index][0] + 1 and knots[index - 1][1] == knots[index][1]:
            knots[index][0] += 1
        elif knots[index][0] > knots[index - 1][0] + 1 and knots[index - 1][1] == knots[index][1]:
            knots[index][0] -= 1
        elif knots[index - 1][1] > knots[index][1] + 1 and knots[index - 1][0] == knots[index][0]:
            knots[index][1] += 1
        elif knots[index][1] > knots[index - 1][1] + 1 and knots[index - 1][0] == knots[index][0]:
            knots[index][1] -= 1
        # diagonal movement
        else:
            if knots[index - 1][0] > knots[index][0]:
                knots[index][0] += 1
            else:
                knots[index][0] -= 1
            if knots[index - 1][1] > knots[index][1]:
                knots[index][1] += 1
            else:
                knots[index][1] -= 1

        # add to history
        if(index == knot_count - 1):
            tail_history.add((knots[index][0],knots[index][1]))


with open("input/day9input.txt") as file:
    for line in file:
        args = line.strip().split(' ')
        match args[0]:
            case "L":
                for i in range(int(args[1])):
                    knots[0][0] -= 1
                    for j in range(1,knot_count):
                        update_knot(j)
            case "R":
                for i in range(int(args[1])):
                    knots[0][0] += 1
                    for j in range(1,knot_count):
                        update_knot(j)
            case "U":
                for i in range(int(args[1])):
                    knots[0][1] += 1
                    for j in range(1,knot_count):
                        update_knot(j)
            case "D":
                for i in range(int(args[1])):
                    knots[0][1] -= 1
                    for j in range(1,knot_count):
                        update_knot(j)
        

print(len(tail_history))