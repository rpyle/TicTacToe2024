team_name = 'carter'
strategy_name = 'Block'
strategy_description = 'Block 3 of a kind if possible, if not then next open spot'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

def move(player, board, score):
  r = 0
  c = 0

  if board[0][0] != '' and board[0][1] != '' or board[0][1] != '' and board[0][2] != '' or board[0][0] != '' and board[0][2] != ''and not board[0][0] != '' and board[0][1] != '' and board[0][2] != '':
    while board[r][c] != ' ':
      c = c + 1
      if c > 2:
        c = 0
        r = r + 1
          
        
  elif board[1][0] != ' ' and board[1][1] != '' or board[1][1] != '' and board[1][2] != '' or board[1][0] != '' and board[1][2] != '' and not board[1][0] != '' and board[1][1] != '' and board[1][2] != '':

    r = 1

    while board[r][c] != ' ':
      c = c + 1
      if c > 2:
        c = 0
        r = r + 1
        
       
      
  elif board[2][0] != '' and board[2][1] != '' or board[2][1] != '' and board[2][2] != '' or board[2][0] != '' and board[2][2] != '' and not board[2][0] != '' and board[2][1] != '' and board[2][2] != '':

    r = 2

    while board[r][c] != ' ':
      c = c + 1
      if c > 2:
        c = 0
        r = r + 1
        
  elif board[0][0] != '' and board[2][2] != '' or board[0][0] != '' and board[1][1] != '' or board[1][1] != '' and board[2][2] != '' and not board[0][0] != '' and board[1][1] != '' and board[2][2] != '':
    if  board[0][0] != '' and board[2][2] != '':
      r = 1
      c = 1
    elif board[0][0] != '' and board[1][1] != '' or board[1][1] != '' and board[2][2] != '':
      c = 0
      r = 0
      while board[r][c] != ' ':
        r = r - 1
        if r < 0:
          r = 2
          c = c + 2
       
  elif board[0][2] != '' and board[1][1] != '' or board[0][2] != '' and board[2][0] != '' or board[1][1] != '' and board[2][0] != '' and not board[0][2] != '' and board[0][1] != '' and board[2][0] != '':
    if  board[0][2] != '' and board[2][0] != '':
      r = 1
      c = 1
    elif board[0][2] != '' and board[1][1] != '' or board[1][1] != '' and board[2][0] != '':
      c = 2
      r = 0
      while board[r][c] != ' ':
        r = r + 1
        if r > 2:
          r = 0
          c = c + 1
          
      
  else:
    while board[r][c] != ' ':
      c = c + 1
      if c > 2:
        c = 0
        r = r + 1
        
  return r, c