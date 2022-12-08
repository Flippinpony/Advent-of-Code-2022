max_row = 99
max_col = 99
tree_grid = [[0 for i in range(max_col)] for j in range(max_row)]
vis_count = 0

def make_grid():
    with open("input/day8input.txt") as file:
        x = 0
        y = 0
        for line in file:
            for num in line:
                if(num != "\n"):
                    tree_grid[x][y] = int(num)
                    x += 1
    
            x = 0
            y += 1

make_grid()

# part 1 (I am not proud of this but its late)
for x in range(max_col):
    for y in range(max_row):

        # edge tree
        if x == 0 or y == 0 or x == max_col - 1 or y == max_row - 1:
            vis_count += 1
        else:
            height = tree_grid[x][y]
            vis_l = True
            vis_r = True
            vis_u = True
            vis_d = True
            # left 
            for col in range(x):
                if tree_grid[col][y] >= height:
                    vis_l = False
                    break
            # right 
            for col in range(x+1,max_col):
                if tree_grid[col][y] >= height:
                    vis_r = False
                    break
            # up 
            for row in range(y):
                if tree_grid[x][row] >= height:
                    vis_u = False
                    break
            # down 
            for row in range(y+1,max_row):
                if tree_grid[x][row] >= height:
                    vis_d = False
                    break
            if vis_l or vis_r or vis_u or vis_d:
                vis_count += 1

print(vis_count)

# part 2
top_score = 0
for x in range(max_col):
    for y in range(max_row):
        l_score = 0
        r_score = 0
        u_score = 0
        d_score = 0
        height = tree_grid[x][y]
        # left
        x_star = x
        y_star = y
        while (x_star > 0):
            l_score += 1
            x_star -= 1
            if(tree_grid[x_star][y] >= height):
                break
        # right
        x_star = x
        y_star = y
        while (x_star < max_col - 1):
            r_score += 1
            x_star += 1
            if(tree_grid[x_star][y] >= height):
                break
        # up
        x_star = x
        y_star = y
        while (y_star > 0):
            u_score += 1
            y_star -= 1
            if(tree_grid[x][y_star] >= height):
                break
        # down
        x_star = x
        y_star = y
        while (y_star < max_row - 1):
            d_score += 1
            y_star += 1
            if(tree_grid[x][y_star] >= height):
                break
        score = l_score*r_score*u_score*d_score
        if score > top_score:
            top_score = score
print(top_score)