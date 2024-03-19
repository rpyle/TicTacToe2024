team_name = 'Dancs'
strategy_name = 'Winning'
strategy_description = 'win'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

def Move (player, board, score):
  r = 0
  c = 0
  while board[r][c] != ' ':
    r = 0
    c = 0
    if board[r][c] != ' ':
      r = 2
      c = 2
    if board[r][c] != ' ':
      c = 1
      r = 1
  return r,c