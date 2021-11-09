import labyrinthe as laby

def pathFinding(maze, xStart, yStart, xEnd, yEnd):
    """Trouve le meilleur chemin dans un labyrinthe entre deux points

    IN
        maze : Tableau de tableau de dictionnaires de 2 booléens | labyrinthe
        xStart, yStart : int | Coordonnées de départ
        xEnd, yEnd : int | Coordonnées d'arrivée

    OUT
        Tableau de string
    """

    paths = [[(xStart, yStart)]]

    # Tableau d'état des cases (set : case déjà parcourue)
    mazeData = [[{"set":False} for i in range(0,len(maze[0]))] for i in range(0,len(maze))]

    def possibleMoves(xF1, yF1):
        """Récupère les mouvements possibles à partir d'une case

        IN
            xF1, yF1 : int | Coordonnées de la case

        OUT
            Tableau de string
        """
        res = []
        if not laby.yAMur(maze, xF1, yF1, "left"):
            res.append("gauche")

        if not laby.yAMur(maze, xF1, yF1, "up"):
            res.append("haut")

        if not laby.yAMur(maze, xF1, yF1, "right"):
            res.append("droite")

        if not laby.yAMur(maze, xF1, yF1, "down"):
            res.append("bas")

        return res

    i = 0
    pathFound = False
    while not pathFound or len(paths) == 0: # Boucler jusqu'à ce que le chemin soit trouvé ou si il n'y a aucun chemin
        caseActive = paths[i][len(paths[i])-1]
        x = caseActive[0]
        y = caseActive[1]

        moves = possibleMoves(x, y)
        movesDone = 0
        if not len(moves) == 0: #Si un mouvement est possible
            if moves[0] == "gauche":
                if movesDone == 0:
                    
                else:

                movesDone = movesDone + 1
                
            
        else: #Si le chemin arrive dans un cul-de-sac, on supprime le chemin
            del paths[i]
    
    

def directionEntreDeuxCases(caseIn, caseOut):
    """Renvoie la direction prise pour aller d'une case à l'autre

    IN
        caseIn : Tuple de 2 int | Case de départ
        caseOut : Tuple de 2 int | Case d'arrivée

    OUT
        String | (haut, bas, droite, gauche, erreur)
    """
    res = "erreur"
    
    if caseIn[0] == caseOut[0]:
        if caseIn[1] < caseOut[1]:
            res = "haut"
        elif caseIn[1] > caseOut[1]:
            res = "bas"
    else:
        if caseIn[1] == caseOut[1]:
            if caseIn[0] < caseOut[0]:
                res = "droite"
            elif caseIn[0] > caseOut[0]:
                res = "gauche"

    return res

def caseAjusteAvecDirection(caseF1, directionF1):
    """Détermine la case dans une direction (case à gauche, etc)

    IN
        caseF1 : Tuple de 2 int | Case de départ
        directionF1 : String (gauche, droite, haut, bas) | Direction à prendre

    OUT
        Tuple de 2 int
    """

    res = caseF1
    if directionF1 == "gauche":
        res[0] = res[0] - 1
    elif directionF1 == "droite":
        res[0] = res[0] + 1
    elif directionF1 == "haut":
        res[1] = res[1] - 1
    elif directionF1 == "bas":
        res[1] = res[1] + 1
    return res
    
    
