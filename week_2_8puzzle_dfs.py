def dfs(start, goal):
    stack = [(start, [])]
    visited = {start}

    while stack:
        state, path = stack.pop()

        if state == goal:
            return path

        blank = state.index(0)
        row = blank // 3
        col = blank % 3

        # Moves: Up, Down, Left, Right
        moves = [
            (-1, 0, "Up"),
            (1, 0, "Down"),
            (0, -1, "Left"),
            (0, 1, "Right")
        ]

        for dr, dc, move in moves:
            new_row = row + dr
            new_col = col + dc

            if 0 <= new_row < 3 and 0 <= new_col < 3:

                new_blank = new_row * 3 + new_col

                new_state = list(state)

                new_state[blank], new_state[new_blank] = \
                    new_state[new_blank], new_state[blank]

                new_state = tuple(new_state)

                if new_state not in visited:
                    visited.add(new_state)
                    stack.append(
                        (new_state, path + [move])
                    )

    return None


# -------------------------------
# INPUT
# -------------------------------

print("Enter START state (9 numbers, use 0 for blank):")
start = tuple(map(int, input().split()))

print("Enter GOAL state (9 numbers, use 0 for blank):")
goal = tuple(map(int, input().split()))


# Check input
if len(start) != 9 or len(goal) != 9:
    print("Error: You must enter exactly 9 numbers.")
    exit()

if set(start) != set(range(9)) or set(goal) != set(range(9)):
    print("Error: Use each number 0 to 8 exactly once.")
    exit()


# -------------------------------
# DFS
# -------------------------------

print("\nSearching...")

solution = dfs(start, goal)


# -------------------------------
# OUTPUT
# -------------------------------

if solution is not None:
    print("\nSolution found!")
    print("Moves:", solution)
    print("Number of moves:", len(solution))
else:
    print("\nNo solution found.")
