team_name = 'leuallen'
strategy_name = 'randomized movement to tie'
strategy_description = 'top right then select random for tie'
import random

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])


def move(player, board, score):
  while score > 0:
      r = random.randint(0, 2)
      c = random.randint(0, 2)
      if r < 3 and c < 3: # prevents out of bounds/rows or columns 
          return r, c

  if score <= 0:
      r = 0
      c = 2

  while board[r][c] != ' ':
    r = (r + 1) if r < 2 else 0  #basically prevents illegal move here
    if r == 0:
        c = (c + 1) if c < 2 else 0

  return r, c
    
