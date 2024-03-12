team_name = 'Spencer'
strategy_name = 'Corners'
strategy_description = 'Fill in center and corners before filling in spots between'

def print_board(board):
  
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

def move(player, board, score):
  '''print("b")
  print(player,score)
  print_board(board)'''
  r = 0
  c = 0

  if board[1][1] == ' ':
    r = 1
    c = 1
    return r, c

  if player == 'X':
    player = 'X'
  if player == 'O':
    player = 'O'

  if board[2][0] and board[0][2] == ' ' or player:
    if board[0][2] == ' ':
      r = 0
      c = 2
    elif board[2][0] == ' ':
      r = 2
      c = 0
    return r,c

  if board[0][0] and board[2][2] == ' ' or player:
    if board[0][0] == ' ':
      r = 0
      c = 0
    elif board[2][2] == ' ':
      r = 2
      c = 2
    return r,c

  if board[0][1] or board[1][0] or board[1][2] or board [2][1] == ' ':
    if board[0][0] and board[0][2] == player:
      if board[0][1] == ' ':
        r = 0
        c = 1
    elif board[0][0] and board[2][0] == player:
      if board[1][0] == ' ':
        r = 1
        c = 0
    elif board[0][2] and board[2][2] == player:
      if board[1][2] == ' ':
        r = 1
        c = 2
    elif board[2][0] and board[2][2] == player:
      if board[2][1] == ' ':
        r = 2
        c = 1
  
  return r, c

  