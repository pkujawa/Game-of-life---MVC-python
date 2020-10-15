import modelGOF
import pygame
from modelGOF import *
from tkinter import *
from tkinter import messagebox

#stworzenie okna gry
GAMESCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
COLOR_ALIVE = (77, 179, 113)
COLOR_DEAD = (105, 100, 100)
#rysowanie komorek
def draw_cells():
    for y in range(ROWS):
        for x in range(COLS):
            if modelGOF.game_tab[x][y] == CELL_ALIVE:
                pygame.draw.circle(GAMESCREEN, COLOR_ALIVE, (int(x * CELL_SIZE + CELL_SIZE/2), int(y * CELL_SIZE + CELL_SIZE/2)), int(CELL_SIZE/2), 0)
            elif modelGOF.game_tab[x][y] == CELL_DEAD:
                pygame.draw.circle(GAMESCREEN, COLOR_DEAD, (int(x * CELL_SIZE + CELL_SIZE/2), int(y * CELL_SIZE + CELL_SIZE/2)), int(CELL_SIZE/2), 0)
#instrukcja gry
def instructionMessageBox():
    Tk().wm_withdraw()
    messagebox.showinfo('Hello', 'Bring cells to life by clicking on them with LMB. Use RMB to kill them. Press Enter to start the simulation or to stop it.')
