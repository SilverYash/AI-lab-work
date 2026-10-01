import random

diff = int(input("enter the diffculty of the game if its easy enter 1 if its medium enter 2 if its hard eneter 3: "))

grid = []
i = 0
while i < 3:
    j = 0
    temp = []
    while j < 3:
        temp.append(0)
        j += 1
    grid.append(temp)
    i += 1

running = True

def print_board():
    print("\nCurrent Board:")
    symbols = {0: ".", 1: "X", 2: "O"}
    for row in grid:
        print(" ".join(symbols[cell] for cell in row))
    print()

def check_win():
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] != 0:
            return grid[i][0]
        if grid[0][i] == grid[1][i] == grid[2][i] != 0:
            return grid[0][i]
            
    if grid[0][0] == grid[1][1] == grid[2][2] != 0:
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] != 0:
        return grid[0][2]

    has_empty = False
    for row in grid:
        if 0 in row:
            has_empty = True
            break
            
    if not has_empty:
        return "Tie"
        
    return None

print_board()

while running:
    try:
        rmove = int(input("enter the row number of the cell number (0-2): "))
        cmove = int(input("enter the col number of the cell number (0-2): "))
    except ValueError:
        print("Please enter valid integers.")
        continue

    while rmove < 0 or rmove > 2 or cmove < 0 or cmove > 2 or grid[rmove][cmove] != 0:
        print("cell invalid type another")
        try:
            rmove = int(input("enter the row number of the cell number (0-2): "))
            cmove = int(input("enter the col number of the cell number (0-2): "))
        except ValueError:
            continue
            
    grid[rmove][cmove] = 1
    print_board()
    
    status = check_win()
    if status is not None:
        if status == 1:
            print("user wins!")
        elif status == "Tie":
            print("game over: It's a tie!")
        running = False
        break

    cost = {}
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            if grid[i][j] == 0:
                costofcell = 0
                if i - 1 >= 0:
                    if grid[i-1][j] != 0: costofcell += 1
                if i + 1 < 3:
                    if grid[i+1][j] != 0: costofcell += 1
                if j - 1 >= 0:
                    if grid[i][j-1] != 0: costofcell += 1
                if j + 1 < 3:
                    if grid[i][j+1] != 0: costofcell += 1
                
                if costofcell not in cost:
                    cost[costofcell] = []
                cost[costofcell].append([i, j])
            j += 1
        i += 1

    indexes = list(cost.keys())
    indexes.sort()
    
    if diff == 1:
        ind = indexes[0]
    elif diff == 2:
        ind = indexes[len(indexes) // 2]
    else:
        ind = indexes[-1]

    coord = random.choice(cost[ind])
    grid[coord[0]][coord[1]] = 2
    print(f"Computer played at row {coord[0]}, col {coord[1]} (Cost targeted: {ind})")
    print_board()

    status = check_win()
    if status is not None:
        if status == 2:
            print("computer wins!")
        elif status == "Tie":
            print("game over: It's a tie!")
        running = False
