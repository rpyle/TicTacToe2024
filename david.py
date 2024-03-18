team_name = 'david'
strategy_name = 'david strategy'
strategy_description = 'it plays the middle first and then plays in consecutive order'

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
  if board[1][1] != ' ':
    c = 1
    r = 1
  elif board[0][0] == ' ':
      c = 0
      r = 0
  elif board[0][1] == ' ':
    c = 0
    r = 1
  elif board[0][2] == ' ':
    c = 0
    r = 2
  elif board[1][0] == ' ':
    c = 1
    r = 0
  elif board [1][2] == ' ' :
    c = 1
    r = 2
  elif board[2][0] == ' ':
    c = 2
    r = 0
  elif board[2][1] == ' ':
    c = 2
    r = 1
  elif board[2][2] == ' ':
    c = 2
    r = 2
  return r, c
