team_name = 'Burnscoolcat'
strategy_name = 'Right Triangle Method'
strategy_description = 'Try and take the backwards L and win or take the diagnol and win'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])


'''def move(player, board, score):
  if board[1][1] == ' ':
    trythis(board)


def trythis(board):
  r = 0
  c = 0
  while board[r][c] != ' ':
    r = r + 1
    c = c + 1
    
  return r, c'''

def move(player, board, score):
  print_board(board)
  r = 0
  c = 0
  
  if board[1][1] == ' ':
    r = 1
    c = 1
  elif (board[0][2] == ' ' ):
    r = 0
    c = 2
  elif (board[2][0] == ' ' ):
    r = 2
    c = 0
  elif (board[2][2] == ' '):
    r = 2
    c = 2
  elif (board[2][1] == ' '):
    r = 2
    c = 1
  elif (board[1][2] == ' '):
    r = 1
    c = 2
  elif (board[2][1] == ' '):
    r = 2
    c = 1
 
  return r, c
  
    
  