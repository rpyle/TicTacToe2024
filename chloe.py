team_name = 'Chloe'
strategy_name = 'New Strategy'
strategy_description = 'Play the next open spot.'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

# original example0 code #
""""
def move(player, board, score):
  r = 0
  c = 0
  while board[r][c] != ' ':
    c = c + 1
    if c > 2:
      c = 0
      r = r + 1

return r, c
"""

# my code #
def move (player, board, score):
  r = 0
  c = 2
  while board[r][c] != ' ':
    r = r +1 
    if r > 2:
      r = 0
      c = c - 1
# prints out board, and r/c values 
  """print(board)
  print(r,c)"""
  return r, c
  





