import queue

next_bench = 20
reg_x = 1
cycle = 0
cmds = queue.Queue()
queued_cmd = ""
queue_count = 0
ans1 = 0

def prime_cmd(cmd):
    global queue_count
    cmd_split = cmd.strip().split()
    op = cmd_split[0]
    if(op == "addx"):
        queue_count = 2
    elif (op == "noop"):
        queue_count = 1

def process_cmd(cmd):
    global reg_x
    if(cmd != ""):
        args = cmd.strip().split(" ")
        if args[0] == "addx":
            # print("adding to x "+ args[1])
            reg_x += int(args[1])

def draw_pxl():
    if cycle % 40 == 0:
        line_end = '\n'
    else:
        line_end = ''
    if abs(reg_x - (cycle - 1) % 40 ) <= 1:
        print("#", end = line_end)
    else:
        print(".", end = line_end)
    

with open("input/day10input.txt") as file:
    for line in file:
        cmds.put(line)

while(True):
    cycle += 1
    queue_count -= 1
    if(queue_count <= 0):
        # cmd finished
        # print("cmd finished at cycle " + str(cycle))
        if(cmds.empty()):
            break
        process_cmd(queued_cmd)
        queued_cmd = cmds.get()
        prime_cmd(queued_cmd)
    if cycle == next_bench:
        ans1 += cycle * reg_x
        next_bench += 40
    draw_pxl()
    
print(ans1)



