import pygame
import sys

def main():

    pygame.init()
    screen = pygame.display.set_mode((1000,500))
    color = (0,0,0)
    color_rect = (255,0,0)
    color_rect2 = (255,255,0)

    x = 30
    y = 30
    
    width = 40
    height = 40
    rect2 = pygame.Rect(300,200,width,height)
    vel = 2
    points_vie = 3
    '''myfont = pygame.font.SysFont("monospace",16)
    score_display = myfont.render(str(points_vie),1,(0,255,0))'''
    text = ' ';
    myfont = pygame.font.SysFont("monospace",16)
    
    
    pygame.display.set_caption("Mouvement personnage, 1er essai")
    #pygame.display.flip()
    running = True

    while running :
        pygame.time.delay(10)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x>0:
            x -= vel
        if keys[pygame.K_RIGHT] and x<1000-width:
            x += vel
        if keys[pygame.K_UP] and y>0:
            y -= vel
        if keys[pygame.K_DOWN] and y<500-height:
            y += vel
        screen.fill(color)
        rect1 = pygame.draw.rect(screen,color_rect,pygame.Rect(x,y,width,height))
        collide = rect2.colliderect(rect1)
        if collide :
            if points_vie > 0 :
                points_vie = points_vie - 1
            color_rect2 = (0,0,255)
        else :
            color_rect2 = (255,255,0)
            
        if points_vie == 0 :
            text = 'GAME OVER !'
        else :
            text = str(points_vie)
        
        score_display = myfont.render(text,1,(0,255,0))
        pygame.draw.rect(screen,color_rect2,rect2)
        screen.blit(score_display, (100,100))
        pygame.display.update()
        
    pygame.quit()


main()










