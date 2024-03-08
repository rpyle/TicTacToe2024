team_name = 'Nyby'
strategy_name = ' '
strategy_description = ' '

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

def move(player, board, score):
  #maybe
  if player == 'X':
    opp = "O"
  else:
    opp = "X"
  print()
  print(player, score)
  print_board(board)
  r = 1
  c = 1
  while board[r][c] != ' ':
    if board[r][c] == opp:
   
      

  
  print(r, c)
  return r, c
