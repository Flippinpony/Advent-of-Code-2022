from collections import deque

stack1 = deque(['B', 'S', 'J', 'Z', 'V', 'D', 'G'])
stack2 = deque(['P', 'V', 'G', 'M', 'S', 'Z'])
stack3 = deque(['F', 'Q', 'T', 'W', 'S', 'B', 'L', 'C'])
stack4 = deque(['Q', 'V', 'R', 'M', 'W', 'G', 'J', 'H'])
stack5 = deque(['D', 'M', 'F', 'N', 'S', 'L', 'C'])
stack6 = deque(['D', 'C', 'G', 'R'])
stack7 = deque(['Q', 'S', 'D', 'J', 'R', 'T', 'G', 'H'])
stack8 = deque(['V', 'F', 'P'])
stack9 = deque(['J', 'T', 'S', 'R', 'D'])

def get_stack(index):
    return globals()["stack"+str(index)]


with open("input/day5input.txt") as file:
    for line in file:
        split_line = line.split(' ')
        count = int(split_line[1])
        source = int(split_line[3])
        dest = int(split_line[5])
        #part 1 method
        #for i in range(count):
            #get_stack(dest).appendleft(get_stack(source).popleft())

        #part 2 method
        to_move = deque()
        for i in range(count):
            to_move.append(get_stack(source).popleft())
        to_move.reverse()
        get_stack(dest).extendleft(to_move)

print(stack1)
print(stack2)
print(stack3)
print(stack4)
print(stack5)
print(stack6)
print(stack7)
print(stack8)
print(stack9)