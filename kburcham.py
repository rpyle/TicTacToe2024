team_name = 'kburcham'
strategy_name = 'Two corners'
strategy_description = 'Pick the middle if possible and use two corners to have two options to win.'

def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-+-+-')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-+-+-')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

def move(player, board, score):
  moves = 0
  r = 1
  c = 1
  while board[r][c] != ' ':
    if board[r][c] == player:
      if board[0][2] == " ":
        r = 0
        c = 2
        if board[2][0] == " ":
          r = 2
          c = 0
      if board[r][c] == player:
        r = 2
        c = 2
      else:
        if board[0][2] != " ":
          if board[0][2] != player:
            r = 2
            c = 1
            if board[r][c] == ' ':
              break
          else:
            r = 1
            c = 2
    else:
      if board[r][c] != ' ':
        if board[r][c] == player:
          r = 0
          c = 2
        else:
          r_list = [0,1,2]
          if board[r_list[r] - 1][c] != player:
            r = r_list[r-2]
          else:
            r = r_list[r-1]
      if board[r][c] != ' ':
        if board[r][c] == player:
          r = 2
          c = 0
    moves += 1
    if moves >= 9:
        break
  
  return r, c