def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def dfs_check(board, player, visited, i, j, dx, dy, count):
    """Depth-First Search to check consecutive player marks in a direction"""
    if count == 3:
        return True  # Found 3 in a row

    ni, nj = i + dx, j + dy

    if 0 <= ni < 3 and 0 <= nj < 3 and board[ni][nj] == player and not visited[ni][nj]:
        visited[ni][nj] = True
        return dfs_check(board, player, visited, ni, nj, dx, dy, count + 1)

    return False


def check_winner(board, player):
    """Uses DFS to check rows, columns, and diagonals"""

    for i in range(3):
        for j in range(3):

            if board[i][j] == player:

                # Reset visited for each check
                visited = [[False]*3 for _ in range(3)]
                visited[i][j] = True

                # Check horizontal, vertical, diagonals
                if (dfs_check(board, player, visited, i, j, 0, 1, 1) or
                    dfs_check(board, player, visited, i, j, 1, 0, 1) or
                    dfs_check(board, player, visited, i, j, 1, 1, 1) or
                    dfs_check(board, player, visited, i, j, 1, -1, 1)):
                    return True

    return False


def get_move(board):

    while True:
        try:
            row, col = map(int, input("Enter your move (row col): ").split())

            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                return row, col

            else:
                print("Invalid move, try again.")

        except ValueError:
            print("Invalid input, please enter numbers.")


def play_game():

    board = [[' ' for _ in range(3)] for _ in range(3)]

    current_player = 'X'

    while True:

        print_board(board)

        print(f"Player {current_player}, it's your turn.")

        row, col = get_move(board)

        board[row][col] = current_player

        if check_winner(board, current_player):

            print_board(board)

            print(f"Player {current_player} wins!")

            break

        if all(cell != ' ' for row in board for cell in row):

            print_board(board)

            print("It's a draw!")

            break

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    play_game()
