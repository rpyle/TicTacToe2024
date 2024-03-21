import random
from re import X
team_name = 'Frattalone'
strategy_name = 'Plus'
strategy_description = 'Makes a plus'
rand_nums = [0, 1, 2]

old_board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

def move(player, board, score):
  global old_board
  global i 
  i = 0
  j = 0
  for i in range (3):
    for j in range (3):
      if board[i][j] != old_board[i][j]:
        pass
  r = i
  c = j
  while board[r][c] != ' ':
    if board[1][1] == ' ':
      r = 1
      c = 1
    if board[1][0] == ' ':
      r = 0
      c = 0
    if board[1][2] == ' ':
      r = 1
      c = 2
    if board[0][1] == ' ':
      r = 0
      c = 2
    if board[2][1] == ' ':
      r = 1
      c = 2
    if board[0][0] == ' ':
      r = 2
      c = 0
    if board[2][2] == ' ':
      r = 2
      c = 2
    if board[0][2] == ' ':
      r = 0
      c = 2
    else:
      c = random.choice(rand_nums)
      r = random.choice(rand_nums)
      
    



  old_board = board
  old_board[r][c] = player
  return r, c