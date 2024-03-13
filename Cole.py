team_name = 'Cole'
strategy_name = 'Right, Middle, Bottom- Win(sometimes)'
strategy_description = 'Play right side, then middle, then bottom.'

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
      c = 1
      r = 1
      if board [r][c] == ' ':
        return r,c
      if board [r][c] != ' ':
        c = c - 1
        if c < 0 :
          c = 0
          r =2
          return r,c
      return r, c
 
  return r, c





 