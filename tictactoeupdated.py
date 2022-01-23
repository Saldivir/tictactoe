#Tic-Tac-Toe assignment, 1/14 Spencer Gunn

from tkinter.messagebox import YES


GameBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in GameBoard:
    board_keys.append(key)


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# Now we'll write the main function which has all the gameplay functionality.
def main():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(GameBoard)
        print("It is " + turn + "'s move.  Where do you want to go?  Use the numpad and press enter when you're done.")

        move = input()        

        if GameBoard[move] == ' ':
            GameBoard[move] = turn
            count += 1
        else:
            print("That slot is filled.\nMove to which place?")
            continue

        # Has player x or o won?
        if count >= 5:
            # across
            if GameBoard['7'] == GameBoard['8'] == GameBoard['9'] != ' ': 
                printBoard(GameBoard)
                print("\nGame Over.\n")                
                print(turn + " won. Congratulations!")                
                break
            elif GameBoard['4'] == GameBoard['5'] == GameBoard['6'] != ' ': 
                printBoard(GameBoard)
                print("\nGame Over.\n")                
                print(turn + " won. Congratulations!")   
                break
            elif GameBoard['1'] == GameBoard['2'] == GameBoard['3'] != ' ': 
                printBoard(GameBoard)
                print("\nGame Over.\n")                
                print(turn + " won. Congratulations!")   
                break
            # down
            elif GameBoard['1'] == GameBoard['4'] == GameBoard['7'] != ' ': 
                printBoard(GameBoard)
                print("\nGame Over.\n")                
                print(turn + " won. Congratulations!")   
                break
            elif GameBoard['2'] == GameBoard['5'] == GameBoard['8'] != ' ': 
                printBoard(GameBoard)
                print("\nGame Over.\n")                
                print(turn + " won. Congratulations!")   
                break
            elif GameBoard['3'] == GameBoard['6'] == GameBoard['9'] != ' ': 
                printBoard(GameBoard)
                print("\nGame Over.\n")                
                print(turn + " won. Congratulations!")   
                break 
            # Diagonally
            elif GameBoard['7'] == GameBoard['5'] == GameBoard['3'] != ' ': 
                printBoard(GameBoard)
                print("\nGame Over.\n")                
                print(turn + " won. Congratulations!")   
                break
            elif GameBoard['1'] == GameBoard['5'] == GameBoard['9'] != ' ': 
                printBoard(GameBoard)
                print("\nGame Over.\n")                
                print(turn + " won. Congratulations!")   
                break 

        # Tie Game
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # changes the player after every move
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    restart = input("Do want to play Again?(y/n)")
    while restart == "y":
        for key in board_keys:
                GameBoard[key] = " "

        main()
    
if __name__ == "__main__":
    main()