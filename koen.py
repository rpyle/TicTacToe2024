team_name = 'koen'
strategy_name = ''
strategy_description = ''

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

def move(player, board, score):
  r = 0
  c = 0
  if board[1][1] == ' ':
    return 2, 2
  elif board[0][0] == ' ':
    return 0, 0
  elif board[0][2] == ' ':
    return 0, 2
  elif
    