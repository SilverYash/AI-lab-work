def dls(state, goal, limit, path):
    # Goal test
    if state == goal:
        return []

    # Depth limit reached
    if limit == 0:
        return None

    # Find blank (0)
    blank = state.index(0)
    row = blank // 3
    col = blank % 3

    # Up, Down, Left, Right
    moves = [
        (-1, 0, "Up"),
        (1, 0, "Down"),
        (0, -1, "Left"),
        (0, 1, "Right")
    ]

    for dr, dc, move in moves:
        new_row = row + dr
        new_col = col + dc

        # Check valid move
        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

            # Create new state
            new_state = list(state)

            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            new_state = tuple(new_state)

            # Don't visit a state already on current path
            if new_state not in path:

                path.add(new_state)

                result = dls(
                    new_state,
                    goal,
                    limit - 1,
                    path
                )

                path.remove(new_state)

                if result is not None:
                    return [move] + result

    return None


def ids(start, goal):

    limit = 0

    while True:

        path = {start}

        result = dls(
            start,
            goal,
            limit,
            path
        )

        if result is not None:
            return result, limit

        limit += 1


# --------------------------------
# INPUT
# --------------------------------

print("Enter START state (use 0 for blank):")
start = tuple(map(int, input().split()))

print("Enter GOAL state (use 0 for blank):")
goal = tuple(map(int, input().split()))


# --------------------------------
# INPUT VALIDATION
# --------------------------------

if len(start) != 9 or len(goal) != 9:
    print("Error: Enter exactly 9 numbers.")
    exit()

if set(start) != set(range(9)) or set(goal) != set(range(9)):
    print("Error: Use numbers 0 to 8 exactly once.")
    exit()


# --------------------------------
# IDS
# --------------------------------

print("\nSearching using IDS...")

solution, depth = ids(start, goal)


# --------------------------------
# OUTPUT
# --------------------------------

print("\nSolution Found!")
print("Moves:", " -> ".join(solution))
print("Number of moves:", len(solution))
print("Depth:", depth)

