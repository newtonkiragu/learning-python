import random

def drawBoard(board):
    '''
    function to print out the board place that was passed
    "board is a list of 10 strings representing the board. ignore 0"
    '''
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def chooseWhoToPlayAgainst():
    '''
    function to switch between a player playing against another player or against the computer
    lets the player type their name and which letter they want to be
    '''
    print('What should I call you?')
    player1UserName = input()
    print('Welcome ' + player1UserName + ',\nDo you want to play against your friend?')
    return input().lower().startswith('y')

def computerOrPlayer2():
    '''
    switches between player 2 and computer
    '''
    player2UserName = ''
    if chooseWhoToPlayAgainst == 'y':
        print('What should I call you?')
        player2UserName = input()
    else:
        player2UserName = 'computer'

    return player2UserName

def inputPlayerLetter():
    '''
    returns a list with the player\'s letter as first item and computer\'s or second player\'s as second item.
    '''
    letter = ''
    
    #check whether the letter that has been input is x or o
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

        #the first element in the list is the player's(player1) letter, the second is the computer's(player2) letter
        if letter == 'X':
            return['X','o']
        else:
            return['O','X']

def whoGoesFirst():
    '''
    randomly choose the player who goes first
    '''
    if random.randint(0,1) == 0:
        return 'player2'
    else:
        return 'player1'

def playAgain():
    '''
    returns True if the player wants to play again, otherwise it returns False
    '''
    print('Do you want to play again?(yes or no)')
    return input().lower().startswith('y')

def makeMove(board,letter,move):
    board[move] = letter

def isWinner(bo,le):
    '''
    Given a board and a player's letter, this function returns True if the player has won.
    Use bo and le so that you don\'t have to type much
    '''
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal(back slash)
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal(forward slash)

def getBoardCopy(board):
    '''
    make a duplicate of the board list and return it's duplicate
    '''
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board,move):
    '''
    return True if the passed move is free on the passed board
    '''
    return board[move] == ''

def getPlayerMove(board):
    '''
    let the player type in their move
    '''
    move = ''

    while move not in '123456789'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move?')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board,moveList):
    '''
    returns a valid move from the passed move on the list
    returns none if there is no valid move
    '''
    possibleMoves = []

    for i in moveList:
        if isSpaceFree(board,i): #check for free space
            possibleMoves.append(i) #add possible moves to list
    
    if len(possibleMoves) != 0: #check for any possible moves
        return random.choice(possibleMoves) #return possible moves randomly
    else:
        return None

def getComputerMove(board,player2Letter):
    '''
    given a board and a computer letter, determine where to move and return that move
    '''
    if player2Letter == 'X':
        player1Letter == 'O'
    else:
        player1Letter == 'X'

    # alogrithm for computer moves:
    # First, check if we can win in the next move
    for i in range(1, 10): #loop through the moves
        copy = getBoardCopy(board) #get a copy of the current state of the board
        if isSpaceFree(copy, i): #check whether there is a move that will make the computer win in a single move
            makeMove(copy, player2Letter, i) #try to make the move
            if isWinner(copy, player2Letter): #check whether that move will make the computer win
                return i #make the move to win the game

    # Check if the player could win on their next move, and block them.
    for i in range(1, 10): #loop through the moves
        copy = getBoardCopy(board) #get a copy of the current state of the board
        if isSpaceFree(copy, i): #check whether there is a move that will make the computer loose in a single move
            makeMove(copy, player1Letter, i) #try to make the move
            if isWinner(copy, player1Letter): #check whether that move will make the computer loose
                return i #make the move to block the player

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None: #check whether the moves the computer should make are taken
        return move #make the move to take one corner

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5): #check whether the center piece is taken
        return 5 #make move to take center piece

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    '''
    return True if every space on the board has been taken, otherwise return False
    '''
    for i in range(1,10): #loop throught the entire board
        if isSpaceFree(board, i): #check whether there is any space on the board
            return False #there is free space. The board is not full
    return True #there is no free space. The board is full

print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [''] * 10 #reset the board
    chooseWhoToPlayAgainst()
    player1UserName = chooseWhoToPlayAgainst().player1UserName()
    player2UserName = computerOrPlayer2()
    player2 = computerOrPlayer2()
    player1Letter, player2Letter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The' + turn + ' will go first')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player1':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, player1Letter, move)

            if isWinner(theBoard, player1Letter):
                drawBoard(theBoard)
                print('hooray. ' + player1UserName + 'has won the game')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie')
                    break
                else:
                    turn = 'player2'

        elif turn == 'player2' and player2 == player2UserName:
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, player2Letter, move)

            if isWinner(theBoard, player2Letter):
                drawBoard(theBoard)
                print('hooray. ' + player2UserName + 'has won the game')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie')
                    break
                else:
                    turn = 'player1'

        else:
            # Computer’s turn.
            move = getComputerMove(theBoard, player2Letter)
            makeMove(theBoard, player2Letter, move)

            if isWinner(theBoard, player2Letter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player1'

    if not playAgain():
        break