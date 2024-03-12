team_name = 'Nyby'
strategy_name = 'Prevention?'
strategy_description = 'Focuses on movement, and then depending on positions, chooses a preventative measure'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])


def move(player, board, score):
  if player == 'X':
    opp = "O"
  else:
    opp = "X"

  r = 1
  c = 1

  tl = board[0][0]
  tm = board[0][1]
  tr = board[0][2]
  ml = board[1][0]
  mm = board[1][1]
  mr = board[1][2]
  bl = board[2][0]
  bm = board[2][1]
  br = board[2][2]

  if mm == player and tl == ' ':
    r = 0
    c = 0
    if mm and tl == player:
      r = 2
      c = 2
  elif mm == player and bl == ' ':
    r = 2
    c = 0
    if mm and bl == player: 
      r = 0
      c = 2
  elif mm == player and br == ' ':
    r = 2
    c = 2
    if mm and br == player:
      r = 0
      c = 0
  elif mm == player and tr == ' ':
    r = 0
    c = 2
    if mm and tr == player:
      r = 2
      c = 0
  
  elif mm == player and tm == ' ':
    r = 0
    c = 1
    if mm and tm == player:
      r = 2
      c =1
  elif mm == player and mr == ' ':
    r = 1
    c = 2
    if mm and mr == player:
      r = 1
      c = 0
  elif mm == player and bm == ' ':
    r = 2
    c = 1
    if mm and bm == player:
      r = 0
      c = 1
  elif mm == player and tm == ' ':
    r = 1
    c = 0
    if mm and tm == player:
      r = 2
      c = 1

  if tl and tm == opp and tr == ' ':
    r = 0
    c = 2
  if tl and tr == opp and tm == ' ':
    r = 0
    c = 1
  if tr and tm == opp and tl == ' ':
    r = 0
    c = 0
  if ml and mm == opp and mr == ' ':
    r = 1
    c = 2
  if ml and mr == opp and mm == ' ':
    r = 0
    c = 0
  if mr and mm == opp and ml == ' ':
    r = 1
    c = 0
  if bl and bm == opp and br == ' ':
    r = 2
    c = 2
  if bl and br == opp and bm == ' ':
    r = 2
    c = 1
  if br and bm == opp and bl == ' ':
    r = 2
    c = 0
  
  if tl and mm == opp and br == ' ':
    r = 2
    c = 2
  if tl and br == opp and mm == ' ':
    r = 1
    c = 1
  if br and mm == opp and tl == ' ':
    r = 0
    c = 0
  if tr and mm == opp and bl == ' ':
    r = 2
    c = 0
  if tr and bl == opp and mm == ' ':
    r = 1
    c = 1
  if bl and mm == opp and tr == ' ':
    r = 0
    c = 2


  if tl and ml == opp and bl == ' ':
    r = 2
    c = 0
  if tl and bl == opp and ml == ' ':
    r = 1 
    c = 0
  if ml and bl == opp and tl == ' ':
    r = 0
    c = 0
  if tm and mm == opp and bm == ' ':
    r = 2
    c = 1
  if tm and bm == opp and mm == ' ':
    r = 0 
    c = 0
  if mm and bm == opp and tm == ' ':
    r = 0
    c = 1
  if tr and mr == opp and br == ' ':
    r = 2
    c = 2
  if tr and br == opp and mr == ' ':
    r = 1 
    c = 2
  if mr and br == opp and tr == ' ':
    r = 0
    c = 2
  
  
  
  
  return r, c

  




