import random

team_name = 'Lucas'
strategy_name = ' '
strategy_description = 'Play the next open spot.'




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
    c = c + 2
    if c == 2:
      #c = 0
      r = r + 2
      if board
  
  return r, c

