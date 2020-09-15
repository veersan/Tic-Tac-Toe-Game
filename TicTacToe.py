from IPython.display import clear_output


# display dashboard


def display_board(board):
    clear_output()
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')


# choose the player choice between 0 and x
def userInput(board):
    # test_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    symbols = ['0', 'x']
    while True:
        inpt1 = input('Please select your Symbol from 0 or x:')
        if inpt1 in symbols:
            if inpt1 == 'x':
                player1 = 'x'
                player2 = '0'
                break
            else:
                player1 = '0'
                player2 = 'x'
                break
        else:
            print('Invalid input. Please choose between 0 or x')

    board_update(board, player1, player2)


# To take input from the users
def board_update(board, player1, player2):
    dummy = 0
    count = 0
    print(f'{player1}-{player2}')
    while True:
        inpt = int(input('please select the index position for your value:'))
        if inpt in range(1, 10):
            if board[inpt - 1] == ' ':
                if dummy == 0:
                    board[inpt - 1] = player1
                    dummy = 1
                    count += 1

                else:
                    board[inpt - 1] = player2
                    dummy = 0
                    count += 1
            else:
                print('That index is already occupied.Please try another one.!!')
        else:
            print('Index is out of range. Please select between 1-9.')
        display_board(board)
        check_winner(board, player1, player2, count)


# To check the winner of the Game
def check_winner(test_board, player1, player2, count):
    if test_board[0] == test_board[1] == test_board[2] == 'x' or \
            test_board[3] == test_board[4] == test_board[5] == 'x' or \
            test_board[6] == test_board[7] == test_board[8] == 'x' or \
            test_board[0] == test_board[4] == test_board[8] == 'x' or \
            test_board[2] == test_board[4] == test_board[6] == 'x' or \
            test_board[0] == test_board[3] == test_board[6] == 'x' or \
            test_board[1] == test_board[4] == test_board[7] == 'x' or \
            test_board[2] == test_board[5] == test_board[8] == 'x':
        if player1 == 'x':
            print('Yippiieee!. Player1 won the match')
        else:
            print('Player2 won the game')

        replay_game()

    elif test_board[0] == test_board[1] == test_board[2] == '0' or \
            test_board[3] == test_board[4] == test_board[5] == '0' or \
            test_board[6] == test_board[7] == test_board[8] == '0' or \
            test_board[0] == test_board[4] == test_board[8] == '0' or \
            test_board[2] == test_board[4] == test_board[6] == '0' or \
            test_board[0] == test_board[3] == test_board[6] == '0' or \
            test_board[1] == test_board[4] == test_board[7] == '0' or \
            test_board[2] == test_board[5] == test_board[8] == '0':
        if player2 == 'x':
            print('Yippiieee!. Player2 won the match')
        else:
            print('Player1 won the game')

        replay_game()
    else:
        if count != 9:
            return
        else:
            print('Ooops! Game over. No one won the game. Better Luck next Time.')
            replay_game()


# Taking user choice whether to play the game again or not
def replay_game():
    r_game = ['Y', 'y', 'N', 'n']
    while True:
        user_choice = input('Do you want to play the game again:')
        if user_choice in r_game:
            if user_choice == 'Y' or user_choice == 'y':
                new_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                display_board(new_board)
                userInput(new_board)
            else:
                print('Thanks for playing the Game. See you soon !!!!')
                exit()
        else:
            print("Invalid input. PLease try again")


# Main method to invoke the program
if __name__ == "__main__":
    t_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    display_board(t_board)
    userInput(t_board)
