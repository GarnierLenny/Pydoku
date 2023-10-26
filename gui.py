import pygame, copy, sys, logging
from sudoku_solver import is_num, get_map, check_hor, check_ver, check_square
import time
from components.display_board import display_board
from pygame_init import *
import pygame_init

global solving

def setup_reference():
  for i in range(9):
    for j in range(9):
      if board[i][j] != 0:
        board_reference[i][j] = 1

def button(pos, dim, text, text_offset, fun, width):
  mouse_pos = pygame.mouse.get_pos()
  global click_lock

  if pygame.mouse.get_pressed()[0] is False:
    click_lock = False

  if (mouse_pos[0] > pos[0] and mouse_pos[0] < pos[0] + dim[0]) and (mouse_pos[1] > pos[1] and mouse_pos[1] < pos[1] + dim[1]):
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), (pos[0], pos[1], dim[0], dim[1]))
    if click_lock is False and pygame.mouse.get_pressed()[0] is True:
      fun()
      click_lock = True
    screen.blit(my_font.render(text, False, (0, 0, 0)), (pos[0] + text_offset[0], pos[1] + text_offset[1]))
  else:
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), (pos[0], pos[1], dim[0], dim[1]), width)
    screen.blit(my_font.render(text, False, (255, 255, 255)), (pos[0] + text_offset[0], pos[1] + text_offset[1]))

def reset():
  for i in range(9):
    for j in range(9):
      if board_reference[i][j] == 0:
        board[i][j] = 0

def solve():
  reset()
  pygame_init.solving = True
  print(pygame_init.solving)
  recursive_solve(board, 0, 0)

def get_highlight_position(x, y):
  y_pos = (y + 1) * 60 - 5 * y
  y_pos += 10 if y >= 3 else 0
  y_pos += 10 if y >= 6 else 0
  x_pos = x * 60 + 20 - (5 * x)
  x_pos += 10 if x >= 3 else 0
  x_pos += 10 if x >= 6 else 0
  return x_pos + 4, y_pos + 4

def highlight_cell(x, y, cell_color, value_color):
  pos = get_highlight_position(x, y)
  pygame.draw.rect(screen, cell_color, (pos[0], pos[1], 52, 52))
  screen.blit(my_font.render(str(board[y][x]), False, value_color), (pos[0] + 15, pos[1] + 4))
  time.sleep(0.2)

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
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
  for i in range(9):
    board[y][x] += 1
    if check_hor(board, x, y) is True and check_ver(board, x, y) is True and check_square(board, x, y) is True:
      display_board()

      highlight_cell(x, y, pygame.Color(255, 255, 255), pygame.Color(0, 200, 0))

      refresh_screen()
      if recursive_solve(board, x + 1, y) is True:
        return True
  board[y][x] = 0
  return False

def refresh_screen():
  pygame.display.flip()
  screen.fill("black")
  clock.tick(60)


def game_loop():
  global running

  while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display_buttons()
    display_board()
    refresh_screen()

def exit_game():
  global running
  running = False

def display_buttons():
  button((570, 200), (200, 50), 'Solve', (45, 2), solve, 3)
  button((570, 300), (200, 50), 'Reset', (45, 2), reset, 3)
  button((570, 400), (200, 50), 'Exit', (65, 2), exit_game, 3)

def init():
  global screen
  global clock

  setup_check_board()
  setup_reference()

  pygame.init()

  game_loop()
  pygame.quit()

with open(get_map(), "r") as f:
  file_map = f.read()
  f.close()


def setup_check_board():
  global board

  k = 0
  for i in range(9):
    for j in range(9):
      try:
        board[i][j] = int(file_map[k])
        k += 2
      except:
        logging.error('Invalid map format')
        exit()

init()