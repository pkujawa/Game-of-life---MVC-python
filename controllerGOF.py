import pygame
import sys

import viewGOF
import modelGOF

pygame.init()

time_on = False
key_down = False

# tytuł
pygame.display.set_caption('GAME OF LIFE')

if __name__ == "__main__":
    #wyswietlenie instrukcji za pomoca messagebox
    viewGOF.instructionMessageBox()
    while True:
        #przechwytywanie dzialan gracza
        for event in pygame.event.get():
            #zamykanie okna gry
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #start i pauza gry
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if time_on:
                    time_on = False
                else:
                    time_on = True
            #ustawianie zywotnosci komorek - tylko w trakcie pauzy
            if time_on is False:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    key_down = True
                    button_type = event.button
                if event.type == pygame.MOUSEBUTTONUP:
                    key_down = False
                if key_down:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    mouse_x = int(mouse_x / modelGOF.CELL_SIZE)
                    mouse_y = int(mouse_y / modelGOF.CELL_SIZE)
                    modelGOF.changeCellState(button_type, mouse_x, mouse_y)
        #obliczanie zmian, gdy czas jest wlaczony
        if time_on is True:
            modelGOF.calculate_state()

        viewGOF.draw_cells()
        pygame.display.update()
        pygame.time.delay(300)
