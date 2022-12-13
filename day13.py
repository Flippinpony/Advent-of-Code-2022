import ast
import copy
paired_packets = []
all_packets = []

def str_to_list(str): 
     return ast.literal_eval(str.strip())
     
def load_packets(paired, all):
    line_num = 0
    # add divider packets for full set
    all.append([[2]])
    all.append([[6]])
    with open("input/day13input.txt") as file:
        lines = file.readlines()
        while line_num < len(lines):
            left = str_to_list(lines[line_num])
            right = str_to_list(lines[line_num + 1])
            # for part 1
            paired.append((left,right))
            # for part 2
            all.append(copy.deepcopy(left))
            all.append(copy.deepcopy(right))
            line_num += 3

def eval_pair(left, right):
    # handle two lists
    if type(left) == type(right) == list:
        result = None
        while left and right and result == None:
            result = eval_pair(left.pop(0), right.pop(0))
        if result != None:
            return result
        elif left and not right:
            return False
        elif right and not left:
            return True
        
    # handle two ints
    elif type(left) == type(right) == int and left != right:
        return left < right
    # handle one of each
    elif type(left) != type(right):
        if type(left) == int:
            return eval_pair([left], right)
        else:
            return eval_pair(left,[right])

def find_right_order(packets):
    index = 1
    sum = 0
    for packet_pair in packets:
        result = None
        left = packet_pair[0]
        right = packet_pair[1]
        result = eval_pair(left, right)
        if result:
            sum += index
        index += 1

    return sum


def bubble_sort(packets):
    n = len(packets)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if not eval_pair(copy.deepcopy(packets[j]), copy.deepcopy(packets[j + 1])):
                packets[j], packets[j + 1] = packets[j + 1], packets[j]


def find_decoder_key(packets):
    key = 1
    for i, packet in enumerate(packets):
        if packet:
            contents = packet.pop()
            if type(contents) == list and contents:
                inner = contents.pop()
                if not contents and not packet and (inner == 2 or inner == 6):
                    print("Key part found")
                    key *= i + 1
    return key

# driver
load_packets(paired_packets, all_packets)
ans1 = find_right_order(paired_packets)
print("Part 1 answer: " + str(ans1))
bubble_sort(all_packets)
ans2 = find_decoder_key(all_packets)
print("Part 2 answer: " + str(ans2))