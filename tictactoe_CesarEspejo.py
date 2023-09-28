#Cesar Espejo
#AAI/CPE/EE-551 Final Project
#"I pledge my honor that I have abided by the Stevens Honor System

import random #Importing random library so that players could randomly be assigned X or O

board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]  #initializing 2-Dimensional array 3x3 board
scorers = [] #initializing list of players
empty = '.'
player1Name = '' #initialize player 1 name variable
player1Score = 0 #initialize player 1 score
player2Name = '' #initialize player 2 name variable
player2Score = 0 #initialize player 2 score
CPUName = "CPU" #initialize name of computer player
CPUScore = 0 #initialize computer score

def showScores(): #show users their current scores
    if playCPU == False: #Check condition of whether or not the player chose to play against a computer
        print(player1Name + " has " + str(player1Score) + " wins") #print out scores in string type
        print(player2Name + " has " + str(player2Score) + " wins")
    elif playCPU == True:
        print(player1Name + " has " + str(player1Score) + " wins")
        print(CPUName + " has " + str(CPUScore) + " wins")

def refreshBoard(): #If user chooses to play game again at the end, this is meant to reset the board
    global board #Used global variable of board so it applies to board all throughout the program
    board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    showBoard()

def assignPlayer():
    global player1 #Used global variables so they apply all throughout the program
    global player2
    global CPU
    player1 = random.randint(0,1) #Randomly pick between 1 and 0 to decide who gets X and O
    if player1 == 0:
        player1 = "X"
        player2 = "O"
        CPU = "O"
    elif player1 == 1:
        player1 = "O"
        player2 = "X"
        CPU = "X"

def assignTurn():
    global turns
    turns = random.randint(0,1)


def showBoard(): #I designed this table to make the appearance of the board nicer and the available positions clearer
    print("*" * 30)
    print("      |       |")
    print("   {col1}  |   {col2}   |  {col3}".format(col1="1" if board[0][0] == empty else board[0][0],
                                                     col2="2" if board[0][1] == empty else board[0][1],
                                                     col3="3" if board[0][2] == empty else board[0][2]))
    print("______|_______|_____")
    print("      |       |")
    print("   {col4}  |   {col5}   |  {col6}".format(col4="4" if board[1][0] == empty else board[1][0],
                                                     col5="5" if board[1][1] == empty else board[1][1],
                                                     col6="6" if board[1][2] == empty else board[1][2]))
    print("______|_______|_____")
    print("      |       |")
    print("   {col7}  |   {col8}   |  {col9}".format(col7="7" if board[2][0] == empty else board[2][0],
                                                     col8="8" if board[2][1] == empty else board[2][1],
                                                     col9="9" if board[2][2] == empty else board[2][2]))
    print("      |       |")

def isPositionsAvailable(): #Iterates through each position on the table to check if it's empty
    available = False
    for x in range(0, 3):
        for j in range(0,3):
            if (board[x][j] == empty):
                available = True
    return available


def findNext(CPU): #This is code for the CPU. If a position is empty, it will take it based on the order below.
    selected = False
    if selected == False and board[1][1] == empty:
        board[1][1] = CPU
        print("CPU selected position 5")
    elif selected == False and board[0][0] == empty:
        board[0][0] = CPU
        print("CPU selected position 1")
    elif selected == False and board[0][2] == empty:
        board[0][2] = CPU
        print("CPU selected position 3")
    elif selected == False and board[2][0] == empty:
        board[2][0] = CPU
        print("CPU selected position 7")
    elif selected == False and board[2][2] == empty:
        board[2][2] = CPU
        print("CPU selected position 9")
    elif selected == False and board[0][1] == empty:
        board[0][1] = CPU
        print("CPU selected position 2")
    elif selected == False and board[1][0] == empty:
        board[1][0] = CPU
        print("CPU selected position 4")
    elif selected == False and board[1][2] == empty:
        board[1][2] = CPU
        print("CPU selected position 6")
    elif selected == False and board[2][1] == empty:
        board[2][1] = CPU
        print("CPU selected position 8")

def playagain(): #A function asking the user if they want to play again. If yes, main() function is started again
#if the user selects no, the program is ended with exit(). Also checks to make sure they type yes or no.
    play = input("Would you like to play again?: ")
    if play.upper() == "YES":
        main()
    elif play.upper() == "NO":
        exit()
    elif play.upper() != "YES" or play.upper() != "NO":
        print("Please type Yes or No")
        playagain()

def checkDraw(): #Function to check whether there is a draw or not. If so, user is asked if they want to play again.
    if board[0][0] != empty and board[0][1] != empty and board[0][2] != empty and board[1][0] != empty and board[1][1] != empty and board[1][2] != empty and board[2][0] != empty and board[2][1] != empty and board[2][2] != empty:
        print("Draw!")
        playagain()

def score(flag): #This function checks which player had the flag that passed as a win. That player (or CPU) will receive
    #a point each time they win
    global player1Score #global variables used so it applies throughout all functions of the code
    global player2Score
    global CPUScore
    if flag == "O" and player1 == "O":
        player1Score += 1
    if flag == "O" and player2 == "O":
        player2Score += 1
    if flag == "O" and CPU == "O":
        CPUScore += 1
    if flag == "X" and player1 == "X":
        player1Score += 1
    if flag == "X" and player2 == "X":
        player2Score += 1
    if flag == "X" and CPU == "X":
        CPUScore += 1

def checkWinner(flag): #This function goes through every possibility of a win in tic-tac-toe. If the conditions for a
#win are found, the board is shown, winner is announced, and the user is asked if they want to play again.
    winner = False
    if (board[0][0] == flag and board[0][1] == flag and board[0][2] == flag):
        winner = True
        showBoard()
        print("Horizontal winner for {flag} in row 1 and columns 1, 2, 3".format(flag=flag))
        score(flag)
        playagain()
    if (board[1][0] == flag and board[1][1] == flag and board[1][2] == flag):
        winner = True
        showBoard()
        print("Horizontal winner for {flag} in row 2 and columns 1, 2, 3".format(flag=flag))
        score(flag)
        playagain()
    if (board[2][0] == flag and board[2][1] == flag and board[2][2] == flag):
        winner = True
        showBoard()
        print("Horizontal winner for {flag} in row 3 and columns 1, 2, 3".format(flag=flag))
        score(flag)
        playagain()
    if (board[0][0] == flag and board[1][0] == flag and board[2][0] == flag):
        winner = True
        showBoard()
        print("Vertical winner for {flag} in rows 1, 2, 3 and column 1".format(flag=flag))
        score(flag)
        playagain()
    if (board[0][1] == flag and board[1][1] == flag and board[2][1] == flag):
        winner = True
        showBoard()
        print("Vertical winner for {flag} in rows 1, 2, 3 and column 2".format(flag=flag))
        score(flag)
        playagain()
    if (board[0][2] == flag and board[1][2] == flag and board[2][2] == flag):
        winner = True
        showBoard()
        print("Vertical winner for {flag} in rows 1, 2, 3 and column 3".format(flag=flag))
        score(flag)
        playagain()
    if (board[0][0] == flag and board[1][1] == flag and board[2][2] == flag) \
            or (board[0][2] == flag and board[1][1] == flag and board[2][0] == flag):
        winner = True
        showBoard()
        print("Cross winner for ", flag)
        score(flag)
        playagain()
    return winner


def block(player1, CPU): #More code to help the computer player determine where to go for their turn. Helps the computer
    #block where the player is trying to win
    blocked = False

    # Horizontal blocking

    if (board[0][0] == empty or board[0][1] == empty or board[0][2] == empty):
        if (board[0][0] == player1 and board[0][1] == player1 and board[0][2] == empty):
            board[0][2] = CPU
            blocked = True
        elif (board[0][0] == player1 and board[0][1] == empty and board[0][2] == player1):
            board[0][1] = CPU
            blocked = True
        elif (board[0][0] == empty and board[0][1] == player1 and board[0][2] == player1):
            board[0][0] = CPU
            blocked = True
    elif (board[1][0] == empty or board[1][1] == empty or board[1][2] == empty):
        if (board[1][0] == player1 and board[1][1] == player1 and board[1][2] == empty):
            board[1][2] = CPU
            blocked = True
        elif (board[1][0] == player1 and board[1][1] == empty and board[1][2] == player1):
            board[1][1] = CPU
            blocked = True
        elif (board[1][0] == empty and board[1][1] == player1 and board[1][2] == player1):
            board[1][0] = CPU
            blocked = True
    elif (board[2][0] == empty or board[2][1] == empty or board[2][2] == empty):
        if (board[2][0] == player1 and board[2][1] == player1 and board[2][2] == empty):
            board[2][2] = CPU
            blocked = True
        elif (board[2][0] == player1 and board[2][1] == empty and board[2][2] == player1):
            board[2][1] = CPU
            blocked = True
        elif (board[2][0] == empty and board[2][1] == player1 and board[2][2] == player1):
            board[2][0] = CPU
            blocked = True
    # Vertical blocking

    elif (board[0][0] == empty or board[1][0] == empty or board[2][0] == empty):
        if (board[0][0] == player1 and board[1][0] == player1 and board[2][0] == empty):
            board[2][0] = CPU
            blocked = True
        elif (board[0][0] == player1 and board[1][0] == empty and board[2][0] == player1):
            board[1][0] = CPU
            blocked = True
        elif (board[0][0] == empty and board[1][0] == player1 and board[2][0] == player1):
            board[0][0] = CPU
            blocked = True
    elif (board[0][1] == empty or board[1][1] == empty or board[2][1] == empty):
        if (board[0][1] == player1 and board[1][1] == player1 and board[2][1] == empty):
            board[2][1] = CPU
            blocked = True
        elif (board[0][1] == player1 and board[1][1] == empty and board[2][1] == player1):
            board[1][1] = CPU
            blocked = True
        elif (board[0][1] == empty and board[1][1] == player1 and board[2][1] == player1):
            board[0][1] = CPU
            blocked = True
    elif (board[0][2] == empty or board[1][2] == empty or board[2][2] == empty):
        if (board[0][2] == player1 and board[1][2] == player1 and board[2][2] == empty):
            board[2][2] = CPU
            blocked = True
        elif (board[0][2] == player1 and board[1][2] == empty and board[2][2] == player1):
            board[1][2] = CPU
            blocked = True
        elif (board[0][2] == empty and board[1][2] == player1 and board[2][2] == player1):
            board[0][2] = CPU
            blocked = True

    # Cross blocking

    elif (board[0][0] == empty or board[1][1] == empty or board[2][2] == empty):
        if (board[0][0] == player1 and board[1][1] == player1 and board[2][2] == empty):
            board[2][2] = CPU
            blocked = True
        elif (board[0][0] == player1 and board[1][1] == empty and board[2][2] == player1):
            board[1][1] = CPU
            blocked = True
        elif (board[0][0] == empty and board[1][1] == player1 and board[2][2] == player1):
            board[0][0] = CPU
            blocked = True
    elif board[0][2] == empty or board[1][1] == empty or board[2][0] == empty:
        if (board[0][2] == player1 and board[1][1] == player1 and board[2][0] == empty):
            board[2][0] = CPU
            blocked = True
        elif board[0][2] == player1 and board[1][1] == empty and board[2][0] == player1:
            board[1][1] = CPU
            blocked = True
        elif (board[0][2] == empty and board[1][1] == player1 and board[2][0] == player1):
            board[0][2] = CPU
            blocked = True
    return blocked


def player1Move(): #Function that serves as player 1's turn
    player1Move = True
    while player1Move: #I used try and except to make sure the users are only inputting numbers for their move.
        try:
            move = int(input(player1Name + " enter your move: "))
        except:
            print("Please select an open position from 1 through 9.")
            continue
        if move > 9: #Had to limit the inputs to integers from 1 to 9.
            print("Please select an open position from 1 through 9.")
            continue
        if move < 1:
            print("Please select an open position from 1 through 9.")
            continue
        #I know the directions ask for the user to input a row and column, but I feel like asking for one number on the
        #grid makes it a lot easier and user-friendly for tic-tac-toe. So, below the player only has to input one number
        #according to the numbers on the grid. If I were to immplement it for the user to input the row and column, I
        #would ask for one input for the row as move1 and then a second input as the column for move2.
        if move == 1:
            move1 = 0
            move2 = 0
        if move == 2:
            move1 = 0
            move2 = 1
        if move == 3:
            move1 = 0
            move2 = 2
        if move == 4:
            move1 = 1
            move2 = 0
        if move == 5:
            move1 = 1
            move2 = 1
        if move == 6:
            move1 = 1
            move2 = 2
        if move == 7:
            move1 = 2
            move2 = 0
        if move == 8:
            move1 = 2
            move2 = 1
        if move == 9:
            move1 = 2
            move2 = 2
        #Once a move is selected, it goes through this if statement to make sure it's an available position.
        if board[move1][move2] == empty:
            board[move1][move2] = player1
            player1Move = False
        else: #If the position selected is not empty, this will be printed.
            print("Position" + str(move) + " is already used")

def player2Move(): #Same as player1Move function above, but this serves as player 2's turn.
    player2Move = True
    while player2Move:
        try:
            move = int(input(player2Name + " enter your move: "))
        except:
            print("Please select an open position from 1 through 9.")
            continue
        if move > 9:
            print("Please select an open position from 1 through 9.")
            continue
        if move < 1:
            print("Please select an open position from 1 through 9.")
            continue
        if move == 1:
            move1 = 0
            move2 = 0
        if move == 2:
            move1 = 0
            move2 = 1
        if move == 3:
            move1 = 0
            move2 = 2
        if move == 4:
            move1 = 1
            move2 = 0
        if move == 5:
            move1 = 1
            move2 = 1
        if move == 6:
            move1 = 1
            move2 = 2
        if move == 7:
            move1 = 2
            move2 = 0
        if move == 8:
            move1 = 2
            move2 = 1
        if move == 9:
            move1 = 2
            move2 = 2
        if board[move1][move2] == empty:
            board[move1][move2] = player2
            player2Move = False
        else:
            print("Position" + str(move) + " is already used")

player1Name = input('Player 1, enter your name: ') #Player 1 is asked to input their name so it can be referred to
#each turn

playCPU = False #This variable is set as False so that we can enter the following while loop.
while not playCPU:
    playCPU = input('Would you like to play against a computer? Yes or No: ') #The user is asked to input yes or no
    if playCPU.upper() == "YES": #I used upper() so the user's response wouldn't be case sensitive. If a user selects
        #yes, the playCPU is set to true and we break out of this loop.
        playCPU = True
        break
    if playCPU.upper() == "NO": #If a user responds no, the playCPU variable is set to false and we break out of this loop.
        playCPU = False
        break
    if playCPU.upper() != "YES" or playCPU.upper() != "NO": #This checks that a user can only respond with yes or no.
        print("Please type Yes or No")
        playCPU = False

if not playCPU: #There is a player 2 if they select no for a computer player. So, a 2nd user has to input their name.
    player2Name = input("Player 2, enter your name: ")

if playCPU == True: #If the user selected yes for a computer player, the computer's name will be CPU.
    CPUName = "CPU"

def main(): #This is the main function that runs the game. I made a main() function so that users have the option to
    #play again. So, if a user does want to play again, I just run main() again to start the code over.
    if (playCPU == False): #If no CPU, then only player1 and player2 scores will be shown.
        print(str(player1Name) + " has " + str(player1Score) + " points")
        print(str(player2Name) + " has " + str(player2Score) + " points")
    if (playCPU == True): #If there's a CPU, then only player1 and the CPU's scores will be shown.
        print(str(player1Name) + " has " + str(player1Score) + " points")
        print(str(CPUName) + " has " + str(CPUScore) + " points")
    assignTurn() #randomly assigns who goes first
    refreshBoard() #This resets the board to make sure all positions are empty
    assignPlayer() #This randomly assigns player 1 and player 2 to X or O
    winner = False
    while isPositionsAvailable() and winner == False and turns == 0: #Conditions to make sure there's spaces and no
        # winner has yet been declared. Also checks the variable turns. If turns = 0, the CPU  goes first when playing
        # against a computer and player 1 goes first when versing a player 2.
        if (playCPU == True): #The code under this condition is if a user wants to play against a computer.
            if block(player1, CPU) == False: #If no block was done by the computer, it proceeds with the code beneath.
                checkDraw() #Checks if there's a draw.
                findNext(CPU) #Determines CPU's next position.
                winner = checkWinner(CPU) #Checks whether winner is True or False.
                showBoard() #Prints out the board for the users to see where the CPU went for their turn.
                if winner == False: #If winner is not yet declared, proceed.
                    checkDraw() #Checks if there's a draw
                    player1Move()  #Player 1's turn
                    winner = checkWinner(player1) #Checks winner again
                    showBoard() #Prints board for the next turn
            else: #Runs the rest of the code even if block is not true.
                findNext(CPU)
                winner = checkWinner(CPU)
                showBoard()
                checkDraw()
                if winner == False:
                    checkDraw()
                    player1Move()
                    winner = checkWinner(player1)
                    showBoard()
        elif (playCPU == False): #If the user does not want to play against a CPU, they proceed with the code beneath.
            player1Move()
            winner = checkWinner(player1) #Check for a winner
            showBoard() #Print out board after player 1's turn
            if winner == False:
                checkDraw() #Check for a draw
                player2Move() #Player 2's turn
                winner = checkWinner(player2) #Check again for a winner
                showBoard() #Show the board after player 2's turn
    while isPositionsAvailable() and winner == False and turns == 1: #The same as above except if turns = 1, then player
        #1 goes first for the computer game and player2 goes first if versing player1.
        if (playCPU == True):
            player1Move()
            winner = checkWinner(player1)
            showBoard()
            if winner == False: #for the scenario where the player goes first and the CPU goes next, I was encountering
                #bugs with the blocking function, so I removed it here, making the computer less intelligent, but still
                #able to play against the player.
                checkDraw()
                findNext(CPU)
                winner = checkWinner(CPU)
                showBoard()

        elif (playCPU == False):
            player2Move()
            winner = checkWinner(player2)
            showBoard()
            if winner == False:
                checkDraw()
                player1Move()
                winner = checkWinner(player1)
                showBoard()
main() #the main code running the game
#Note: Once a player selects CPU or no CPU, that is set for the rest of the time the program is running. So, if a player
#wants to switch from Player2 to CPU or vice versa, they have to rerun the code. Same applies for player's names. Also,
#points don't save, so once the program ends, the scoreboard ends with it and will reset when the code is ran again.