
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
p = 0
co2 = 0
def move(player, board, score):
  global t
  r = 1
  c = 1
  if t < 100:
   print(print_board(board))
    
   t = t+1
  global co
  if co < 100:
    co = co+1
    print (co)
  global p
  if p < 100:
    p = p+1 
    print (player)
  
  while board[r][c] != ' ':
    global co2
    r = 0
    c = 0
    while board[r][c] != ' ':
      c = c + 1
      if c > 2:
        c = 0
        r = r + 1

      
    if board[2][0] == ' ':
      c = 0
      r = 2
      
      
  return r, c
  
  
  