team_name = 'Best'
strategy_name = 'absolute skill ggez'
strategy_description = 'has a set path that will go along with, doesnt distinguish between players, just knows where it has been and where it isnt.' 
global boogalyboogalyboo
#boogalyboogalyboo is a variable that determines strategy used, it only has 2 chances to actvate cmnd ohno permanently to be the strategy for if center is placed on the first enemy term, this variable just either activates ohno or makes sure it doesnt activate ohno. It is named after a cars reference 
global path
global level
global path2
path2 = 0
level = 0
path = 0
boogalyboogalyboo = 0
def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

def ohno(player, board, score):
  global level
  r = 1
  c = 1 
  while board[1][1] != ' ':
    if board[0][2] == ' ':
      r = 0 
      c = 2
      return r, c
    elif board[2][0] == ' ':
      r = 0
      c = 1
      return r, c
    if board[1][1] and board[2][1] == ' ':
      if level == 0:
        r = 0
        c = 1
      if level == 0:
        level = 1
        return r, c
    elif board[1][1] and board[0][1] == ' ':
      if level == 0:
        level = 1
        r = 2
        c = 1
      if level == 0:
        level = 1
        return r, c
    elif board[1][1] and board[1][0] == ' ':
      if level == 0:
        level = 1
        r = 1
        c = 2
      if level == 0:
        level = 1
        return r, c
    elif board[1][1] and board[1][2] == ' ':
      if level == 0:
        level = 1
        r = 1
        c = 0
      if level == 0:
        level = 1
        return r, c

  for i in range(3):
    for b in range(3):
      if board[i][b] == ' ':
        r = i
        c = b
        return r, c



def move(player, board, score):
  global boogalyboogalyboo
  global path
  global level
  global path2
  #row x axis 1st parameter in list
  #colum y axis 2nd parameter in list
  r = 1
  c = 1
  if board[1][1] == ' ' and boogalyboogalyboo < 1: 
    boogalyboogalyboo =+ 1
  if board[1][1] != ' ' and boogalyboogalyboo < 1: 
    ohno(player, board, score)
  else: 
    if board[0][2] == ' ' and (path == 1 or path == 0):
      path = 1
      r = 0 
      c = 2
      if board[0][2] == ' ' and level == 0:
        level = 1
        return r, c
        
      if board[2][2] == ' ' and level == 1:
        level = 2
        path2 = 1
        r = 2
        c = 2
        return r, c
      elif board[0][0] == ' ' and level == 1:
        level = 2
        r = 0
        c = 0
        return r, c
        
      if board[2][2] == ' ' and level == 2:
        level = 3
        r = 2
        c = 2
        return r, c
      if path2 == 1:
        if board[0][0] == ' ' and level == 3:
          r = 0
          c = 0
          return r, c
        elif board[2][1] == ' ' and level == 3:
          r = 2
          c = 1
          return r, c
        elif board[1][2] == ' ' and level == 3:
          r = 1
          c = 2
          return r, c
      if path2 == 0:
        if board[0][0] == ' ' and level == 3:
          r = 0
          c = 0
          return r, c
        elif board[1][0] == ' ' and level == 3:
          r = 1
          c = 0
          return r, c
        elif board[0][1] == ' ' and level == 3:
          r = 0
          c = 1
          return r, c

    elif board[2][2] != ' ' and (path == 2 or path == 0):
      path = 2
      r = 0
      c = 1
      if board[2][2] == ' ' and level == 0:
        level = 1
        return r, c
      if board[2][0] == ' ' and level == 1:
        level = 2
        r = 2
        c = 0
        return r, c
      elif board[0][0] == ' ' and level == 1:
        level = 2
        r = 0
        c = 0
        return r, c
      elif board[1][1] == ' ' and level == 2:
        level = 3
        r = 1
        c = 1
        return r, c
      elif board[2][1] == ' ' and level == 2:
        r = 1
        c = 1
        return r, c
    
    for i in range(3):
      for b in range(3):
        if board[i][b] == ' ':
          r = i
          c = b
          return r, c
      
  return r, c