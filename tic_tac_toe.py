''' Create the board using the dictionary with the keys location from left to right. The values will change
according to the players moves. '''

theBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

board_keys = []


for key in theBoard:
    board_keys.append(key)

''' 
Write a function to check whether the board is filled or not.
'''

def printBoard(board):
    print()
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

# Now we'll write the main function which has all the gameplay functionality.
def game():

    turn = 'X'
    count = 0

#Iterate over the board and return false if the board contains an empty sign or else return true.

    for i in range(10):
        printBoard(theBoard)
        print("\nUse the keys between 1 and 9 to play, fill in any of the blank spaces.")
        print( turn + "'s turn to choose a square (1-9): ")

        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nChoose a different place.")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** 😁. Yaaaas!!! " +turn + " won. ****\n")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** 😁. Yaaaas!!! " +turn + " won. ****\n")
                break
            elif theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** 😁. Yaaaas!!! " +turn + " won. ****\n")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** 😁. Yaaaas!!! " +turn + " won. ****\n")
                break
            elif theBoard['8'] == theBoard['5'] == theBoard['2'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** 😁. Yaaaas!!! " +turn + " won. ****\n")
                break
            elif theBoard['9'] == theBoard['6'] == theBoard['3'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** 😁. Yaaaas!!! " +turn + " won. ****\n")
                break 
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** 😁. Yaaaas!!! " +turn + " won. ****\n")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** 😁. Yaaaas!!! " +turn + " won. ****\n")
                break 

        # If neither X nor O wins and the board is full, that is a tie.
        if count == 9:
            print("\nGame Over.\n")                
            print("😔. It's a Tie!!\n")

        # Shift the players after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Ask the player if he/she wants to restart the game.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y"  or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "

        game()

if __name__ == "__main__":
    game()