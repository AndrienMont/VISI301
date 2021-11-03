import pygame
import sys
import labyrinthe as laby
import dessinLaby as dessLab

def main():

    pygame.init()
    
    screen = pygame.display.set_mode((700,700))
    pygame.display.set_caption("Prototype Alpha-1 du projet MazeRunner")

    origine_x = 0
    origine_y = 0
    tailleCase = 20

    dedale = laby.generateMaze(10,10)
    laby.drawMaze(dedale)

    dessLab.dessineDedale(origine_x,origine_y,tailleCase,dedale, 10,10,screen)

    running = True

    while running :
        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        pygame.display.update()

    pygame.quit()


main()
