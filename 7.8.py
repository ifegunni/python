# Create a class TicTacToe that will enable you to write a complete program to play the
# game of tic-tac-toe. The class contains a 3-by-3 double-subscripted list of letters. The constructor
# should initialize the empty board to all zeros. Allow two human players. Wherever the first player
# moves, place an "X" in the specified square; place an "O" wherever the second player moves. Each
# move must be to an empty square. After each move, determine whether the game has been won and
# whether the game is a draw. [Note: If you feel ambitious, modify your program so that the computer
# makes the moves for one of the players automatically. Also, allow the player to choose whether to go
# first or second.]


board =["-","-","-",
        "-","-","-",
        "-","-","-"]

#If game is still going
gameStillGoing = True


#who won? or tie?
winner = None

#whose turn is it
currentPlayer = "X"

def displayBoard():

    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def playGame():

    #display initial board
    displayBoard()

    while gameStillGoing:

        #handle a single turn of an arbituary player
        handleTurn(currentPlayer)

        #check if the has been ended
        checkIfGameOver()

        #flip to the other player
        flipPlayer()

    #The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


#handle a single turn of an arbituary player
def handleTurn(player):

    print(player + "'s turn.'")
    position  = input("Choose a positon from 1-9: ")

    valid = False
    while not valid:
        while position not in ["1","2", "3", "4", "5","6","7","8","9"]:
            position = input("Invalid Input: Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    board[position] = player

    displayBoard()

def checkIfGameOver():
    checkForWinner()
    checkIfTie()


def checkForWinner():

    #set global variable
    global winner

    #checkRows
    rowWinner = checkRows()
    #CheckColumns
    columnWinner = CheckColumns()
    #checkdiagonals
    diagonalWinner = checkDiagonals()

    if rowWinner:
        #there was a winner
        winner = rowWinner
    elif columnWinner:
        #there was a winner
        winner = columnWinner
    elif diagonalWinner:
        #there was a winner
        winner = diagonalWinner
    else:
        #there was no winnner
        winner = None
    return winner

def checkRows():
    global gameStillGoing

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    #if any of the rows does match, flag that is a win
    if row_1 or row_2 or row_3:
        gameStillGoing = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def CheckColumns():
    global gameStillGoing

    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    #if any of the column does match, flag that is a win
    if col_1 or col_2 or col_3:
        gameStillGoing = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return


def checkDiagonals():
    global gameStillGoing

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    #if any of the diagonal does match, flag that is a win
    if diagonal_1 or diagonal_2:
        gameStillGoing = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return


def checkIfTie():

    global gameStillGoing
    if  "-" not in board:
        gameStillGoing = False
    return

def flipPlayer():

    global currentPlayer

    #if current player was x change to O and vice versa
    if currentPlayer == "X":
        currentPlayer = "O"
    elif currentPlayer == "O":
        currentPlayer = "X"

    return
playGame()



#board
#display board
#play game
#handle turn
#check win
    # check row
    # check column
    # check diagonal
#check if tie
#flip player
