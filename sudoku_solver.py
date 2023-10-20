
import copy

def check_hor(board, x, y):
  for j in range(9):
      if board[y][x] == board[y][j] and j != x:
        break
      if j == 8:
        return True
  return False

def check_ver(board, x, y):
  for j in range(9):
      if board[y][x] == board[j][x] and j != y:
        break
      if j == 8:
        return True
  return False

def rec(board, x, y):
  if x == 9:
    x = 0
    y += 1
  if y == 9:
    return True
  while board[y][x] != 0:
    x += 1
    if x == 9:
      x = 0
      y += 1
    if y == 9:
      return True
  for i in range(9):
    board[y][x] += 1
    if check_hor(board, x, y) == True and check_ver(board, x, y) == True:
      if rec(board, x + 1, y) == True:
        return True
  board[y][x] = 0
  return False

def is_solved(board):
  ref = [0, 0, 0, 0, 0, 0, 0, 0, 0]
  for line in board:
      occurences = copy.copy(ref)
      for value in line:
        occurences[value - 1] += 1
        if occurences[value - 1] > 1:
            return False
  return True

solved_board = [
  [5, 3, 8, 7, 6, 9, 4, 1, 2],
  [6, 9, 7, 1, 4, 2, 8, 3, 5],
  [1, 2, 4, 8, 3, 5, 7, 6, 9],
  [8, 6, 3, 4, 2, 7, 9, 5, 1],
  [9, 7, 1, 5, 8, 3, 6, 2, 4],
  [4, 5, 2, 6, 9, 1, 3, 8, 7],
  [7, 1, 9, 3, 5, 8, 2, 4, 6],
  [2, 8, 6, 9, 7, 4, 5, 3, 1],
  [3, 4, 5, 2, 1, 6, 8, 7, 9]
]

board = [
  [0, 0, 0, 5, 7, 3, 0, 0, 2],
  [0, 0, 7, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 2, 9, 1, 3, 6, 0],
  [0, 6, 0, 4, 2, 5, 1, 8, 0],
  [0, 1, 0, 0, 0, 0, 0, 5, 0],
  [0, 8, 4, 1, 6, 9, 0, 2, 0],
  [0, 4, 1, 6, 5, 7, 0, 0, 0],
  [6, 0, 0, 0, 0, 0, 4, 0, 0],
  [8, 0, 0, 9, 1, 4, 0, 0, 0]
]

if rec(board, 0, 0) == False:
  print("Invalid sudoku map")