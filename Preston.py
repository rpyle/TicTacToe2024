import random

team_name = 'Preston_test'
strategy_name = 'Middle and corners'
strategy_description = 'Prioritize middle and corners whilelist not getting checkmated'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])
  print()

spot1 = 0,0
spot2 = 0,1
spot3 = 0,2
spot4 = 1,0
spot5 = 1,1
spot6 = 1,2
spot7 = 2,0
spot8 = 2,1
spot9 = 2,2


def move(player, board, score):
  if player == 'X':
    other_player = 'O'
    r = random.randint(0,2)
    c = random.randint(0,2)
    if board[2][2] == ' ':
      r = 2
      c = 2
    else:
      r = random.randint(0,2)
      c = random.randint(0,2)
    if board[1][1] == ' ':
      r = 1
      c = 1
    else:
      r = random.randint(0,2)
      c = random.randint(0,2)
    if board[1][1] == player and board[2][2] == player:
      r = 0
      c = 0
    elif board[1][1] == player and board[0][1] == player:
      r = 2
      c = 1
    elif board[1][1] == player and board[0][2] == player:
      r = 2
      c = 0
    elif board[1][1] == other_player:
      r = 2
      c = 1
    elif board[2][0] == other_player:
      r = 2
      c = 0
    elif board[0][0] == other_player and board[0][1] == other_player:
      r = 0
      c = 2
    elif board[0][0] == other_player and board[1][0] == other_player:
      r = 2
      c = 0
    elif board[0][0] == other_player and board[2][2] == other_player:
      r = 0
      c = 2 
    elif board[0][0] == other_player and board[2][0] == other_player:
      r = 1
      c = 0
    elif board[0][0] == other_player and board[0][2] == other_player:
      r = 0
      c = 1

    return r, c
    
  if player == 'O':
    other_player = 'X'
    r = random.randint(0,2)
    c = random.randint(0,2)
    
    if board[2][2] == ' ':
      r = 2
      c = 2
    else:
      r = random.randint(0,2)
      c = random.randint(0,2)
    if board[1][1] == ' ':
      r = 1
      c = 1
    else:
      r = random.randint(0,2)
      c = random.randint(0,2)
    if board[1][1] == player and board[2][2] == player:
      r = 0
      c = 0
    elif board[1][1] == player and board[0][1] == player:
      r = 2
      c = 1
    elif board[1][1] == player and board[0][2] == player:
      r = 2
      c = 0
    elif board[0][0] == other_player and board[0][1] == other_player:
      r = 0
      c = 2 
    elif board[0][0] == other_player and board[2][2] == other_player:
      r = 0
      c = 2 
    elif board[0][0] == other_player and board[1][0] == other_player:
      r = 2
      c = 0
    elif board[0][0] == other_player and board[2][0] == other_player:
      r = 1
      c = 0
    elif board[0][0] == other_player and board[0][2] == other_player:
      r = 0
      c = 1
    elif board[1][1] == other_player:
      r = 2
      c = 2
    elif board[2][2] == other_player:
      r = 1
      c = 1
    elif board[2][1] == other_player:
      r = 0
      c = 2
    elif board[0][2] == other_player:
      r = 1
      c = 2
    return r, c
  