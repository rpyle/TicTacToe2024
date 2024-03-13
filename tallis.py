team_name = 'Tallis'
strategy_name = 'Right Side'
strategy_description = 'Fills out the right side, then goes through each spot'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])
'''
def move(player, board, score):
  print_board(board)
  r = 0
  c = 0 
  while board[r][c] != ' ':
    c = c + 1
    if c > 2:
      c = 0
      r = r + 1

  return r, c
'''

def move(player, board, score):
  r = 0
  c = 2
  if board[r][c] != ' ':
    r = r + 1
    if r > 2:
      r = 0
      c = 0
    else:
      r = 0
      c = 0 
      while board[r][c] != ' ':
        c = c + 1
        if c > 2:
          c = 0
          r = r + 1
      return r, c
  else:
    return r, c
      