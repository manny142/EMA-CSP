def print_board(board):
    # Display the 3x3 board with position numbers for empty spaces
    for i in range(3):
        print(f" {board[i*3] if board[i*3] != ' ' else i*3} | {board[i*3+1] if board[i*3+1] != ' ' else i*3+1} | {board[i*3+2] if board[i*3+2] != ' ' else i*3+2}")
        if i < 2:
            print("-----------")

def check_winner(board, player):
    # Check all winning combinations by 3 rows, 3 cols, 2 diagonals
    wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(board[a] == board[b] == board[c] == player for a,b,c in wins)

def tic_tac_toe():
    # Initialize empty board and start game loop
    board = [' '] * 9
    
    while True:
        print_board(board)
        
        # Player move: get valid position input
        while True:
            pos = int(input("Enter position (0-8): "))
            if board[pos] == ' ':
                board[pos] = 'X'
                break
        
        # Check player win
        if check_winner(board, 'X'):
            print_board(board)
            print("You win!")
            break
        
        # Computer move: place at first available position
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                break
        
        # Check computer win
        if check_winner(board, 'O'):
            print_board(board)
            print("Computer wins!")
            break
        
        # Check draw
        if ' ' not in board:
            print_board(board)
            print("It's a draw!")
            break

# Run the game
tic_tac_toe()
