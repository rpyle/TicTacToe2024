import random
team_name = 'Mustafa'
strategy_name = 'Center then next Open random corrner then next oepn'
strategy_description = 'Play center if available, then random open corrner then next open spot.'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

def move(player, board, score):
    print()
    print(player, score)
    print_board(board)
  
    r = random.randint(0, 2)
    c = random.randint(0, 2)
    
    while board[r][c] != ' ':
        r = random.randint(0, 2)
        c = random.randint(0, 2)
    
    if board[1][1] == ' ':
        r = 1
        c = 1
    elif board[0][0] == ' ':
        r = 0
        c = 0
    elif board[0][2] == ' ':
        r = 0
        c = 2
    elif board[2][0] == ' ':
        r = 2
        c = 0
    elif board[2][2] == ' ':
        r = 2
        c = 2
    else:
        r = 0
        c = 1
    print(r, c)
    return r, c