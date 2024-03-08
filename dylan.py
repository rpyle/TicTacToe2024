team_name = 'dylan'
strategy_name = 'winning strat'
strategy_description = 'real'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

def move(player, board, score):
  r = 0
  c = 0
  while board[r][c] == ' ':
    r = 1
    c = 1
    if board[r][c] == ' ':
      r = 1
      c = 2
    if board[r][c] == ' ':
      r = 1
      c = 0
    else:
      r = r + 1
      c = c + 1
  return r, c