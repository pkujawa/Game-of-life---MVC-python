#! /usr/bin/env python
# -*- coding: utf-8 -*-

# zdefiniowanie stalych
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 700
CELL_SIZE = 20
COLS = int(SCREEN_WIDTH / CELL_SIZE)
ROWS = int(SCREEN_HEIGHT / CELL_SIZE)
CELL_DEAD = 0
CELL_ALIVE = 1

#stan gry przedstawiony za pomocą listy dwuwymiarowej; poczatkowo - same martwe komorki
game_tab = [CELL_DEAD] * COLS
for col in range(COLS):
    game_tab[col] = [CELL_DEAD] * ROWS

#funckja zmieniajaca stan kazdej komorki na podstawie ilosci sasiadow
def calculate_state():
    global game_tab
    next_tab = [CELL_DEAD] * COLS
    for col in range(COLS):
        next_tab[col] = [CELL_DEAD] * ROWS
    #obliczanie ilosci sasiadow z zalozeniem periodycznych warunkow brzegowych
    for y in range(ROWS):
        for x in range(COLS):
            neighbors = 0
            if game_tab[(x - 1 + COLS)%COLS][(y - 1+ROWS)%ROWS] == CELL_ALIVE:
                neighbors += 1
            if game_tab[x][(y - 1 + ROWS)%ROWS] == CELL_ALIVE:
                neighbors += 1
            if game_tab[(x + 1+COLS)%COLS][(y - 1 + ROWS)%ROWS] == CELL_ALIVE:
                neighbors += 1
            if game_tab[(x - 1 + COLS)%COLS][y] == CELL_ALIVE:
                neighbors += 1
            if game_tab[(x + 1 + COLS)%COLS][y] == CELL_ALIVE:
                neighbors += 1
            if game_tab[(x - 1 + COLS)%COLS][(y + 1 + ROWS)%ROWS] == CELL_ALIVE:
                neighbors += 1
            if game_tab[x][(y + 1 + ROWS)%ROWS] == CELL_ALIVE:
                neighbors += 1
            if game_tab[(x + 1 + COLS)%COLS][(y + 1 + ROWS)%ROWS] == CELL_ALIVE:
                neighbors += 1
            #warunki smierci komorki - osamotnienie lub przeludnienie
            if game_tab[x][y] == CELL_ALIVE and (neighbors < 2 or neighbors > 3):
                next_tab[x][y] = CELL_DEAD
            #warunki dalszego zycia - 2 lub 3 sasiadow
            elif game_tab[x][y] == CELL_ALIVE and (neighbors == 3 or neighbors == 2):
                next_tab[x][y] = CELL_ALIVE
            #warunek ozywienia komorki - 3 sasiadow
            elif game_tab[x][y] == CELL_DEAD and neighbors == 3:
                next_tab[x][y] = CELL_ALIVE
    game_tab = next_tab

#zmiana stanu komorki w odpowiedzi na przycisk myszy
def changeCellState(click_type, mouse_x, mouse_y):
    #lewy przycisk myszy -  ozywianie
    if(click_type == 1):
        game_tab[mouse_x][mouse_y] = CELL_ALIVE
    #prawy przycisk myszy - usmiercanie
    elif(click_type == 3):
        game_tab[mouse_x][mouse_y] = CELL_DEAD


