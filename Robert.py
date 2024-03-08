import example0
import example1
import example2
import Robert
import random
team_name = 'Rob'
strategy_name = 'Immaginary Technique. Purple'
strategy_description = 'Throughout heaven and earth, I alone am the honored one'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

  

def move(player, board, score):
  if player == 'O':
    if board[0][0] == 'X':
      moveset1()
    if board[0][1] == 'X':
      moveset2()
    if board[0][2] == 'X':
      moveset3()
    if board[1][0] == 'X':
      moveset4()
    if board[1][1] == 'X':
      moveset5()
    if board[1][2] == 'X':
      moveset6()
    if board[2][0] == 'X':
      moveset7()
    if board[2][1] == 'X':
      moveset8()
    if board[2][2] == 'X':
      moveset9()
  elif player == 'X'""
  r = 0 
  c = 0
  while board[r][c] != ' ':
    if player == 'X':
      opp = 'O'
    else:
      opp = 'X'
      if board[1][1] == ' ':
        return 1, 1
      else:
        if board[0][0] == ' ':
          return 0, 0
        elif board[0][2] == ' ':
          return 0, 2
        elif board[2][0] == ' ':
          return 2, 0
        elif board[2][2] == ' ':
          return 2, 2
      if board[0][2] == ' ':
        return 0, 2
      elif board[2][0] == ' ':
        return 2, 0
      elif board[2][2] == ' ':
        return 2, 2
      elif board[0][1] == ' ':
        return 0, 1
      elif board[1][0] == ' ':
        return 1, 0
      elif board[2][1] == ' ':
        return 1, 0
      elif board[1][2] == ' ':
        return 1, 2
      if board[0][0] == 'X' and board[0][2] == 'X':
        return 0, 1
      if board[0][0] == 'X' and board[2][0] == 'X':
        return 1, 0
        

