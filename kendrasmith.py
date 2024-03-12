import random
team_name = 'kendrasmith'
strategy_name = 'Corners then Center then Random'
strategy_description = 'Play corners if availible, then center if availible, then random'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

r_corners = [0,2]
c_corners = [0,2]

r_list = [0,1,2]
c_list = [0,1,2]

def move(player, board, score):
  r = random.choice(r_corners)
  c = random.choice(c_corners)
  while board[r][c] != ' ':
    if (board[0][0] != ' ' and board[0][2] != ' ' and board[2][0] != ' ' and board[2][2] != ' '):
      if board[1][1] == ' ':
        r = 1
        c = 1
      else:
        r = random.choice(r_list)
        c = random.choice(c_list)
    else:
      r = random.choice(r_corners)
      c = random.choice(c_corners)
  
    
  '''print(r, c)
  print_board(board)'''
  return r, c
  

