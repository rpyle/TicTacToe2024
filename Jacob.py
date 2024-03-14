import random
team_name = 'Jacob'
strategy_name = 'Corners'
strategy_description = 'Try to get corners then in between corners won.'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])


movelist=[]
def move(player, board, score):
  turnum = 1
  for i in board:
    for j in i:
      if j == player:
        turnum += 1
  global movelist, turn
  r = 0
  c = 2
  if turnum == 1:
    r = 0
    c = 2
    if board[r][c] != ' ':
      r = 2
      c = 0
  if turnum == 2:
    r = 2
    c = 2
    if board[r][c] != ' ':
      r = 0
      c = 0
      if board[r][c] != ' ':
        r = 1
        c = 1
  if turnum == 3:
    turns=int(len(movelist))
    turn1=(movelist[turns-2])
    turn2=(movelist[turns-1])
    if turn1 == (0,2) and turn2 ==(2,2):
      r = 1
      c = 2
      if board[r][c] != ' ':
        r = 0
        c = 1
        if board[r][c] != ' ':
          r = random.randint(0,2)
          c = random.randint(0,2)
    elif turn1 == (2,0) and turn2 ==(2,2):
      r = 2
      c = 1
      if board[r][c] != ' ':
        r = 1
        c = 0
        if board[r][c] != ' ':
          r = random.randint(0,2)
          c = random.randint(0,2)
    elif turn2 == (1,1):
      r = random.randint(0,2)
      c = random.randint(0,2)
  if turnum == 4:
    r = random.randint(0,2)
    c = random.randint(0,2)
  if turnum == 5:
    r = random.randint(0,2)
    c = random.randint(0,2)
  movelist.append((r,c))
  return r, c
  