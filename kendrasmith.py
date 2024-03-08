import random
team_name = 'kendrasmith'
strategy_name = ' '
strategy_description = ' '

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

r_corners = [0,0,2,2]
c_corners = [0,2,0,2]

r_list = [0,1,2]
c_list = [0,1,2]

def move(player, board, score):
  print_board(board)
  r = random.choice(r_corners)
  c = random.choice(c_corners)
  while board[r][c] != ' ':
    if r == 0 and c == 0:
     if board[0][2] == ' ':
      r = 0
      c = 2
     elif board[2][0] == ' ':
       r = 2
       c = 0
     elif board[2][2] == ' ':
       r = 2
       c = 2
  
    r = random.choice(r_corners)
    c = random.choice(c_corners)

    
    c = c + 1
    if c > 2:
      c = 0
      r = r + 1

  return r, c