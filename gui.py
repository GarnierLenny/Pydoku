import pygame, copy, sys, logging
from sudoku_solver import recursive_solve, is_num, get_map

running = True
screen = 0
clock = 0
click_lock = False
pygame.font.init()
my_font = pygame.font.SysFont('sans', 40)
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
board_reference = [
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

def setup_reference():
  for i in range(9):
    for j in range(9):
      if board[i][j] != 0:
        board_reference[i][j] = 1

def set_cell_value(x, y):
  keys = pygame.key.get_pressed()
  if keys[pygame.K_0] or keys[pygame.K_BACKSPACE]:
    board[y][x] = 0
  elif keys[pygame.K_1]:
    board[y][x] = 1
  elif keys[pygame.K_2]:
    board[y][x] = 2
  elif keys[pygame.K_3]:
    board[y][x] = 3
  elif keys[pygame.K_4]:
    board[y][x] = 4
  elif keys[pygame.K_5]:
    board[y][x] = 5
  elif keys[pygame.K_6]:
    board[y][x] = 6
  elif keys[pygame.K_7]:
    board[y][x] = 7
  elif keys[pygame.K_8]:
    board[y][x] = 8
  elif keys[pygame.K_9]:
    board[y][x] = 9

def print_cell_value(value, hover_check, ref, y):
  if value != 0:
    if hover_check == 1:
      screen.blit(my_font.render(str(value), False, (0, 0, 0)), (ref + 20, y + 7))
    else:
      screen.blit(my_font.render(str(value), False, (255, 255, 255)), (ref + 20, y + 7))

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
  recursive_solve(board, 0, 0)

def print_square(board, square_x, square_y, x, y):
  for i in range(3):
    ref = copy.copy(x)
    for j in range(3):
      hover_check = 0
      pos = pygame.mouse.get_pos()
      if (pos[0] > ref + 5 and pos[0] < ref + 55) and (pos[1] > y + 5 and pos[1] < y + 55) and board_reference[i + 3 * square_y][j + 3 * square_x] == 0:
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), (ref, y, 60, 60))
        hover_check = 1
        set_cell_value(j + 3 * square_x, i + 3 * square_y)
      else:
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), (ref, y, 60, 60), 4)
        hover_check = 0
      print_cell_value(board[i + 3 * square_y][j + 3 * square_x], hover_check, ref, y)
      ref += 55
    y += 55

def game_loop():
  global running

  while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")

    y = 60
    for i in range(3):
      x = 20
      for j in range(3):
        print_square(board, j, i, x, y)
        x += 55 * 3 + 10
      y += 55 * 3 + 10

    display_buttons()
    pygame.display.flip()

    clock.tick(60)

def exit_game():
  global running
  running = False

def display_buttons():
  screen.blit(my_font.render('SUDOKU', False, (255, 255, 255)), (195, 10))
  button((570, 200), (200, 50), 'Solve', (45, 2), solve, 3)
  button((570, 300), (200, 50), 'Reset', (45, 2), reset, 3)
  button((570, 400), (200, 50), 'Exit', (65, 2), exit_game, 3)

def init():
  global screen
  global clock

  setup_check_board()
  setup_reference()

  pygame.init()
  screen = pygame.display.set_mode((800, 600))
  clock = pygame.time.Clock()

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