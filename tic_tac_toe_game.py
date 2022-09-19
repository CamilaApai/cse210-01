"""
CSE 210 W01 Prove: Developer
Camila Apai
"""
def main():
    print("Welcome to the Tic-Tac-Toe game!")
    board = create_board()
    player = next_player("")
    while True:
        show_board(board)
        select_square(player, board)
        player = next_player(player)
        if (win_game(board)):
            print("Good game. Thanks for playing!")
            break
            
def create_board():
    """Creates a list that contains the numbers of the board.

    Parameter filename: none.
    Return: board.
    """
    board = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    return board

def show_board(board):
    """Displays the board for the user to see.

    Parameter filename: board.
    Return: none.
    """
    print()
    print(f"{board[0]} | {board[1]} | {board[2]} | {board[3]}")
    print("-+-+-+-+-+-+-+-")
    print(f"{board[4]} | {board[5]} | {board[6]} | {board[7]}")
    print("-+-+-+-+-+-+-+-")
    print(f"{board[8]} | {board[9]}| {board[10]}| {board[11]}")
    print("-+-+-+-+-+-+-+-")
    print(f"{board[12]}| {board[13]}| {board[14]}| {board[15]}")
    print()

def next_player(player):
    """Determines who is going to be the next player.

    Parameter filename: player.
    Return: the player ("x" or "o").
    """
    if player == "x":
        return "o"
    else:
        return "x"

def select_square(player, board):
    """Ask the user for the place where they wanna place their mark, and and then place it.

    Parameter filename: player, board.
    Return: none.
    """
    choose_square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[choose_square - 1] = player

def win_game(board):
    """Shows the different movements to win/end the game.

    Parameter filename: board.
    Return: boolean variable.
    """
    if board[0] == board[1] == board[2] == board[3]:
        return True
    elif board[4] == board[5] == board[6] == board[7]:
        return True
    elif board[8] == board[9] == board[10] == board[11]:
        return True
    elif board[12] == board[13] == board[14] == board[15]:
        return True
    elif board[0] == board[4] == board[8] == board[12]:
        return True
    elif board[1] == board[5] == board[9] == board[13]:
        return True
    elif board[2] == board[6] == board[10] == board[14]:
     return True
    elif board[3] == board[7] == board[11] == board[15]:
     return True
    elif board[0] == board[5] == board[10] == board[15]:
     return True
    elif board[3] == board[6] == board[9] == board[12]:
     return True
    else:
        return False
    

if __name__ == "__main__":
    main()

    