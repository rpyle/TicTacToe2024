team_name = 'Kostons Bot'
strategy_name = 'watch 2 in a row'
strategy_description = 'look for win,look for block then play middle or diagonals'

import random

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

def move(player, board, score):


  if player == 'X':
    opp = 'O'
  else:
    opp = 'X'

  r, c = trywins(board,opp)
  if r is not False:
     return r, c
  r, c = trywins(board,player)
  if r is not False:
    return r, c
  else:
    r = 1
    c = 1
    if board[r][c] != ' ':
      r = 2
      c = 2
      if board[r][c] != ' ':
        r = 0
        c = 0
        if board[r][c] != ' ':
          r = 0
          c = 2
          if board[r][c] != ' ':
            r = 2
            c = 0
            if board[r][c] != ' ':
              r = random.randint(0,2)
              c = random.randint(0,2)
    return r, c
    
  

def trywins(board,opp):
  rlist1, clist1 = checkboard(board,opp)

  val1 = check(rlist1)
  val2 = check(clist1)

  if val1 is not False:
    r  = val1
    c = 0

    while board[r][c] != ' ' and c <= 2:
      c += 1
      if c == 3:
        break
      if board[r][c] == ' ':
        return r, c
  
  if val2 is not False:
    c = val2
    r = 0

    while board[r][c] != ' ' and r <= 2:
      r += 1
      if r == 3:
        break
      if board[r][c] == ' ' :
        return r, c
  return False, False


def checkboard(board,opp):
  rlist = []
  clist = []
  for r in range(2):
    for c in range(2):
      if board[r][c] == opp:
        rlist.append(r)
        clist.append(c)
  return rlist, clist

def check(list):
  dupes = []
  unique = []
  for i in list:
    if i not in unique:
      unique.append(i)
    elif i not in dupes:
      dupes.append(i)


  if len(dupes) != 0:
    return dupes[0]
  else:
    return False

  