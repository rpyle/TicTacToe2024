team_name = 'kburcham'
strategy_name = ''
strategy_description = ''

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

def move(player, board, score):
  print_board(board)
  r = 0
  c = 0
  while board[r][c] != ' ':
    if board[r][c] == player:
      r = 2
      c = 2
    else:
      r = 2
    if board[r][c] != ' ':
      if board[r][c] == player:
        r = r + 2
        c = c + 2
      r = 0
      c = 2
    if board[r][c] != ' ':
      r = 2
      c = 0

  print(r,c)
  return r, c