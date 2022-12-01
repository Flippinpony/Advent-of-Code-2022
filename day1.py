elflist = [0]
topelf = 0
topthree = 0

with open("input/day1input.txt") as file:
    for line in file:
        if line == "\n":
            elflist.append(0)
        else:
            elflist[len(elflist)-1]+=int(line)

elflist.sort()
topelf = elflist[len(elflist)-1]
topthree = topelf + elflist[len(elflist)-2] + elflist[len(elflist)-3]

print('top elf: ' + str(topelf))
print('top three: ' + str(topthree))