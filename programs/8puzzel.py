# 8-Puzzle Solvability Check using Inversion Count

def count_inversions(state):
    """
    Count the number of inversions in the 8-puzzle state.
    """
    # Flatten the 2D list into 1D list and ignore 0 (blank)
    flat_list = [num for row in state for num in row if num != 0]

    inversions = 0
    for i in range(len(flat_list)):
        for j in range(i + 1, len(flat_list)):
            if flat_list[i] > flat_list[j]:
                inversions += 1

    return inversions


def is_solvable(state):
    """
    Returns True if the 8-puzzle state is solvable, otherwise False.
    """
    return count_inversions(state) % 2 == 0


# Example Test Cases
initial_state_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]  # Solvable (Goal State)

initial_state_2 = [
    [1, 2, 3],
    [4, 6, 5],
    [7, 8, 0]
]  # Unsolvable

# Output
print("State 1 is solvable:", is_solvable(initial_state_1))
print("State 2 is solvable:", is_solvable(initial_state_2))