import random

#case : {"wallUp" = "True", "wallLeft" = "True"}

def generateMaze(long, larg, haut):
    """Génère un labyrinthe

        IN
            long : int | longueur du labyrinthe
            larg : int | largeur du labyrinthe
	    haut : int | hauteur du labyrinthe

        OUT
            maze : tableau de (tableau de (tableau de (dictionnaire de trois booléens "wallUp" "wallLeft" "wallLow"))) | labyrinthe généré

            """

    mazeRes = [[[{"wallUp":True, "wallLeft":True, "wallLow":True} for i in range(0,larg)] for i in range(0,long)] for i in range(0, haut)] # Labyrinthe résultat de dimensions lhaut x long x larg

    mazeData = [[[{"set":False, "done":False} for i in range(0,larg)] for i in range(0,long)] for i in range(0, haut)] # Tableau d'état des cases (set : case déjà utilisée, done : case dont le traitement est fini)

    caseActive = (0,0,0) #randomBorderTile(long, larg) # Définit un point de départ aléatoire
    z = caseActive[0]
    x = caseActive[1]
    y = caseActive[2]
	
    casesParcourues = [] # Liste de l'ordre de vérification des cases
    indexCaseActive = 0 # Indice de la case active dans casesParcourues

    while (len(casesParcourues) < long*larg*haut):
        #TRAITER ELEMENT
        casesParcourues.append(caseActive)
        mazeData[z][x][y]["set"] = True

        if (len(casesParcourues) == long*larg*haut): # Si le labyrinthe est complet, on arrête la boucle (-10 pts en INFO303)
            break

        #OBTENIR ELEMENT SUIVANT
        while checkMovementPossibility(mazeData, z, x, y) == False: #Tant que aucun mouvement n'est possible
            mazeData[z][x][y]["done"] = True # La case courante n'est pas à traiter par la suite

            while mazeData[z][x][y]["done"]: # Chercher la prochaine case à traiter
                indexCaseActive = indexCaseActive - 1
                
                caseActive = casesParcourues[indexCaseActive]
                z = caseActive[0]
                x = caseActive[1]
                y = caseActive[2]

        #Obtient nouvelle case    
        randomIndex = randomizeList([i for i in range(0,6)]) #Mélange l'ordre de vérification des index
        mouvTrouve = False
        i = 0
        rI = randomIndex[0]
        while mouvTrouve == False: #Cherche un mouvement valide aléatoirement
            if rI == 0: #Haut
                mouvTrouve = checkUpMove(mazeData, z, x, y)
            elif rI == 1: #Bas
                mouvTrouve = checkDownMove(mazeData, z, x, y)
            elif rI == 2: #Gauche
                mouvTrouve = checkLeftMove(mazeData, z, x, y)
            elif rI == 3: #Droite
                mouvTrouve = checkRightMove(mazeData, z, x, y)
            elif rI == 4: #Niveau Inférieur
                mouvTrouve = checkLowMove(mazeData, z, x, y)
            elif rI == 5: #Niveau Supérieur
                mouvTrouve = checkHighMove(mazeData, z, x, y)

            if mouvTrouve == False:
                i = i + 1
                rI = randomIndex[i]

        #Redéfini la case active
        if rI == 0: #Haut
            mazeRes[z][x][y]["wallUp"] = False #Enlève le mur entre l'ancienne et nouvelle case
            caseActive = [z, x, y-1]
        elif rI == 1: #Bas
            mazeRes[z][x][y+1]["wallUp"] = False #Enlève le mur entre l'ancienne et nouvelle case
            caseActive = [z, x, y+1]
        elif rI == 2: #Gauche
            mazeRes[z][x][y]["wallLeft"] = False #Enlève le mur entre l'ancienne et nouvelle case
            caseActive = [z, x-1, y]
        elif rI == 3: #Droite
            mazeRes[z][x+1][y]["wallLeft"] = False #Enlève le mur entre l'ancienne et nouvelle case
            caseActive = [z, x+1, y]
        elif rI == 4: #Niveau Inférieur
            mazeRes[z][x][y]["wallLow"] = False #Enlève le mur entre l'ancienne et nouvelle case
            caseActive = [z-1, x, y]
        elif rI == 5: #Niveau Supérieur
            mazeRes[z+1][x][y]["wallLow"] = False #Enlève le mur entre l'ancienne et nouvelle case
            caseActive = [z+1, x, y]
            

        indexCaseActive = len(casesParcourues) #La case active est la dernière
        z = caseActive[0]
        x = caseActive[1]
        y = caseActive[2]
        
    return mazeRes

def checkMovementPossibility(mazeDataF1, zF1, xF1, yF1):
    """Vérifie si un mouvement est possible

    IN
    	mazeDataF1 : tableau de tableau de tableau de cases | labyrinthe
   	zF1 : int | cote de la case à vérifier
        xF1 : int | abscisse de la case à vérifier
        yF1 : int | ordonnée de la case à vérifier
    OUT
        boolean
    """

    c1 = checkLeftMove(mazeDataF1, zF1, xF1, yF1)
    c2 = checkRightMove(mazeDataF1, zF1, xF1, yF1)
    c3 = checkUpMove(mazeDataF1, zF1, xF1, yF1)
    c4 = checkDownMove(mazeDataF1, zF1, xF1, yF1)
    c5 = checkLowMove(mazeDataF1, zF1, xF1, yF1)
    c6 = checkHighMove(mazeDataF1, zF1, xF1, yF1)

    return c1 or c2 or c3 or c4 or c5 or c6

def checkLeftMove(mazeDataF2, zF2, xF2, yF2):
    """Vérifie si un mouvement à gauche est possible

    IN
    	mazeDataF2 : tableau de tableau de tableau de cases | labyrinthe
    	zF2 : int | cote de la case à vérifier
        xF2 : int | abscisse de la case à vérifier
        yF2 : int | ordonnée de la case à vérifier

    OUT
        boolean
    """

    return xF2 > 0 and mazeDataF2[zF2][xF2-1][yF2]["set"] == False

def checkRightMove(mazeDataF2, zF2, xF2, yF2):
    """Vérifie si un mouvement à droite est possible

    IN
    	mazeDataF2 : tableau de tableau de tableau de cases | labyrinthe
    	zF2 : int | cote de la case à vérifier
        xF2 : int | abscisse de la case à vérifier
        yF2 : int | ordonnée de la case à vérifier

    OUT
        boolean
    """
    return xF2 < len(mazeDataF2[0])-1 and mazeDataF2[zF2][xF2+1][yF2]["set"] == False

def checkUpMove(mazeDataF2, zF2, xF2, yF2):
    """Vérifie si un mouvement en haut est possible

    IN
    	mazeDataF2 : tableau de tableau de tableau de cases | labyrinthe
    	zF2 : int | cote de la case à vérifier
        xF2 : int | abscisse de la case à vérifier
        yF2 : int | ordonnée de la case à vérifier

    OUT
        boolean
    """

    return yF2 > 0 and mazeDataF2[zF2][xF2][yF2-1]["set"] == False

def checkDownMove(mazeDataF2, zF2, xF2, yF2):
    """Vérifie si un mouvement en bas est possible

    IN
    	mazeDataF2 : tableau de tableau de tableau de cases | labyrinthe
    	zF2 : int | cote de la case à vérifier
        xF2 : int | abscisse de la case à vérifier
        yF2 : int | ordonnée de la case à vérifier

    OUT
        boolean
    """

    return yF2 < len(mazeDataF2[0][0])-1 and mazeDataF2[zF2][xF2][yF2+1]["set"] == False

def checkLowMove(mazeDataF2, zF2, xF2, yF2):
    """Vérifie si un mouvement en haut est possible

    IN
    	mazeDataF2 : tableau de tableau de tableau de cases | labyrinthe
    	zF2 : int | cote de la case à vérifier
        xF2 : int | abscisse de la case à vérifier
        yF2 : int | ordonnée de la case à vérifier

    OUT
        boolean
    """

    return zF2 > 0 and mazeDataF2[zF2-1][xF2][yF2]["set"] == False

def checkHighMove(mazeDataF2, zF2, xF2, yF2):
    """Vérifie si un mouvement en bas est possible

    IN
        mazeDataF2 : tableau de tableau de tableau de cases | labyrinthe
    	zF2 : int | cote de la case à vérifier
        xF2 : int | abscisse de la case à vérifier
        yF2 : int | ordonnée de la case à vérifier

    OUT
        boolean
    """

    return zF2 < len(mazeDataF2)-1 and mazeDataF2[zF2+1][xF2][yF2]["set"] == False
    
            
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
    for k in range(len(mazeF3)-1, -1, -1):
        for j in range(0, len(mazeF3[0][0])):
            ligne = ""
            for i in range(0, len(mazeF3[0])):
                if mazeF3[k][i][j]["wallLeft"]:
                    ligne=ligne+"|"
                else:
                    ligne=ligne+" "

                if mazeF3[k][i][j]["wallUp"]:
                    ligne=ligne+"̿"
                else:
                    ligne=ligne+"v"

                if i == len(mazeF3) -1:
                    ligne = ligne + "|"
            print(ligne)
        ligne = " " + ("̿ "*(len(mazeF3[0])))
        print(ligne)
    print()

def yAMur(mazeF4, z, x, y, direction):
    """Vérifie si il y a un mur

    IN
        mazeDataF4 : tableau de tableau de tableau de cases | labyrinthe
	zF4 : int | cote de la case à vérifier
        xF4 : int | abscisse de la case à vérifier
        yF4 : int | ordonnée de la case à vérifier
        direction : string | Direction du mur à vérifier ("left", "right", "up", "down")

    OUT
        boolean | Renvoie "vrai" si il y a un mur
    """

    res = True
    
    if direction == "left":
        res = mazeF4[z][x][y]["wallLeft"]

    if direction == "up":
        res = mazeF4[z][x][y]["wallUp"]

    if direction == "low":
        res = mazeF4[z][x][y]["wallLow"]

    if direction == "right" and x < len(mazeF4[0])-1:
        res = mazeF4[z][x+1][y]["wallLeft"]

    if direction == "down" and y < len(mazeF4[0][0])-1:
        res = mazeF4[z][x][y+1]["wallUp"]

    if direction == "high" and y < len(mazeF4)-1:
        res = mazeF4[z+1][x][y]["wallLow"]

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
