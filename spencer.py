team_name = 'Spencer'
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
    r = 1
    c =1

  while board[0][0] and board[0][2] == ' ':
    r = 0
    c = 0
  
  while board[r][c] != ' ':
    
    c = c + 1
    if c > 2:
      c = 0
      r = r + 1
  
  return r, c

