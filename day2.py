total_score_pt1 = 0
total_score_pt2 = 0

with open("input/day2input.txt") as file:
    for line in file:
        theirs = ord(line[0]) - 64
        mine = ord(line[2]) - 87
        total_score_pt1 += mine;
        if mine == theirs:
            total_score_pt1 += 3
        elif (mine ) % 3 == (theirs + 1) % 3:
            total_score_pt1 += 6

print (total_score_pt1)

with open("input/day2input.txt") as file:
    for line in file:
        theirs = ord(line[0]) - 64
        match line[2]:
            case 'X':
                mine = ((theirs + 1) % 3) + 1
            case 'Y':
                mine = theirs
                total_score_pt2 += 3
            case 'Z':
                mine = (theirs % 3) + 1
                total_score_pt2 += 6
                
        total_score_pt2 += mine

print(total_score_pt2)
