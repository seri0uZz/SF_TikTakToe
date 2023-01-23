def greet():
    print("-----------------")
    print("|  Welcome you  |")
    print("|  in the game  |")
    print("| 'Tic-Tac-Toe' |")
    print("-----------------")
    print("Input format: X Y")
    print("X - row number  ")
    print("Y - column number")


def show_board():
    print()
    print(f"   | 0 | 1 | 2 |")
    print("----------------")
    for i in range(3):
        print(f"{i}  | {board[i][0]} | {board[i][1]} | {board[i][2]} |")
        print("----------------")
    print()


def request_coordinates():
    while True:
        coordinates = input("Input coordinates: ").split()
        if len(coordinates) != 2:
            print("Please, input 2 coordinates!")
            continue

        if not (coordinates[0].isdigit()) or not (coordinates[1].isdigit()):
            print("Please, input the numbers!")
            continue

        x, y = map(int, coordinates)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Coordinates must be between '0' and '2'. Try again, please.")
            continue

        if board[x][y] != " ":
            print("The cell on the board is occupied. Try again, please")
            continue

        return x, y


def win_condition():
    win_coordinates = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                       ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                       ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for coordinates in win_coordinates:
        symbols = []
        for c in coordinates:
            symbols.append(board[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("'X' WON!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("'0' WON!!!")
            return True
    return False


greet()
board = [[" "] * 3 for _ in range(3)]
count = 0

while True:
    count += 1
    show_board()
    if count % 2 == 1:
        print("Your turn 'X'")
    else:
        print("Your turn 'O'")

    x, y = request_coordinates()

    if count % 2 == 1:
        board[x][y] = "X"
    else:
        board[x][y] = "0"

    if win_condition():
        break

    if count == 9:
        print("Draw!")
        break
