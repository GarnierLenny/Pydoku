# Sudokupy

This is a playable sudoku game made with python

Originally I intended to only make a solver but I thought that it would be more appreciable with an graphical user interface.

## Installation

```bash
  python -m pip install -U pygame==2.5.2 --user
```

## Usage

```bash
// to only run the solver
python3 sudoku_solver.py [file_map path]

// to run the game
python3 gui.py [file_map path]
```

## In game

Once the game is running you can play it by placing your mouse on a cell and pressing one of the numbers on your keyboard, this will set the cell value to the corresponding key pressed.

Pressing the key '0' or backspace will clear the current cell.

Two buttons are on the interface, "Solve" and "Reset":
"Solve" will as it suggest solve the sudoku
"Reset" will clear every cell you changed, setting the sudoku to its default state

## Note

As of today (October 20th 2023) this project is kind of a draft so I plan on improving it along my python journey so stay tuned !

If you see something that is bad practice or simply wrong in my code feel free to contact me I'd be happy to exchange with you :)