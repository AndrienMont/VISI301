import pygame
from pygame.locals import *
 
pygame.init()
 
class perso:
     
    def __init__(self): # Chargement du sprite et definition de sa position
         
        self.personnage = pygame.image.load('perso.png').convert_alpha()
        self.rect = self.personnage.get_rect()
        self.X = 0
        self.Y = 0
     
    def update (self):                      # Ajout d'une fonction Update
         
        self.position = (self.X,self.Y)
        self.rect = pygame.Rect(self.position, (100,100))      # Mise a jour du Rect par rapport à sa nouvelle position
 
         
    def bouge (self, direction):  # Definition d'un fonction pour faire bouger le sprite
             
            if direction == 'droite':               
                self.direct = self.personnage
                self.X += 4
            if direction == 'gauche':
                self.direct = self.personnage
                self.X -= 4
            if direction == "haut":
                self.direct = self.personnage
                self.Y -= 4
            if direction == "bas":
                self.direct = self.personnage
                self.Y += 4
 
 
screen = pygame.display.set_mode((500,500))   # Ouverture de la fenetre 
fond = pygame.image.load("background.jpg").convert()  # affichage du fond
joueur = perso()
 
mur = pygame.image.load('mur.png').convert_alpha()
mur_pos = mur.get_rect()
mur_pos = pygame.Rect((250,300) ,(216,216))         # Definition de la position du coin en haut à gauche du sprite
                                                    # et de sa taille


# Effectuer un deplacement plusieurs fois en laissant appuyé sur la touche
pygame.key.set_repeat(400, 30)

 
loop = True
while loop:
    for event in pygame.event.get():
        if event.type == QUIT:
            loop = False
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                joueur.update()                         # mise a jour du Rect avant de tester la collision
                if joueur.rect.colliderect(mur_pos):    # Si il y a une collision, le sprite va dans le sens inverse et donc s'écarte du mur.
                    print('collision')
                    joueur.bouge('droite')
                else:
                    joueur.bouge('gauche')              # Sinon il va dans la direction souhaité
                    
            if event.key == K_RIGHT:
                joueur.update()                         
                if joueur.rect.colliderect(mur_pos):
                    print('collision')
                    joueur.bouge('gauche')
                else:
                    joueur.bouge('droite')
                    
            if event.key == K_UP:
                joueur.update()                        
                if joueur.rect.colliderect(mur_pos):
                    print('collision')
                    joueur.bouge('bas')
                else:
                    joueur.bouge('haut')
                    
            if event.key == K_DOWN:
                joueur.update()                        
                if joueur.rect.colliderect(mur_pos):
                    print('collision')
                    joueur.bouge("haut")
                else:
                    joueur.bouge('bas')
                    
    #Re-collage          
    screen.blit(fond, (0,0))
    screen.blit(mur, (250,300))           
    screen.blit(joueur.personnage , (joueur.X, joueur.Y))
    
    #Rafraichissement
    pygame.display.flip()
