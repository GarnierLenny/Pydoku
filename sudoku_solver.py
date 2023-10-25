
import copy, time, sys, logging
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

def recursive_solve(board, x, y):
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
  # this section of the code needs to be extracted so that gui can call it every loop, return updated version of the board
  for i in range(9):
    board[y][x] += 1
    if check_hor(board, x, y) is True and check_ver(board, x, y) is True:
      for line in board:
        print(line)
      print()
      if recursive_solve(board, x + 1, y) is True:
        return True
  board[y][x] = 0
  # to here
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
  try:
    value = int(c)
    if value >= 0 and value <= 9:
      return True
  except:
    return False

def get_map():
  if (len(sys.argv) > 1):
    return sys.argv[1]
  return "map"

def solve():
  k = 0
  for i in range(9):
    for j in range(9):
      try:
        board[i][j] = int(file_map[k])
        k += 2
      except:
        logging.error("Invalid map format")
        exit()
  recursive_solve(board, 0, 0)
  for line in board:
    print(line)

if (sys.argv[0] == "sudoku_solver.py"):
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
  with open(get_map(), "r") as f:
    file_map = f.read()
    solve()