def initialize_board():
    """Initializes an empty Tic Tac Toe board."""
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print("|".join(row))
        print("-" * 5)

def player_move(board, player):
    """Allows a player to make a move on the board."""
    try:
        row = int(input(f"Player {player}, enter your row (0-2): "))
        col = int(input(f"Player {player}, enter your column (0-2): "))
        if board[row][col] == " ":
            board[row][col] = player
        else:
            print("This spot is already taken.")
            player_move(board, player)
    except (ValueError, IndexError):
        print("Please enter a valid row and column.")
        player_move(board, player)

def check_win(board):
    """Checks if there is a win on the board."""
    # Check rows, columns, and diagonals
    lines = []
    lines.extend(board)  # Rows
    lines.extend([[board[row][col] for row in range(3)] for col in range(3)])  # Columns
    lines.append([board[i][i] for i in range(3)])  # Diagonal
    lines.append([board[i][2-i] for i in range(3)])  # Anti-diagonal

    for line in lines:
        if line.count(line[0]) == 3 and line[0] != " ":
            return True
    return False

def check_tie(board):
    """Checks if there is a tie."""
    for row in board:
        if " " in row:
            return False
    return True

def play_game():
    """Main function to play the game."""
    board = initialize_board()
    current_player = "X"
    
    while True:
        print_board(board)
        player_move(board, current_player)
        
        if check_win(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()