team_name = 'Ben'
strategy_name = 'Center corners'
strategy_description = 'takes the middle than the open corners'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

def move(player, board, score):
  #print_board(board)
  r = 0
  c = 0
  if board[1][1] == ' ':
    c = 1
    r = 1
  elif board[0][0] == ' ':
    c = 0
    r = 0
  elif board[2][2] == ' ':
    c = 2
    r = 0
  elif board[2][0] == ' ':
    c = 0
    r = 2
  elif board[1][0] == ' ':
    c = 2
    r = 2
  
  #print(r,c)
  return r, c