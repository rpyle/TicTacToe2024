import random

from example0 import print_board
team_name = 'Regesh'
strategy_name = 'attack the attacker strat'
strategy_description = 'play based on the side the attacker attacks, the strat priorizes the center and two corners at all times so it can complete one of the few created options but this strat is dependent on middle point or first turn. '

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])


def move(player, board, score):
  # Winning strat
  
  r = 0
  c = 0
  if board[1][1] == ' ':
      return 1, 1
  elif board[0][0] == ' ':
      return 0, 0
  elif board[0][2] == ' ':
      return 0, 2
  elif board[2][0] == ' ':
      return 2, 0
  elif board[2][2] == ' ':
      return 2, 2
  elif board[0][1] == ' ':
      return 0, 1
  elif board[1][0] == ' ':
      return 1, 0
  elif board[1][2] == ' ':
      return 1, 2
  elif board[2][1] == ' ':
      return 2, 1
  return r, c