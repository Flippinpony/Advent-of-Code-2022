from collections import deque

monkeys = []
round_count = 0
max_round = 10000
relief_val = 3
is_part1 = False

class Monkey:
    def __init__(self, id, items, operation, test, true_dest, false_dest):
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.true_dest = true_dest
        self.false_dest = false_dest
        self.inspect_count = 0
    
    def do_turn(self):
        while len(self.items) > 0:
            item = self.items.popleft()
            # inspect item and apply operation
            item = eval(self.operation.split(" = ")[1].replace("old", str(item)))
            self.inspect_count += 1
            # apply relief value
            if(is_part1):
                item = item // relief_val
            else:
                item = item % relief_val
            # evaluate test and pass item
            num = int(self.test.split(" ").pop())
            dest = 0
            if item % num == 0:
               dest = int(self.true_dest.strip().split(" ").pop())
            else:
                 dest = int(self.false_dest.strip().split(" ").pop())
            monkeys[dest].items.append(item)

    def print(self):
        print("\tMonkey " + str(self.id) + " (inspect count " + str(self.inspect_count) + "): ", end = '')
        print(self.items)


def populate_monkeys():
    global monkeys
    line_num = 0
    with open("input/day11input.txt") as file:
        lines = file.readlines()
        while line_num < len(lines):
            items = deque(map(int, lines[line_num+1][18:].strip().split(", ")))
            operation = lines[line_num+2][13:]
            test = lines[line_num+3][8:]
            true_dest = lines[line_num+4][13:]
            false_dest = lines[line_num+5][14:]
            monkeys.append(Monkey(len(monkeys), items, operation, test, true_dest, false_dest))
            line_num += 7

def do_round():
    global round_count
    global is_part1
    round_count += 1
    for monkey in monkeys:
        monkey.do_turn()
    if(is_part1):
        print("Round " + str(round_count) + " results:")
        for monkey in monkeys:
         monkey.print()


populate_monkeys()
if(not is_part1):
    relief_val = 1
    for monkey in monkeys:
        relief_val *= int(monkey.test.split(" ").pop())
while (round_count < max_round):
    do_round()
first = 0
second = 0
for monkey in monkeys:
    if(monkey.inspect_count > first):
        second = first
        first = monkey.inspect_count
    elif(monkey.inspect_count > second):
        second = monkey.inspect_count

print("Monkey Business: " + str(first*second))
print(relief_val)