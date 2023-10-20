
import copy
import time
import sys

global board

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

def is_num(c):
  if c >= '0' and c <= '9':
      return True
  return False

def map_checker(file_map):
  for i in range(0, 80, 2):
    if is_num(file_map[i]) == False or (file_map[i + 1] != ' ' and file_map[i + 1] != '\n'):
      return False
  return True

if (len(sys.argv) != 1):
  board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
  ]
  f = open(sys.argv[1], "r")
  file_map = f.read()
  if map_checker(file_map) == False:
    print("Passed map is invalid")
  else:
    k = 0
    for i in range(9):
      for j in range(9):
        board[i][j] = int(file_map[k])
        k += 2
    rec(board, 0, 0)
    for line in board:
      print(line)

# if rec(board, 0, 0) == False:
#   print("Invalid sudoku map")