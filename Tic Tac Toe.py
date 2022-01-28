from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[0]+'|'+board[1]+'|'+board[2])
    print('-|-|-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-|-|-')
    print(board[6] + '|' + board[7] + '|' + board[8])


def Player_choice():

    choice= ''
    while choice!='X' and choice!='O':
        choice=input('What is the First Player choice X or O')

    player1=choice

    if choice=='X':
        player2='O'
    if choice=='O':
        player2='X'
    return player1,player2

def placing(board):
    globals()
    for i in range(50):
        x=int(input('Turn of Player1'))
        board[x]='X'
        y =int(input('Turn of Player2'))
        board[y] = 'O'

