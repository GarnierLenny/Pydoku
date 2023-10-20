import pygame
import copy
from sudoku_solver import rec

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

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

pygame.font.init()
my_font = pygame.font.SysFont('sans', 40)

def setup_reference():
  for i in range(9):
    for j in range(9):
      if board[i][j] != 0:
        board_reference[i][j] = 1

def set_frame_value(x, y):
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

def print_square_number(value, hover_check, ref, y):
  if value != 0:
    if hover_check == 1:
      screen.blit(my_font.render(str(value), False, (0, 0, 0)), (ref + 20, y + 7))
    else:
      screen.blit(my_font.render(str(value), False, (255, 255, 255)), (ref + 20, y + 7))

click_lock = False

def button(pos, dim, text, text_offset, fun, width):
  mouse_pos = pygame.mouse.get_pos()
  global click_lock

  if pygame.mouse.get_pressed()[0] == False:
    click_lock = False

  if (mouse_pos[0] > pos[0] and mouse_pos[0] < pos[0] + dim[0]) and (mouse_pos[1] > pos[1] and mouse_pos[1] < pos[1] + dim[1]):
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), (pos[0], pos[1], dim[0], dim[1]))
    if click_lock == False and pygame.mouse.get_pressed()[0] == True:
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
  rec(board, 0, 0)

def print_square(board, square_x, square_y, x, y):

  button((570, 250), (200, 50), 'Solve', (45, 2), solve, 3)
  button((570, 350), (200, 50), 'Reset', (45, 2), reset, 3)

  screen.blit(my_font.render('SUDOKU', False, (255, 255, 255)), (195, 10))
  for i in range(3):
    ref = copy.copy(x)
    for j in range(3):
      hover_check = 0
      pos = pygame.mouse.get_pos()
      if (pos[0] > ref + 5 and pos[0] < ref + 55) and (pos[1] > y + 5 and pos[1] < y + 55) and board_reference[i + 3 * square_y][j + 3 * square_x] == 0:
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), (ref, y, 60, 60))
        hover_check = 1
        set_frame_value(j + 3 * square_x, i + 3 * square_y)
      else:
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), (ref, y, 60, 60), 4)
        hover_check = 0
      print_square_number(board[i + 3 * square_y][j + 3 * square_x], hover_check, ref, y)
      ref += 55
    y += 55

def game_loop():
  y = 60
  for i in range(3):
    x = 20
    for j in range(3):
      print_square(board, j, i, x, y)
      x += 55 * 3 + 10
    y += 55 * 3 + 10

def init():
  running = True

  while running:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False
      screen.fill("black")
      game_loop()
      pygame.display.flip()

      clock.tick(60)

  pygame.quit()

setup_reference()
init()