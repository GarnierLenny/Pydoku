import pygame
import time, copy
from pygame_init import *
import pygame_init

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
  global screen

  if value != 0:
    if hover_check == 1:
      screen.blit(my_font.render(str(value), False, (0, 0, 0)), (ref + 20, y + 7))
    else:
      screen.blit(my_font.render(str(value), False, (255, 255, 255)), (ref + 20, y + 7))

def print_square(square_x, square_y, x, y):
  global board
  global solving

  for i in range(3):
    ref = copy.copy(x)
    for j in range(3):
      hover_check = 0
      pos = pygame.mouse.get_pos()
      if (pos[0] > ref + 5 and pos[0] < ref + 55) and (pos[1] > y + 5 and pos[1] < y + 55) and board_reference[i + 3 * square_y][j + 3 * square_x] == 0 and pygame_init.solving is False:
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), (ref, y, 60, 60))
        hover_check = 1
        set_cell_value(j + 3 * square_x, i + 3 * square_y)
      else:
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), (ref, y, 60, 60), 4)
        hover_check = 0
      print_cell_value(board[i + 3 * square_y][j + 3 * square_x], hover_check, ref, y)
      ref += 55
    y += 55

def display_board():
  global board
  screen.blit(my_font.render('SUDOKU', False, (255, 255, 255)), (195, 10))
  y = 60
  for i in range(3):
    x = 20
    for j in range(3):
      print_square(j, i, x, y)
      x += 55 * 3 + 10
    y += 55 * 3 + 10