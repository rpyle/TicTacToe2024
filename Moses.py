
team_name = "Moses bot"
strategy_name = "goat"
strategy_description = "win"
def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2]+'\n')

co = 0
t = 0
i = 0
p = 0
co2 = 0
def move(player, board, score):
  global t
  global i
  
  
   
  global co
 
  if co < 2600:
    co = co+1
    print (co)
  global p
  if p < 2600:
    p = p+1 
    print (player)
  
  r = 1
  c = 1
  while board[r][c] != ' ':
    global co2
    r = 0
    c = 0
    while board[r][c] != ' ':
      c = c + 1
      if c > 2:
        c = 0
        r = r + 1
    if board[1][0] == ' ':
      r = 1
      c = 0

    if board[0][0] == ' ':
      r = 0
      c = 0

    if board[2][0] == ' ':
      c = 0
      r = 2

    if board[0][2] != ' ' and board[0][2]!= player and board[1][1] == player and board[2][2] == ' ':
      c = 2
      r = 2
    if board[1][1] != player and board[1][1] != ' ' and board[0][2] == player and board[1][2] == ' ':
      r = 1
      c = 2
    if board[0][2] == player and board[1][2] == player and board[2][2] == ' ':
      r = 2
      c = 2
      
    if board[0][2] == ' ':
      c = 2
      r = 0

    if board[1][1] == player and board[2][0] != player and board[2][0] != ' ' and board[2][2] == ' ':
      r = 2
      c = 2

  if board[0][0] != player and board[2][0] == player and board[0][0] != ' ' and board[2][0] != ' ' and board[1][0] == ' ':
    r = 1
    c = 0
  if board[2][2] != player and board[0][0] != player and board[2][2] != ' ' and board[0][0] != ' ' and board[2][0] == ' ':
    r = 2
    c = 0
  if board[0][2] != player and board[0][0] != player and board[2][2] != ' ' and board[0][0] != ' ' and board[2][0] == ' ':
    r = 2
    c = 0
  if board[2][0] != player and board[1][2] != player and board[2][0] != ' ' and board[1][2] != ' ' and board[2][2] == ' ':
    r = 2
    c = 2
  if board[0][1] != player and board[1][1] != player and board[0][1] != ' ' and board[1][1] != ' ' and board[2][1] == ' ':
    r = 2
    c = 1
  if board[0][0] != player and board[1][0] != player and board[0][0] != ' ' and board[1][0] != ' ' and board[2][0] == ' ':
    r = 2
    c = 0
  if board[0][0] != player and board[0][2] != player and board[0][0] != ' ' and board[0][2] != ' ' and board[0][1] == ' ':
    r = 0
    c = 1
  if board[2][0] != player and board[2][2] != player and board[2][0] != ' ' and board[2][2] != ' ' and board[2][1] == ' ':
    r = 2
    c = 1
  if board[2][1] != player and board[2][2] != player and board[2][1] != ' ' and board[2][2] != ' ' and board[0][1] == ' ':
    r = 0
    c = 1

  if board[0][2] == player and board[0][1] == player and board[0][0] == ' ':
    r = 0
    c = 0
  if board[0][2] == player and board[1][1] == player and board[2][0] == ' ':
      r = 2
      c = 0
  if board[0][2] == player and board[2][2] == player and board[1][2] == ' ':
    r = 1
    c = 2
  if board[0][1] == player and board[1][1] == player and board[2][1] == ' ':
    r = 2
    c = 1
  if board[0][0] == player and board[1][0] == player and board[2][0]:
    r = 2
    c = 0
  if board[2][2] == player and board[1][1] == player and board[0][0] == ' ':
    r = 0
    c = 0
  if board[0][0] == player and board[1][1] == player and board[2][2] == ' ':
    r = 2
    c = 2
  if board[2][0] == player and board[2][2] == player and board[2][1] == ' ':
    r = 2
    c = 1
  if board[0][0] == player and board[0][2] == player and board[0][1] == ' ':
    r = 0
    c = 1
  if board[0][0] != player and board[2][0] != player and board[2][0] != ' ' and board[0][0] != ' ' and board[1][0] == ' ':
    r = 1
    c = 0

  print (r,c)
  if i < 2600:
   print(score)
   i = i+1
  if t < 2600:
   print(print_board(board))
   t = t+1
      
  return r, c
  
  
  