board = ['_' for x in range(9)]

def print_board():

    print('|' + board[0] + ' ' + board[1] + ' ' + board[2] + '|'+ '\n' )
    print('|' + board[3] + ' ' + board[4] + ' ' + board[5] + '|'+ '\n' )
    print('|' + board[6] + ' ' + board[7] + ' ' + board[8] + '|'+ '\n' )

def check_board():
    
    #check horizontal
    if ((board[0] == 'x' and board[1] == 'x' and board[2] == 'x')
        or (board[3] == 'x' and board[4] == 'x' and board[5] == 'x') 
        or (board[6] == 'x' and board[7] == 'x' and board[8] == 'x')
        or (board[0] == 'o' and board[1] == 'o' and board[2] == 'o')
        or (board[3] == 'o' and board[4] == 'o' and board[5] == 'o') 
        or (board[6] == 'o' and board[7] == 'o' and board[8] == 'o')
        ):
        return True
    else:
        #check diagonal
        if ((board[0] == 'x' and board[4] == 'x' and board[8] == 'x')
            or (board[2] == 'x' and board[4] == 'x' and board[6] == 'x') 
            or (board[0] == 'o' and board[4] == 'o' and board[8] == 'o')
            or (board[2] == 'o' and board[4] == 'o' and board[6] == 'o') 
            ):
            return True
        else:
                #check vertical
                if ((board[0] == 'x' and board[3] == 'x' and board[6] == 'x')
                    or (board[1] == 'x' and board[4] == 'x' and board[7] == 'x') 
                    or (board[2] == 'x' and board[5] == 'x' and board[8] == 'x')
                    or (board[0] == 'o' and board[3] == 'o' and board[6] == 'o')
                    or (board[1] == 'o' and board[4] == 'o' and board[7] == 'o') 
                    or (board[2] == 'o' and board[5] == 'o' and board[8] == 'o')
                    ):
                    return True
                else:
                    if (board[0] != '_' and board[1] != '_' and board[2] != '_'
                        and board[3] != '_' and board[4] != '_' and board[5] != '_' 
                        and board[6]!= '_' and board[7] != '_' and board[8] != '_'):
                        return True
                    else:
                        return False

def check_tie():
    if (board[0] != '_' and board[1] != '_' and board[2] != '_'
                        and board[3] != '_' and board[4] != '_' and board[5] != '_' 
                        and board[6]!= '_' and board[7] != '_' and board[8] != '_'):
                        return True
    else: 
        return False


def check_move(move):
    if (move < 0 or move > 9):
        print('Invalid Input Please Insert a number 1 - 9')
        return False
    elif(board[move-1] != '_'):
        print('Invalid Move Please Try Again')
        return False
    else: 
        return True
    
        

# user input
while not check_board():
    
    for i in range(2):
        print_board()
        if (i == 0):
            while(True):
                move = int (input('Player 1: Please input a place number 1 - 9: '))
                if (check_move(move)):
                    break
            
            board[move - 1] = 'x'
            check_board()
            if (check_board() == True):
                print_board()
                if (check_tie):
                    print('Tie')
                    break
                else:
                    print('Player 1 wins!')
                    break
                    
        elif (i == 1):
            while(True):
                move = int (input('Player 2: Please input a place number 1 - 9: '))
                if (check_move(move)):
                    break
     
            board[move - 1] = 'o'
            check_board()
            if (check_board() == True):
                print_board()
                if (check_tie):
                    print('Tie')
                    break
                else:
                    print('Player 2 wins!')
                    break
              