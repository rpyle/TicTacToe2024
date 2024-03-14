import random
team_name = 'Johnathan'
strategy_name = 'Diagonal to random'
strategy_description = 'go to the middle of the board and try to get the diagonal if taken go random'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])
Correct=True
def move(player, board, score):
  global Correct
  r=0
  c=2
  while board[r][c] != ' ':
    if Correct==True:
      c= c - 1
      r= r + 1
      if c == -1 :
        Correct=False
    if Correct == False:
      r = 2
      c = c+1
    if c == 3 and r== 2:
      r= random.randint(0,2)
      c= random.randint(0,2)

  return r, c
