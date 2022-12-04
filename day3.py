sack1 = ""
sack2 = ""
total1 = 0
total2 = 0

def get_char_value(in_char):
    if(in_char.islower()):
        return ord(in_char)-96  
    else:
        return ord(in_char)-38

with open("input/day3input.txt") as file:
    for line in file:
        sack1 = line[:len(line)//2]
        sack2 = line[len(line)//2:]
        for char in sack1:
            if(char in sack2):
                total1 += get_char_value(char)
                break
print(total1)


with open("input/day3input.txt") as file:
    lines = file.readlines()
    for i in range(0, len(lines), 3):
        elf1 = lines[i].strip()
        elf2 = lines[i+1].strip()
        elf3 = lines[i+2].strip()
        candidates = {x for x in elf1 if x in elf2}
        result = {x for x in candidates if x in elf3}
        total2 += get_char_value(result.pop())
print(total2)
