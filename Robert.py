import random


team_name = 'Rob'
strategy_name = 'Imaginary Technique. Hollow. Purple'
strategy_description = 'Throughout heaven and earth, I alone am the honored one'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])


def move(player, board, score):
  r, c = 0, 0
  if player == 'O':
    if board[0][0] == 'X':
      r, c = movesetstart2(player, board, score)
    elif board[0][1] == 'X':
      r, c = movesetstart2(player, board, score)
    elif board[0][2] == 'X':
      r, c = movesetstart2(player, board, score)
    elif board[1][0] == 'X':
      r, c = movesetstart2(player, board, score)
    elif board[1][1] == 'X':
      r, c = moveset5(player, board, score)
    elif board[1][2] == 'X':
      r, c = movesetstart2(player, board, score)
    elif board[2][0] == 'X':
      r, c = movesetstart2(player, board, score)
    elif board[2][1] == 'X':
      r, c = movesetstart2(player, board, score)
    elif board[2][2] == 'X':
      r, c = movesetstart2(player, board, score)
  elif player == 'X':
    r, c = movesetstart(player, board, score)
  return r, c

def movesetstart(player, board, score):
  r = 0
  c = 0
  moves = 1
  while moves != 9:
      if board[1][1] == ' ':
        moves += 2
        r, c = 1, 1
      elif board[0][0] == ' ':
        moves += 2
        r, c = 0, 0
      elif board[0][2] == ' ':
        moves += 2
        r, c = 0, 2
      elif board[2][0] == ' ':
        moves += 2
        r, c = 2, 0
      elif board[2][2] == ' ':
        moves += 2
        r, c = 2, 2
      elif board[0][0] == 'O' and board[0][2] == 'O' and moves == 5:
        moves += 2
        r, c = 0, 1
      elif board[0][0] == 'O' and board[0][1] == 'O' and moves == 5:
        moves += 2
        r, c = 0, 2
      elif board[0][1] == 'O' and board[0][2] == 'O' and moves == 5:
        moves += 2
        r, c = 0, 0
      elif board[0][0] == 'O' and board[2][0] == 'O' and moves == 5:
        moves += 2
        r, c = 1, 0
      elif board[0][0] == 'O' and board[1][0] == 'O' and moves == 5:
        moves += 2
        r, c = 2, 0
      elif board[1][0] == 'O' and board[2][0] == 'O' and moves == 5:
        moves += 2
        r, c = 0, 0
      elif board[2][0] == 'O' and board[2][1] == 'O' and moves == 5:
        moves += 2
        r, c = 2, 2
      elif board[2][0] == 'O' and board[2][2] == 'O' and moves == 5:
        moves += 2
        r, c = 2, 1
      elif board[2][1] == 'O' and board[2][2] == 'O' and moves == 5:
        moves += 2 
        r, c = 2, 1
      elif board[2][2] == 'O' and board[1][2] == 'O' and moves == 5:
        moves += 2
        r, c = 0, 2
      elif board[1][2] == 'O' and board[0][2] == 'O' and moves == 5:
        moves +=2 
        r, c = 2, 2
      elif board[2][2] == 'O' and board[0][2] == 'O' and moves == 5:
        moves += 2
        r, c = 1, 2
      else:
        if board[r][c] == ' ' and moves == 7:
          moves += 2
          r, c = r, c
        else:
          moves += 2
          r = random.randint(0, 2)
          c = random.randint(0, 2)
  return r, c 
      
      

def movesetstart2(player, board, score):
  r = 0
  c = 0
  moves = 1
  while moves != 9:
      if board[1][1] == ' ':
        moves += 2
        r, c = 1, 1
      elif board[0][0] == ' ':
        moves += 2
        r, c = 0, 0
      elif board[0][2] == ' ':
        moves += 2
        r, c = 0, 2
      elif board[2][0] == ' ':
        moves += 2
        r, c = 2, 0
      elif board[2][2] == ' ':
        moves += 2
        r, c = 2, 2
      elif board[0][2] == ' ':
        moves += 2
        r, c = 0, 2
      elif board[0][0] == 'O' and board[0][2] == 'O' and moves == 5:
        moves += 2
        r, c = 0, 1
      elif board[0][0] == 'O' and board[0][1] == 'O' and moves == 5:
        moves += 2
        r,c = 0, 2
      elif board[0][1] == 'O' and board[0][2] == 'O' and moves == 5:
        moves += 2
        r, c = 0, 0
      elif board[0][0] == 'O' and board[2][0] == 'O' and moves == 5:
        moves += 2
        r, c = 1, 0
      elif board[0][0] == 'O' and board[1][0] == 'O' and moves == 5:
        moves += 2
        r, c = 2, 0
      elif board[1][0] == 'O' and board[2][0] == 'O' and moves == 5:
        moves += 2
        r,c = 0, 0
      elif board[2][0] == 'O' and board[2][1] == 'O' and moves == 5:
        moves += 2
        r,c = 2, 2
      elif board[2][0] == 'O' and board[2][2] == 'O' and moves == 5:
        moves += 2
        r,c = 2, 1
      elif board[2][1] == 'O' and board[2][2] == 'O' and moves == 5:
        moves += 2 
        r, c = 2, 1
      elif board[2][2] == 'O' and board[1][2] == 'O' and moves == 5:
        moves += 2
        r,c = 0, 2
      elif board[1][2] == 'O' and board[0][2] == 'O' and moves == 5:
        moves +=2 
        r,c = 2, 2
      elif board[2][2] == 'O' and board[0][2] == 'O' and moves == 5:
        moves += 2
        r,c = 1, 2
      elif board[0][0] == 'X' and board[0][2] == 'X' and moves == 5:
        moves += 2
        r, c = 0, 1
      elif board[0][0] == 'X' and board[0][1] == 'X' and moves == 5:
        moves += 2
        r, c = 0, 2
      elif board[0][1] == 'X' and board[0][2] == 'X' and moves == 5:
        moves += 2
        r, c = 0, 0
      elif board[0][0] == 'X' and board[2][0] == 'X' and moves == 5:
        moves += 2
        r, c = 1, 0
      elif board[0][0] == 'X' and board[1][0] == 'X' and moves == 5:
        moves += 2
        r, c = 2, 0
      elif board[1][0] == 'X' and board[2][0] == 'X' and moves == 5:
        moves += 2
        r, c = 0, 0
      elif board[2][0] == 'X' and board[2][1] == 'X' and moves == 5:
        moves += 2
        r, c = 2, 2
      elif board[2][0] == 'X' and board[2][2] == 'X' and moves == 5:
        moves += 2
        r, c = 2, 1
      elif board[2][1] == 'X' and board[2][2] == 'X' and moves == 5:
        moves += 2 
        r, c = 2, 1
      elif board[2][2] == 'X' and board[1][2] == 'X' and moves == 5:
        moves += 2
        r, c = 0, 2
      elif board[1][2] == 'X' and board[0][2] == 'X' and moves == 5:
        moves +=2 
        r, c = 2, 2
      elif board[2][2] == 'X' and board[0][2] == 'X' and moves == 5:
        moves += 2
        r, c = 1, 2
      else:
        if board[r][c] == ' ' and moves == 7:
          moves += 2
          r, c = r, c
        else:
          moves +=2
          r = random.randint(0, 2)
          c = random.randint(0, 2)
  return r, c


def moveset5(player, board, score):
  r = 0
  c = 0
  moves = 1
  while moves != 9:
    if board[1][1] == 'X':
      moves += 2
      r, c = 0, 0
    elif board[0][1] == 'X':
      moves += 2
      r, c = 2, 1
    elif board[1][0] == 'X':
      moves += 2
      r, c = 1, 2
    elif board[2][1] == 'X':
      moves += 2
      r, c = 0, 1
    elif board[1][2] == 'X':
      moves += 2
      r, c = 1, 0
    elif board[0][2] == 'X':
      moves += 2
      r,c = 2, 0
    elif board[2][0] == 'X':
      moves += 2
      r, c = 0, 2
    elif board[0][0] == 'O' and board[0][2] == 'O' and moves == 5:
      moves += 2
      r, c = 0, 1
    elif board[0][0] == 'O' and board[0][1] == 'O' and moves == 5:
      moves += 2
      r,c = 0, 2
    elif board[0][1] == 'O' and board[0][2] == 'O' and moves == 5:
      moves += 2
      r, c = 0, 0
    elif board[0][0] == 'O' and board[2][0] == 'O' and moves == 5:
      moves += 2
      r, c = 1, 0
    elif board[0][0] == 'O' and board[1][0] == 'O' and moves == 5:
      moves += 2
      r, c = 2, 0
    elif board[1][0] == 'O' and board[2][0] == 'O' and moves == 5:
      moves += 2
      r,c = 0, 0
    elif board[2][0] == 'O' and board[2][1] == 'O' and moves == 5:
      moves += 2
      r,c = 2, 2
    elif board[2][0] == 'O' and board[2][2] == 'O' and moves == 5:
      moves += 2
      r,c = 2, 1
    elif board[2][1] == 'O' and board[2][2] == 'O' and moves == 5:
      moves += 2 
      r, c = 2, 1
    elif board[2][2] == 'O' and board[1][2] == 'O' and moves == 5:
      moves += 2
      r,c = 0, 2
    elif board[1][2] == 'O' and board[0][2] == 'O' and moves == 5:
      moves +=2 
      r,c = 2, 2
    elif board[2][2] == 'O' and board[0][2] == 'O' and moves == 5:
      moves += 2
      r,c = 1, 2
    else:
      if board[r][c] == ' ':
        moves += 2
        r, c = r, c
      else:
        moves += 2
        r = random.randint(0, 2)
        c = random.randint(0, 2)
  return r, c

