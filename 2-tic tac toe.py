import random
import colorama
from colorama import Fore
colorama.init(autoreset=True)

game_list = [['_', '_', '_'],
             ['_', '_', '_'],
             ['_', '_', '_']]

def get_cell():
    row = int(input('pls enter row: '))
    col = int(input('pls enter column: '))
    return row,col

def show_cell():
    for i in range(3):
        for j in range(3):
            print(game_list[i][j],end=' ')
        print()

def check():
    if game_list[0][0] == 'X' and game_list[0][1] == 'X' and game_list[0][2] == 'X' :
        print('Player 1 Wins')
        exit()

    elif game_list[0][0] == 'O' and game_list[0][1] == 'O' and game_list[0][2] == 'O' :
        print('Player 2 Wins')
        exit()

    elif game_list[1][0] == 'X' and game_list[1][1] == 'X' and game_list[1][2] == 'X' :
        print('Player 1 Wins')
        exit()
    
    elif game_list[1][0] == 'O' and game_list[1][1] == 'O' and game_list[1][2] == 'O':
        print('Player 2 Wins')
        exit()

    elif game_list[2][0] == 'X' and game_list[2][1] == 'X' and game_list[2][2] == 'X':
        print('Player 1 Wins')
        exit()
    
    elif game_list[2][0] == 'O' and game_list[2][1] == 'O' and game_list[2][2] == 'O':
        print('Player 2 Wins')
        exit()

    elif game_list[0][0] == 'X' and game_list[1][0] == 'X' and game_list[2][0] == 'X':
        print('Player 1 Wins')
        exit()

    elif game_list[0][0] == 'O' and game_list[1][0] == 'O' and game_list[2][0] == 'O':
        print('Player 2 Wins')
        exit()

    elif game_list[0][1] == 'X' and game_list[1][1] == 'X' and game_list[2][1] == 'X':
        print('Player 1 Wins')
        exit()

    elif game_list[0][1] == 'O' and game_list[1][1] == 'O' and game_list[2][1] == 'O':
        print('Player 2 Wins')
        exit()

    elif game_list[0][2] == 'X' and game_list[1][2] == 'X' and game_list[2][2] == 'X':
        print('Player 1 Wins')
        exit()

    elif game_list[0][2] == 'O' and game_list[1][2] == 'O' and game_list[2][2] == 'O':
        print('Player 2 Wins')
        exit()

    elif game_list[0][0] == 'X' and game_list[1][1] == 'X' and game_list[2][2] == 'X':
        print('Player 1 Wins')
        exit()

    elif game_list[0][0] == 'O' and game_list[1][1] == 'O' and game_list[2][2] == 'O':
        print('Player 2 Wins')
        exit()

    elif game_list[0][2] == 'X' and game_list[1][1] == 'X' and game_list[2][0] == 'X':
        print('Player 1 Wins')
        exit()

    elif game_list[0][2] == 'O' and game_list[1][1] == 'O' and game_list[2][0] == 'O':
        print('Player 2 Wins')
        exit()





x = int(input('If you want play solo enter \'1\' or If you want play with a player enter \'2\': '))

while True:
    if x == 1 :
        check()
        print('Player 1:')
        
        while True :
            p1_row , p1_col = get_cell()
            if 0 <= p1_row <= 2 and 0 <= p1_col <= 2:
                if game_list[p1_row][p1_col] == '_':
                    game_list[p1_row][p1_col] = Fore.BLUE + 'X'
                    show_cell()
                    check()
                    break
                else:
                    print('This cell is full, pls enter another cell !!!')

        print('Player 2:')
        
        while True:
            rand_row = random.randint(0,2)
            rand_col = random.randint(0,2)
            if 0 <= rand_row <= 2 and 0 <= rand_col <= 2:
                if game_list[rand_row][rand_col] == '_':
                    game_list[rand_row][rand_col] = Fore.RED + 'O'
                    show_cell()
                    check()
                    break
    
    elif x == 2:
        check()
        print('Player 1:')
        
        while True :
            
            p1_row , p1_col = get_cell()

            if 0 <= p1_row <= 2 and 0 <= p1_col <= 2:
                
                if game_list[p1_row][p1_col] == '_':
                    game_list[p1_row][p1_col] = Fore.BLUE + 'X'
                    show_cell()
                    check()
                    break
                else:
                    print('This cell is full, pls enter another cell !!!')

        print('Player 2:')

        while True :
            
            p2_row , p2_col = get_cell()

            if 0 <= p2_row <= 2 and 0 <= p2_col <= 2:
                if game_list[p2_row][p2_col] == '_':
                    game_list[p2_row][p2_col] = Fore.RED + 'O'
                    show_cell()
                    check()
                    break
                else:
                    print('This cell is full, pls enter another cell !!!')