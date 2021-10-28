import random

longueur = 16
largeur = 10
labyrinthe = []

#case : {"wallUp" = "True", "wallLeft" = "True"}

def generateMaze(long, larg):
    """Génère un labyrinthe

        IN
            long : int | longueur du labyrinthe
            larg : int | largeur du labyrinthe

        OUT
            maze : tableau de tableau de cases | labyrinthe généré
            """

    mazeRes = [[{"wallUp":True, "wallLeft":True} for i in range(0,larg)] for i in range(0,long)]

    mazeData = [[{"set":False, "done":False} for i in range(0,larg)] for i in range(0,long)]

    caseActive = [0, 0]
    x = 0
    y = 0
	
    casesParcourues = []
    indexCaseActive = 0
    ajouterCase = True

    while (len(casesParcourues) < long*larg):
        #Traiter élément
        if ajouterCase:
            casesParcourues.append(caseActive)
            print(x)
            print(y)
            print()
            mazeData[x][y]["set"] = True

        #Obtenir élément suivant
        ajouterCase = True
        if checkMovementPossibility(mazeData, x, y): #Si une case à côté est libre
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

                i = i + 1
                rI = randomIndex[i]

            #Redéfinie la case active
            if rI == 0: #Haut
                mazeRes[x][y]["wallUp"] = False #Enlève le mur entre l'ancienne et nouvelle case
                caseActive = [x, y-1]
            elif rI == 1: #Bas
                mazeRes[x][y+1]["wallUp"] = False #Enlève le mur entre l'ancienne et nouvelle case
                caseActive = [x, y+1]
            elif rI == 2: #Gauche
                mazeRes[x-1][y]["wallLeft"] = False #Enlève le mur entre l'ancienne et nouvelle case
                caseActive = [x-1, y]
            elif rI == 3: #Droite
                mazeRes[x+1][y]["wallLeft"] = False #Enlève le mur entre l'ancienne et nouvelle case
                caseActive = [x+1, y]
                
        else: #Si aucun mouvement n'est possible
            ajouterCase = False 
            mazeData[x][y]["done"] = True # La case n'est pas à traiter à la suite

            while mazeData[x][y]["done"]:
                indexCaseActive = indexCaseActive - 1
                
                casesParcourues[indexCaseActive]
                x = caseActive[0]
                y = caseActive[1]
            
        
            

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

    mouvCounter = 4

    if checkLeftMove(mazeDataF1, xF1, yF1) == False:
        mouCounter = mouvCounter - 1

    if checkRightMove(mazeDataF1, xF1, yF1) == False:
        mouCounter = mouvCounter - 1

    if checkUpMove(mazeDataF1, xF1, yF1) == False:
        mouCounter = mouvCounter - 1

    if checkDownMove(mazeDataF1, xF1, yF1) == False:
        mouCounter = mouvCounter - 1

    return mouvCounter > 0

def checkLeftMove(mazeDataF2, xF2, yF2):
    """Vérifie si un mouvement à gauche est possible

    IN
        x : int | abscisse de la case à vérifier
        y : int | largeur du labyrinthe
        mazeDataF1 : tableau de tableau de cases | labyrinthe

    OUT
        res : boolean
    """
    res = True
    if xF2 > 0: 
        if mazeDataF2[xF2-1][yF2]["set"]: #Si la case de gauche est définie, il y a un mouvement de moins possible
            res = False
    else: #Si la case est tout à gauche, il y a un mouvement de moins possible
        res = False

    return res

def checkRightMove(mazeDataF2, xF2, yF2):
    """Vérifie si un mouvement à droite est possible

    IN
        x : int | abscisse de la case à vérifier
        y : int | largeur du labyrinthe
        mazeDataF1 : tableau de tableau de cases | labyrinthe

    OUT
        res : boolean
    """
    res = True
    if xF2 < len(mazeDataF2): 
        if mazeDataF2[xF2+1][yF2]["set"]: #Si la case de droite est définie, il y a un mouvement de moins possible
            res = False
    else: #Si la case est tout à droite, il y a un mouvement de moins possible
        res = False

    return res

def checkUpMove(mazeDataF2, xF2, yF2):
    """Vérifie si un mouvement en haut est possible

    IN
        x : int | abscisse de la case à vérifier
        y : int | largeur du labyrinthe
        mazeDataF1 : tableau de tableau de cases | labyrinthe

    OUT
        res : boolean
    """
    res = True
    if yF2 > 0: 
        if mazeDataF2[xF2][yF2-1]["set"]: #Si la case du haut est définie, il y a un mouvement de moins possible
            res = False
    else: #Si la case est tout en haut, il y a un mouvement de moins possible
        res = False

    return res

def checkDownMove(mazeDataF2, xF2, yF2):
    """Vérifie si un mouvement en bas est possible

    IN
        x : int | abscisse de la case à vérifier
        y : int | largeur du labyrinthe
        mazeDataF1 : tableau de tableau de cases | labyrinthe

    OUT
        res : boolean
    """
    res = True
    if yF2 < len(mazeDataF2[0]): 
        if mazeDataF2[xF2][yF2+1]["set"]: #Si la case du bas est définie, il y a un mouvement de moins possible
            res = False
    else: #Si la case est tout en bas, il y a un mouvement de moins possible
        res = False

    return res
    
            
def randomizeList(liste):
    """Mélange la liste"""

    res = liste

    def swap(i1, i2):
        """Inverse 2 élément dans une liste"""
        save = res[i1]
        res[i1] = res[i2]
        res[i2] = save

    for i in range(0,len(liste)-2):
        swap(i, random.randint(i+1, len(liste)-1))

    return res
