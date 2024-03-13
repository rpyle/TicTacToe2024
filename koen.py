team_name = 'koen'
strategy_name = 'Middle & Corners'
strategy_description = 'Play middle and corners, and then play first open spots.' 

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

def move(player, board, score):
  if board[1][1] == ' ':
    r = 1
    c = 1
  elif board[0][0] == ' ':
    r = 0
    c = 0
  elif board[0][2] == ' ':
    r = 0
    c = 2
  elif board[2][0] == ' ':
    r = 2
    c = 0
  elif board[2][2] == ' ':
    r = 2
    c = 2
  else:
    for r in range(3):
      for c in range(3):
          if board[r][c] == ' ':
            return r, c
  return r, c
  
    

    