"""TickerTacker: A Chatbot TicTacToe - Ria Thompson Cogs 18 SP2019


For the purposes of this assignment, I wanted to code a classic paper-and-pencil game to be played via chatbot, so I created an interactive game of Tic Tac Toe.  Typically, this game is played between 2 people, one that is 'X' and the other 'O', where the objective is for a player to place 3 marks in a row either vertically, horizontally, or diagonally, thus winning the game.  If neither player is able to do this, the game ends in a draw. 

When playing with a chatbot, however, the user's opponent is a simple artificial intelligence such as the one written in the code below, named TickerTacker.  The user plays first as 'X, and then waits for TickerTacker to complete the first move or completes the first move him/herself.  The game continues alternating between the user and the chatbot until either player has won or until the game ends in a draw.  TickerTacker will then ask if the user wants to play again, at which point he/she can decide he wants to continue, or exit the game.

#### Process
- When writing my code, I found an incredibly helpful diagram (cited below) that helped me pseudocode it initially, to make sure I took into account all the steps of the game, such as asking if the player wants to play again, checking to see if a player won, etc.
- After that, I was able to work module by module to build a simple, minimal viable product before adding elements to make the chatbot more human as well, adding to the complexity of the board to mimic a real board, etc.

#### Citations
- Pseudocode outline: https://inventwithpython.com/chapter10.html
- isDigit info: https://www.programiz.com/python-programming/methods/string/isdigit
- Cogs 18 (Ellis) Lectures: https://cogs18.github.io/intro/ """

#Importing Random
import random

#Board structure inspired by the one cited above
def draw_board(board):
    
    print(' --- --- ---')
    print('| '+ board[1] + ' | ' + board[2] + ' | ' + board[3] + ' |')
    print(' --- --- ---')
    print('| '+ board[4] + ' | ' + board[5] + ' | ' + board[6] + ' |')
    print(' --- --- ---') 
    print('| '+ board[7] + ' | ' + board[8] + ' | ' + board[9] + ' |')
    print(' --- --- ---')


#Checking to see if there is a row on the board
#Code help from source cited above
def check_winner(board, ltr):
    
    #Defines possible rows that must be completed to win
    rows = [(7, 8, 9), (4, 5, 6), (1, 2, 3), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    
    #Checking possible horizontal/vertical/diagonal row
    for row in rows:
        if board[row[0]] == ltr and board[row[1]] == ltr and board[row[2]] == ltr:
            return True
    return False

#Checks to see if board is full
#Returns boolean
def full_board(board):
    
    return board.count(' ') <= 1

#Get player move from input
def user_move(board):
    
    move = input("Please choose an open spot from 1 to 9!")
    
    while not move.isdigit() or int(move) <= 0 or int(move) >= 10 or board[int(move)] != ' ':
        move = input("Please type a valid number from 1 to 9.")
    move = int(move)
    board[move] = 'X'
    return move 

#Function for chatbot
def chatbot_move(board):
    
    i = 1
    next_move = []
    for letter in board[1:]:
        if letter == ' ':
            next_move.append(i)
        i += 1
    if next_move:
        return random.choice(next_move)
    return 0

#Function for main "TickerTacker" chatbot 
def ticker_tacker(board):
    print("Let's Play!")
    print("My name's TickerTacker.")
    print("I'll be your opponent today in Tic Tac Toe!")
    print("Here's a look at the board we'll be playing with.")
    print(' --- --- ---')
    print('| '+ '1' + ' | ' + '2' + ' | ' + '3' + ' |')
    print(' --- --- ---')
    print('| '+ '4' + ' | ' + '5' + ' | ' + '6' + ' |')
    print(' --- --- ---') 
    print('| '+ '7' + ' | ' + '8' + ' | ' + '9' + ' |')
    print(' --- --- ---')
    print("Note: the spaces are labeled by the numbers on the board, so when you know what space you want to play, go ahead and type that number.")
    print("------------")
    print("Now go ahead and choose your first space...")
    draw_board(board)
    
    #Placing user move on board if there isn't a winner
    while not full_board(board):
        if not check_winner(board, 'O'):
            user_move(board)
            draw_board(board)
        #Ending game with TickerTacker win if board is full
        else:
            print('Looks like I won this time!')
            print('-----------------------------------')
            return
        
        #Placing chatbot move on board if there is a tie/isn't a winner
        if not check_winner(board, 'X'):
            move = chatbot_move(board)
            #Ending game with a tie
            if move == 0:
                print('Looks like we tied.')
                print('-----------------------------------')
                return
            #Placing chatbot move on board if there isn't a winner
            else:
                board[move] = 'O'
                print('TickerTacker placed an "O" in', move , ':')
                draw_board(board)
        #User move wins game
        else:
            print('Shucks...Looks like you won. Good job!')
            print('-----------------------------------')
            return
    #Print board in tie
    if full_board(board):
        print('Looks like we tied.')
        print('-----------------------------------')

#Starting and continuing the game
def play():
    
    play_again = "y"
    while True:
        if play_again.lower() == 'y' or play_again.lower == 'yes':
            board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            print('-----------------------------------')
            ticker_tacker(board)
        elif play_again.lower() == 'n' or play_again.lower == 'no':
            print("Thanks for playing! Come back soon :-)")
            break
        else:
            print("Please type y or n :~)")
        play_again = input("Do you want to play again? Y or N: ")
        
play()