#EXPLICATION DE L'ALGORITHME

#   Crée un tableau V de vecteurs de la taille du labyrinthe
#   Crée une liste T de cases que l'on va traiter
#   Ajoute la case de fin à la liste T

#   Tant que la case départ n'est pas atteinte
#       Créer une liste newT
#       Pour toutes les cases dans la liste T
#           Attribuer aux cases à gauche, à droite, en haut et en bas un vecteur dans V qui pointe vers la case courante
#           Illustration :
#                 (0,1)
#      (1,0) (case Courante) (-1, 0)
#                 (0,-1)
#           Ajouter les cases à gauche, à droite, en haut et en bas à newT
#       Définir T comme newT, Ceci donne les cases à traiter à la prochaine itération

#   Une fois que l'on a trouvé la case départ
#   On crée un tableau Res

#   En commençant par la case départ, on lui ajoute le vecteur de V de la case courante et on enregistre la nouvelle case dans Res
#   Illustration :
#       case courante : (5,3)
#       vecteur sur la case courante : V[5][3] = (1,0)

#       case courante := case courante + vecteur sur la case courante = (5,3) + (1,0) = (6,3)

#   Répéter jusqu'à ce que l'on trouve la case de fin

#   Retourner Res

import labyrinthe3DPrototype as laby
import time

def pathFinding(maze, start, end):
    """Détermine le chemin le plus court entre un départ et une arrivée dans un labyrinthe
    
    IN
        maze : labyrinthe 2D | labyrinthe environnement
        start : Tuple de 2 int | case départ
        end : Tuple de 2 int | case arrivée
        
    OUT
        Tableau de Tuple de 2 int
    
    """

    mazeVectors = [[[(0,0,0) for i in range(0, len(maze[0][0]))] for i in range(0, len(maze[0]))] for i in range(0, len(maze))]
    activeTiles = [end]
    trouve = False

    while not trouve:
        for tile in activeTiles:
            if tile == start:
                trouve = True

        
        newActiveTiles = []
        for tile in activeTiles:
            z = tile[0]
            x = tile[1]
            y = tile[2]
            if not laby.yAMur(maze, x, y, z, "left"):
                if not (mazeVectors[z][x-1][y] != (0,0,0) or mazeVectors[z][x-1][y] == end):
                    mazeVectors[z][x-1][y] = (0,1,0)
                    newActiveTiles.append((z, x-1, y))
                    
            if not laby.yAMur(maze, x, y, z, "right"):
                if not (mazeVectors[z][x+1][y] != (0,0,0) or mazeVectors[z][x+1][y] == end):
                    mazeVectors[z][x+1][y] = (0,-1,0)
                    newActiveTiles.append((z, x+1, y))
                    
            if not laby.yAMur(maze, x, y, z, "up"):
                if not (mazeVectors[z][x][y-1] != (0,0,0) or mazeVectors[z][x][y-1] == end):
                    mazeVectors[z][x][y-1] = (0,0,1)
                    newActiveTiles.append((z, x, y-1))
                    
            if not laby.yAMur(maze, x, y, z, "down"):
                if not (mazeVectors[z][x][y+1] != (0,0,0) or mazeVectors[z][x][y+1] == end):
                    mazeVectors[z][x][y+1] = (0,0,-1)
                    newActiveTiles.append((z, x, y+1))
                    
            if not laby.yAMur(maze, x, y, z, "low"):
                if not (mazeVectors[z-1][x][y] != (0,0,0) or mazeVectors[z-1][x][y] == end):
                    mazeVectors[z-1][x][y] = (1,0,0)
                    newActiveTiles.append((z-1, x, y))
                    
            if not laby.yAMur(maze, x, y, z, "high"):
                if not (mazeVectors[z+1][x][y] != (0,0,0) or mazeVectors[z+1][x][y] == end):
                    mazeVectors[z+1][x][y] = (-1,0,0)
                    newActiveTiles.append((z+1, x, y))
        activeTiles = newActiveTiles
        
    res = []
    currentTile = start
    while currentTile != end:
        res.append(currentTile)
        
        z = currentTile[0]
        x = currentTile[1]
        y = currentTile[2]
        currentTile = (z + mazeVectors[z][x][y][0], x + mazeVectors[z][x][y][1], y + mazeVectors[z][x][y][2])
    res.append(end)
    del res[0]
    
    return res

def showPF(maze, path):
    for i in range(len(path)):
        laby.drawMaze(maze, path[i])
        time.sleep(1);

T = laby.generateMaze(3,3,3)
laby.drawMaze(T)
showPF(T, pathFinding(T, (0,0,0), (2,2,2)))
