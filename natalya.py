team_name = 'Natalya'
strategy_name = 'Natalya'
strategy_description = 'Play the right column.'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

def move(player, board, score):
  r = 0
  c = 2
  while board[r][c] != ' ':
    r = r + 1
    if r > 2:
      r = 0
      c = c - 1
  return r, c