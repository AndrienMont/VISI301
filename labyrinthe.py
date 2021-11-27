import random

#case : {"wallUp" = "True", "wallLeft" = "True"}

def generateMaze(long, larg):
    """Génère un labyrinthe

        IN
            long : int | longueur du labyrinthe
            larg : int | largeur du labyrinthe

        OUT
            maze : tableau de (tableau de (dictionnaire de deux booléens "wallUp" "wallLeft")) | labyrinthe généré

            """

    mazeRes = [[{"wallUp":True, "wallLeft":True} for i in range(0,larg)] for i in range(0,long)] # Labyrinthe résultat de dimensions long x larg

    mazeData = [[{"set":False, "done":False} for i in range(0,larg)] for i in range(0,long)] # Tableau d'état des cases (set : case déjà utilisée, done : case dont le traitement est fini)

    caseActive = randomBorderTile(long, larg) # Définit un point de départ aléatoire  
    x = caseActive[0]
    y = caseActive[1]
	
    casesParcourues = [] # Liste de l'ordre de vérification des cases
    indexCaseActive = 0 # Indice de la case active dans casesParcourues

    while (len(casesParcourues) < long*larg):
        #TRAITER ELEMENT
        casesParcourues.append(caseActive)
        mazeData[x][y]["set"] = True

        if (len(casesParcourues) == long*larg): # Si le labyrinthe est complet, on arrête la boucle (-10 pts en INFO303)
            break

        #OBTENIR ELEMENT SUIVANT
        while checkMovementPossibility(mazeData, x, y) == False: #Tant que aucun mouvement n'est possible
            mazeData[x][y]["done"] = True # La case courante n'est pas à traiter par la suite

            while mazeData[x][y]["done"]: # Chercher la prochaine case à traiter
                indexCaseActive = indexCaseActive - 1
                
                caseActive = casesParcourues[indexCaseActive]
                x = caseActive[0]
                y = caseActive[1]

        #Obtient nouvelle case    
        randomIndex = randomizeList([i for i in range(0,4)]) #Mélange l'ordre de vérification des index
        mouvTrouve = False
        i = 0
        rI = randomIndex[0]
        while mouvTrouve == False: #Cherche un mouvement valide aléatoirement
            if rI == 0: #Haut
                mouvTrouve = checkUpMove(mazeData, x, y)
            elif rI == 1: #Bas
                mouvTrouve = checkDownMove(mazeData, x, y)
            elif rI == 2: #Gauche
                mouvTrouve = checkLeftMove(mazeData, x, y)
            elif rI == 3: #Droite
                mouvTrouve = checkRightMove(mazeData, x, y)

            if mouvTrouve == False:
                i = i + 1
                rI = randomIndex[i]

        #Redéfini la case active
        if rI == 0: #Haut
            mazeRes[x][y]["wallUp"] = False #Enlève le mur entre l'ancienne et nouvelle case
            caseActive = [x, y-1]
        elif rI == 1: #Bas
            mazeRes[x][y+1]["wallUp"] = False #Enlève le mur entre l'ancienne et nouvelle case
            caseActive = [x, y+1]
        elif rI == 2: #Gauche
            mazeRes[x][y]["wallLeft"] = False #Enlève le mur entre l'ancienne et nouvelle case
            caseActive = [x-1, y]
        elif rI == 3: #Droite
            mazeRes[x+1][y]["wallLeft"] = False #Enlève le mur entre l'ancienne et nouvelle case
            caseActive = [x+1, y]
            

        indexCaseActive = len(casesParcourues) #La case active est la dernière
        x = caseActive[0]
        y = caseActive[1]
        
    return mazeRes

def checkMovementPossibility(mazeDataF1, xF1, yF1):
    """Vérifie si un mouvement est possible

    IN
        x : int | abscisse de la case à vérifier
        y : int | largeur du labyrinthe
        mazeDataF1 : tableau de tableau de cases | labyrinthe
    OUT
        boolean
    """

    return checkLeftMove(mazeDataF1, xF1, yF1) or checkRightMove(mazeDataF1, xF1, yF1) or checkUpMove(mazeDataF1, xF1, yF1) or checkDownMove(mazeDataF1, xF1, yF1)

def checkLeftMove(mazeDataF2, xF2, yF2):
    """Vérifie si un mouvement à gauche est possible

    IN
        x : int | abscisse de la case à vérifier
        y : int | ordonnée de la case à vérifier
        mazeDataF1 : tableau de tableau de cases | labyrinthe

    OUT
        boolean
    """

    return xF2 > 0 and mazeDataF2[xF2-1][yF2]["set"] == False

def checkRightMove(mazeDataF2, xF2, yF2):
    """Vérifie si un mouvement à droite est possible

    IN
        x : int | abscisse de la case à vérifier
        y : int | ordonnée de la case à vérifier
        mazeDataF1 : tableau de tableau de cases | labyrinthe

    OUT
        boolean
    """
    return xF2 < len(mazeDataF2)-1 and mazeDataF2[xF2+1][yF2]["set"] == False

def checkUpMove(mazeDataF2, xF2, yF2):
    """Vérifie si un mouvement en haut est possible

    IN
        x : int | abscisse de la case à vérifier
        y : int | ordonnée de la case à vérifier
        mazeDataF1 : tableau de tableau de cases | labyrinthe

    OUT
        boolean
    """

    return yF2 > 0 and mazeDataF2[xF2][yF2-1]["set"] == False

def checkDownMove(mazeDataF2, xF2, yF2):
    """Vérifie si un mouvement en bas est possible

    IN
        x : int | abscisse de la case à vérifier
        y : int | ordonnée de la case à vérifier
        mazeDataF1 : tableau de tableau de cases | labyrinthe

    OUT
        boolean
    """

    return yF2 < len(mazeDataF2[0])-1 and mazeDataF2[xF2][yF2+1]["set"] == False
    
            
def randomizeList(liste):
    """Mélange la liste"""

    res = liste

    def swap(i1, i2):
        """Inverse 2 élément dans une liste"""
        save = res[i1]
        res[i1] = res[i2]
        res[i2] = save

    for i in range(0,len(liste)-2):
        swap(i, random.randint(i, len(liste)-1))

    return res

def drawMaze(mazeF3):
    for j in range(0, len(mazeF3[0])):
        ligne = ""
        for i in range(0, len(mazeF3)):
            if mazeF3[i][j]["wallLeft"]:
                ligne=ligne+"|"
            else:
                ligne=ligne+" "

            if mazeF3[i][j]["wallUp"]:
                ligne=ligne+"̿"
            else:
                ligne=ligne+" "

            if i == len(mazeF3) -1:
                ligne = ligne + "|"
        print(ligne)
    ligne = " " + ("̿ "*(len(mazeF3[0])))
    print(ligne)

def yAMur(mazeF4, x, y, direction):
    """Vérifie si il y a un mur

    IN
        mazeDataF4 : tableau de tableau de cases | labyrinthe
        x : int | abscisse de la case à vérifier
        y : int | ordonnée de la case à vérifier
        direction : string | Direction du mur à vérifier ("left", "right", "up", "down")

    OUT
        boolean | Renvoie "vrai" si il y a un mur
    """

    res = True
    
    if direction == "left":
        res = mazeF4[x][y]["wallLeft"]

    if direction == "up":
        res = mazeF4[x][y]["wallUp"]

    if direction == "right" and x < len(mazeF4)-1:
        res = mazeF4[x+1][y]["wallLeft"]

    if direction == "down" and y < len(mazeF4[0])-1:
        res = mazeF4[x][y+1]["wallUp"]

    return res

def randomBorderTile(longF1, largF1):
    """Donne une case de frontière aléatoire

    IN
        longF1 : int | longueur du tableau
        largF1 : int | largeur du tableau

    OUT
        tableau de 2 int
    """

    perimeter = 2*(longF1 + largF1) - 4
    randomTile = random.randint(0,perimeter+1)

    if randomTile < longF1:
        res = [randomTile, 0]
    elif randomTile <= longF1+largF1-2:
        res = [longF1 - 1, randomTile - longF1 + 1]
    elif randomTile < 2*longF1+largF1:
        res = [randomTile - longF1 - largF1 + 1, largF1 - 1]
    else:
        res = [0, randomTile - 2*longF1 - largF1 + 2]

    return res
