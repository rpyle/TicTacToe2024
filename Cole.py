team_name = 'Cole'
strategy_name = 'Win'
strategy_description = 'Play the next open spot.'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

def move(player, board, score):
  print_board(board)
  r = 1
  c = 1
  if board[r][c] == ' ':
    return r, c
  elif board[r-1][c+1] == ' ':
    c = c + 1
    r = r - 1
    return r, c
  elif board[r-1][c-1] == ' ':
    c = c - 1
    r = r - 1
    return r, c