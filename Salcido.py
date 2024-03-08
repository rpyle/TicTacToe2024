import random
team_name = 'Salcido'
strategy_name = 'Win'
strategy_description = 'Never Losing'

def move(player, board, score):
  r = 0
  c = 0
  spot = 0

  while board[r][c] != ' ':
    r = random.randint(0,2)
    c = random.randint(0,2)

  

  spot1 = board[0][0]
  spot2 = board[0][1]
  spot3 = board[0][2]
  spot4 = board[1][0]
  spot5 = board[1][1]
  spot6 = board[1][2]
  spot7 = board[2][0]
  spot8 = board[2][1]
  spot9 = board[2][2]

  if spot1 == player:
    spot1 = "z"
  elif spot1 == ' ':
    spot1 = 0
  else:
    spot1 = "y"
  if spot2 == player:
    spot2 = "z"
  elif spot2 == ' ':
    spot2 = 0
  else:
    spot2 = "y"
  if spot3 == player:
    spot3 = "z"
  elif spot3 == ' ':
    spot3 = 0
  else:
    spot3 = "y"
  if spot4 == player:
    spot4 = "z"
  elif spot4 == ' ':
    spot4 = 0
  else:
    spot4 = "y"
  if spot5 == player:
    spot5 = "z"
  elif spot5 == ' ':
    spot5 = 0
  else:
    spot5 = "y"
  if spot6 == player:
    spot6 = "z"
  elif spot6 == ' ':
    spot6 = 0
  else:
    spot6 = "y"
  if spot7 == player:
    spot7 = "z"
  elif spot7 == ' ':
    spot7 = 0
  else:
    spot7 = "y"
  if spot8 == player:
    spot8 = "z"
  elif spot8 == ' ':
    spot8 = 0
  else:
    spot8 = "y"
  if spot9 == player:
    spot9 = "z"
  elif spot9 == ' ':
    spot9 = 0
  else:
    spot9 = "y"

  if (spot5 == "y"):
    spot = 1
  elif (spot5 == 0):
    spot = 5

  if (spot5 == "y"):
    if (spot3 == "y"):
      if (spot7 == 0):
        spot = 7
    if (spot7 == "y"):
      if (spot3 == 0):
        spot = 3
    if (spot2 == "y"):
      if (spot8 == 0):
        spot = 8
    if (spot4 == "y"):
      if (spot6 == 0):
        spot = 6
    if (spot6 == "y"):
      if (spot4 == 0):
        spot = 4
    if (spot8 == "y"):
      if (spot2 == 0):
        spot = 2
    if (spot9 == "y"):
      if (spot3 == 0):
        spot = 3
      elif (spot3 == "y"):
        if spot4 == 0:
          spot = 4
        else:
          if spot2 == 0:
            spot = 2
      elif (spot3 == "z"):
        if spot2 == 0:
          spot = 2
        else:
          if spot4 == 0:
            spot = 4

  if (spot5 == "z"):
    if (spot1 == "y"):
      if (spot3 == "y"):
        if spot2 == 0:
          spot = 2
      if (spot7 == "y"):
        if spot4 == 0: 
          spot = 4
      if (spot2 == "y"):
        if spot3 == 0:
          spot = 3
      if (spot4 == "y"):
        if spot7 == 0:
          spot = 7
      if (spot6 == "y"):
        if spot3 == 0:
          spot = 3
      if (spot8 == "y"):
        if spot7 == 0:
          spot = 7
      if (spot9 == "y"):
        if spot4 == 0:
          spot = 4
    if (spot2 == "y"):
      if (spot3 == "y"):
        if spot1 == 0:
          spot = 1
      if (spot7 == "y"):
        if spot1 == 0: 
          spot = 1
      if (spot4 == "y"):
        if spot1 == 0:
          spot = 1
      if (spot6 == "y"):
        if spot3 == 0:
          spot = 3
      if (spot8 == "y"):
        if spot1 == 0:
          spot = 1
      if (spot9 == "y"):
        if spot3 == 0:
          spot = 3
    if (spot3 == "y"):
      if (spot7 == "y"):
        if spot4 == 0: 
          spot = 4
      if (spot4 == "y"):
        if spot1 == 0:
          spot = 1
      if (spot6 == "y"):
        if spot9 == 0:
          spot = 9
      if (spot8 == "y"):
        if spot9 == 0:
          spot = 9
      if (spot9 == "y"):
        if spot6 == 0:
          spot = 6
    if (spot4 == "y"):
      if (spot7 == "y"):
        if spot1 == 0: 
          spot = 1
      if (spot6 == "y"):
        if spot1 == 0:
          spot = 1
      if (spot8 == "y"):
        if spot7 == 0:
          spot = 7
      if (spot9 == "y"):
        if spot7 == 0:
          spot = 7
    if (spot6 == "y"):
      if (spot7 == "y"):
        if spot9 == 0: 
          spot = 9
      if (spot8 == "y"):
        if spot9 == 0:
          spot = 9
      if (spot9 == "y"):
        if spot3 == 0:
          spot = 3
    if (spot7 == "y"):
      if (spot8 == "y"):
        if spot9 == 0:
          spot = 9
      if (spot9 == "y"):
        if spot8 == 0:
          spot = 8
    if (spot8 == "y"):
      if (spot9 == "y"):
        if spot7 == 0:
          spot = 7

  if (spot1 == "y"):
    if spot2 == "y":
      if spot3 == 0:
        spot = 3
    if spot3 == "y":
      if spot2 == 0:
        spot = 2
    if spot4 == "y":
      if spot7 == 0:
        spot = 7
    if spot7 == "y":
      if spot4 == 0:
        spot = 4
    if spot5 == "y":
      if spot9 == 0:
        spot = 9
  if (spot3 == "y"):
    if spot2 == "y":
      if spot1 == 0:
        spot = 1
    if spot6 == "y":
      if spot9 == 0:
        spot = 9
    if spot5 == "y":
      if spot7 == 0:
        spot = 7
    if spot9 == "y":
      if spot6 == 0:
        spot = 6
  if (spot7 == "y"):
    if spot4 == "y":
      if spot1 == 0:
        spot = 1
    if spot5 == "y":
      if spot3 == 0:
        spot = 3
    if spot8 == "y":
      if spot9 == 0:
        spot = 9
    if spot9 == "y":
      if spot8 == 0:
        spot = 8
  if (spot9 == "y"):
    if spot6 == "y":
      if spot3 == 0:
        spot = 3
    if spot5 == "y":
      if spot1 == 0:
        spot = 1
    if spot8 == "y":
      if spot7 == 0:
        spot = 7
  if (spot2 == "y"):
    if spot5 == "y":
      if spot8 == 0:
        spot = 8
  if (spot4 == "y"):
    if spot5 == "y":
      if spot6 == 0:
        spot = 6
  if (spot6 == "y"):
    if spot5 == "y":
      if spot4 == 0:
        spot = 4
  if (spot8 == "y"):
    if spot5 == "y":
      if spot2 == 0:
        spot = 2

  if (spot1 == "z"):
    if spot2 == "z":
      if spot3 == 0:
        spot = 3
    if spot3 == "z":
      if spot2 == 0:
        spot = 2
    if spot4 == "z":
      if spot7 == 0:
        spot = 7
    if spot7 == "z":
      if spot4 == 0:
        spot = 4
    if spot5 == "z":
      if spot9 == 0:
        spot = 9
  if (spot3 == "z"):
    if spot2 == "z":
      if spot1 == 0:
        spot = 1
    if spot6 == "z":
      if spot9 == 0:
        spot = 9
    if spot5 == "z":
      if spot7 == 0:
        spot = 7
    if spot9 == "z":
      if spot6 == 0:
        spot = 6
  if (spot7 == "z"):
    if spot4 == "z":
      if spot1 == 0:
        spot = 1
    if spot5 == "z":
      if spot3 == 0:
        spot = 3
    if spot8 == "z":
      if spot9 == 0:
        spot = 9
    if spot9 == "z":
      if spot8 == 0:
        spot = 8
  if (spot9 == "z"):
    if spot6 == "z":
      if spot3 == 0:
        spot = 3
    if spot5 == "z":
      if spot1 == 0:
        spot = 1
    if spot8 == "z":
      if spot7 == 0:
        spot = 7
  if (spot2 == "z"):
    if spot5 == "z":
      if spot8 == 0:
        spot = 8
  if (spot4 == "z"):
    if spot5 == "z":
      if spot6 == 0:
        spot = 6
  if (spot6 == "z"):
    if spot5 == "z":
      if spot4 == 0:
        spot = 4
  if (spot8 == "z"):
    if spot5 == "z":
      if spot2 == 0:
        spot = 2
  









  
  if spot == 1:
    r = 0
    c = 0
  if spot == 2:
    r = 0
    c = 1
  if spot == 3:
    r = 0
    c = 2
  if spot == 4:
    r = 1
    c = 0
  if spot == 5:
    r = 1
    c = 1
  if spot == 6:
    r = 1
    c = 2
  if spot == 7:
    r = 2
    c = 0
  if spot == 8:
    r = 2
    c = 1
  if spot == 9:
    r = 2
    c = 2
    

  
  return r, c