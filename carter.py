team_name = 'E4'
strategy_name = 'idk'
strategy_description = 'idk'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

def move(player, board, score):
  r = 0
  c = 0
  print(board)
  '''  
  while board[r][c] != ' ':
    c = c + 1
    if c > 2:
      c = 0
      r = r + 1
      '''
  if board[0][0] == 'X' and board[0][1] == 'X' or board[0][1] == 'X' and board[0][2] == 'X' or board[0][0] == 'X' and board[0][2] == 'X':
    while board[r][c] != ' ':
      c = c + 1
      if c > 2:
        c = 0
        r = r + 1
        '''
      return r, c
      '''
  elif board[1][0] == 'X' and board[1][1] == 'X' or board[1][1] == 'X' and board[1][2] == 'X' or board[1][0] == 'X' and board[1][2] == 'X':
    while board[r][c] != ' ':
      r = 1
      c = c + 1
      if c > 2:
        c = 0
        r = r + 1
      return r, c
  elif board[2][0] == 'X' and board[2][1] == 'X' or board[2][1] == 'X' and board[2][2] == 'X' or board[2][0] == 'X' and board[2][2] == 'X':
    while board[r][c] != ' ':
      r = 2
      c = c + 1
      if c > 2:
        c = 0
        r = r + 1
      return r, c
  elif board[0][0] == 'X' and board[2][2] == 'X' or board[0][0] == 'X' and board[1][1] == 'X' or board[1][1] == 'X' and board[2][2] == 'X':
    while board[r][c] != ' ':
      r = r + 1
      c = c + 1
      if c > 2:
        c = 0
        r = r + 1
      return r, c
  elif board[0][2] == 'X' and board[1][1] == 'X' or board[0][2] == 'X' and board[2][0] == 'X' or board[1][1] == 'X' and board[2][0] == 'X':
    while board[r][c] != ' ':
      r = r + 1
      c = c + 1
      if c > 2:
        c = 0
        r = r + 1
      return r, c
  else:
    while board[r][c] != ' ':
      c = c + 1
      if c > 2:
        c = 0
        r = r + 1
  return r, c