def player_input():
    
    player1marker = None
    player2marker = None
 
    while player1marker != 'X' and player1marker != 'O':
        player1marker = str(input('Player 1, select X or O as your marker.')).upper()
        if player1marker == 'X':
            player1marker = 'X'
            player2marker  = 'O'
        elif player1marker == 'O':
            player1marker = 'O'
            player2marker = 'X'
        else:
            print('This is not a valid option. Pick again')

    print('Player 1 will be ' + player1marker + ' and Player 2 will be ' + player2marker)

    return(player1marker, player2marker)


import random

def choose_first():
    
    output = random.randint(1, 2)
    goingFirst = None
    goingSecond = None
    
    if output == 1:
        goingFirst = 'Player 1'
        goingSecond = 'Player 2'
    else:
        goingFirst = 'Player 2'
        goingSecond = 'Player 1'
    
    print(goingFirst + " will go first!")
    return (goingFirst, goingSecond)


def space_check(board, position):
    
    if board[position] == ' ':
        return True
    return False


def player_choice(board):
    
    while True:
        nextPosition = int(input('Please input a position from number 0 to 8'))
        if nextPosition not in range(0, 9):
            print('This is not a valid input. Please pick again')
        elif space_check(board, nextPosition) == False:
            print('This spot is already taken. Please pick another one.')
        else:
            return nextPosition
        



def place_marker(board, marker, nextPosition):
    board[nextPosition] = marker
    


def display_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print('\n'*20)


def win_check(board, mark):

    if (board[0] == mark and board[1] == mark and board[2] == mark) or (board[3] == mark and board[4] == mark and board[5] == mark) or (board[6] == mark and board[7] == mark and board[8] == mark) or (board[0] == mark and board[3] == mark and board[6] == mark) or (board[1] == mark and board[4] == mark and board[7] == mark) or (board[2] == mark and board[5] == mark and board[8] == mark) or (board[0] == mark and board[4] == mark and board[8] == mark) or (board[2] == mark and board[4] == mark and board[6] == mark):
        return True
    return False

def full_board_check(board):
    
    for i in board:
        if i == ' ':
            return False
    return True



def replay():
    
    while True:
        playAgain = str(input('Would you like to play again (Y/N)')).upper()
        
        if playAgain == 'Y':
            return True
        elif playAgain == 'N':
            return False
        else:
            print('This is not a valid option. Please pick again')

    False


#Game start
    

print('Welcome to Tic Tac Toe!')

while True:
    
    game_on = True #turning the game on

    while game_on:

        board = [' ',' ',' ',' ',' ',' ',' ',' ',' '] # setting the board       
        p1mark, p2mark = player_input() # player 1 selects mark, and player 2 gets mark (variables are either X or O)
        first, second = choose_first() # randomizer chooses who goes first, stores it into respective variables (variable have string of Player 1 or 2)
        activeMarker = None

        if first == 'Player 1': # setting which player is the active one (i.e. whoever's turn it is)
            activeMarker = p1mark
        else:
            activeMarker = p2mark

        while True: 
            
            spot = player_choice(board) # this asks a player for the next position and returns an integer
            place_marker(board, activeMarker, spot) # intakes board, marker, position and updates board
            display_board(board)
            reset = None
            
            if full_board_check(board) == True: # check if board is full, asks if the games wants to be played again
                print('The board is full. There are no more moves left')
                
                reset = replay()
                if reset:
                    print('Let''s go again')
                    break
                else:
                    print('Thank you for playing!')
                    break
                
            elif win_check(board, activeMarker):  # check if active marker has won, asks if game wants to be played again
                if activeMarker == p1mark:
                    print('Player 1 has won!')
                else:
                    print('Player 2 has won!')
                
                reset = replay()
                if reset:
                    print('Let''s go again')
                    break
                else:
                    print('Thank you for playing!')
                    break

            # switch the marker after each turn
            if activeMarker == p1mark:
                activeMarker = p2mark
            else:
                activeMarker = p1mark
    
        game_on = False

    break
