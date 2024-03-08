team_name = 'Burnscoolcat''
strategy_name = 'Try something'
strategy_description = 'Just try and put X somewhere'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

'''
def move(player, board, score):
  r = 0
  c = 0
  while board[r][c] != ' ':
    c = c + 1
    if c > 2:
      c = 0
      r = r + 1
  
  return r, c
'''

def move(player, board, score):
  if board[1][1] == ' ':
    trythis(board)


def trythis(board):
  r = 0
  c = 0
  while board[r][c] != ' ':
    r = r + 1
    c = c + 1
    
  return r, c