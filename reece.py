import random
team_name = 'Webb'
strategy_name = 'Center-Diagonal-Random'
strategy_description = 'Play center if available, then both diagonals to the right, then random'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

def move(player, board, score):
  r = 0
  c = 0
  
  while board[r][c] != ' ':
    r = random.randint(0,2)
    c = random.randint(0,2)
  if board [0][2] == ' ':
    r = 0
    c = 2
  if board [2][2] == ' ':
    r = 2
    c = 0
  if board [1][1] == ' ':
    r = 1
    c = 1
  return r, c