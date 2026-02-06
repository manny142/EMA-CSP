import random
number = random.randint(1, 9)
number = str(number)
player = input("Enter your move (row and column)example : 1,2: ")
tic = player.split(",")
toe = tic[0] + tic[1]
a = "      |                     |"
b = "      |                     |"
c = " _____|_____________________|______"
d = "      |                     |"
e = "      |                     |"
f = " _____|_____________________|______"
g = "      |                     |"
h = "      |                     |"
s = " _____|_____________________|______"
# build board and place player's move
board = [[" " for _ in range(3)] for _ in range(3)]
try:
    r = int(tic[0].strip()) - 1
    c = int(tic[1].strip()) - 1
    if 0 <= r < 3 and 0 <= c < 3:
        board[r][c] = "X"
    else:
        print("Invalid move. Use numbers 1-3.")
except Exception:
    print("Invalid input. Use format row,col like 1,2")
robot = "X"
player = "O"

# Robot responds when player selects a cell
if board[r][c] == " ":
    board[r][c] = player
    robot_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    if robot_moves:
        robot_response = random.choice(robot_moves)
        board[robot_response[0]][robot_response[1]] = robot
    # Robot chooses cell randomly that is empty and places its move there
    print(robot_response)
# print board
print()
for i, row in enumerate(board):
    print(" " + " | ".join(row))
    if i < 2:
        print("---+---+---")
print()