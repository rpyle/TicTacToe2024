import random
from re import X
team_name = 'Frattalone'
strategy_name = 'Next Open'
strategy_description = 'Play the next open spot.'

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
  print_board(old_board)
  print_board(board)
  for i in range (3):
    for j in range (3):
      if board[i][j] != old_board[i][j]:
        print(i, j)
  r = 1
  c = 0
  if player == 'X':
    opponent = 'O'
  if player == 'O':
    opponent = 'X'
  '''while board[r][c] != ' ':
    c = c + 1
    r = r + 1
    if c > 2:
      c = 0
      r = r + 1'''
  old_board = board
  old_board[r][c] = player
  return r, c
