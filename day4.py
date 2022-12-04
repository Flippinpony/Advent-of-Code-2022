elf1 = set()
elf2 = set()
answer1 = 0
answer2 = 0

def populate_set(in_set, start, end):
    in_set.clear()
    for x in range(start,end+1):
        in_set.add(x)

with open("input/day4input.txt") as file:
    for line in file:
        elves = line.split(',')
        populate_set(elf1,int(elves[0].split('-')[0]),int(elves[0].split('-')[1]))
        populate_set(elf2,int(elves[1].split('-')[0]),int(elves[1].split('-')[1]))
        if (elf1.issuperset(elf2) or elf2.issuperset(elf1)):
            answer1 += 1
        if (not elf1.isdisjoint(elf2)):
            answer2 += 1
print(answer1)
print(answer2)