#Zain Kergaye
#Mr. Webster
#Programming 2

#Hours wasted: 0.1

#To DO:
#1. Create a class that makes an array 
#2. Get user input for the array
#3. Check if number is 1 or 0 
#5. give user feedback
#6. If number is 3 then say that they already hit that spot
#7. end game when they hit everything

from random import randint

def menu():
    print('Welcome to BattleShip!')
    print('')
    print('1. Play BattleShip')
    print('2. View scores')
    print('3. Exit game')
    print('')



board = []



#Function for printing the board:
def print_board(board):
    print('\n')
    print("Battle Field")
    print('')
    for row in board:
        print (" ".join(row))

def random_row(board):
    return randint(0,len(board) - 1)

def random_col(board):
    return randint(0,len(board[0]) - 1)



loop = 0

while (loop != 1):

    menu()
    menuInput = int(input('Enter selection 1-3: '))
    if(menuInput == 3):
        break
    if (menuInput == 2):
        print('This section has not been coded yet')
        #Put new things here
    if(menuInput == 1):
        board.clear()
        for x in range(5):
            board.append(["0"] * 5)
        
        ship_row = random_row(board)
        ship_col = random_col(board)

        gamedone = 1
        while gamedone == 1:
            print_board(board)
            print("\n")
            guess_row = int(input("Guess row: "))
            guess_col = int(input("Guess col: "))
            print('\n')

            if (guess_row == ship_row & guess_col == ship_col):
                print("You win!")
                break

            else:
                if(guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                    print("That's not in the board")
                    #print_board(board)
                elif(board[guess_row][guess_col] == 'X'):
                    print('Already hit')
                    #print_board(board)
                else:
                    print('miss')
                    board[guess_row][guess_col] = 'X'
                    #print_board(board)