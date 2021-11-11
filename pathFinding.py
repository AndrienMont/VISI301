import labyrinthe as laby

def pathFinding(maze, start, end):

    mazeVectors = [[(0,0) for i in range(0, len(maze[0]))] for i in range(0, len(maze))]
    activeTiles = [end]
    trouve = False

    while not trouve:
        for tile in activeTiles:
            if tile == start:
                trouve = True

        
        newActiveTiles = []
        for tile in activeTiles:
            x = tile[0]
            y = tile[1]
            if not laby.yAMur(maze, x, y, "left"):
                if not (mazeVectors[x-1][y] != (0,0) or mazeVectors[x-1][y] == end):
                    mazeVectors[x-1][y] = (1,0)
                    newActiveTiles.append((x-1, y))
            if not laby.yAMur(maze, x, y, "right"):
                if not (mazeVectors[x+1][y] != (0,0) or mazeVectors[x+1][y] == end):
                    mazeVectors[x+1][y] = (-1,0)
                    newActiveTiles.append((x+1, y))
            if not laby.yAMur(maze, x, y, "up"):
                if not (mazeVectors[x][y-1] != (0,0) or mazeVectors[x][y-1] == end):
                    mazeVectors[x][y-1] = (0,1)
                    newActiveTiles.append((x, y-1))
            if not laby.yAMur(maze, x, y, "down"):
                if not (mazeVectors[x][y+1] != (0,0) or mazeVectors[x][y+1] == end):
                    mazeVectors[x][y+1] = (0,-1)
                    newActiveTiles.append((x, y+1))
        activeTiles = newActiveTiles

    res = []
    currentTile = start
    while currentTile != end:
        res.append(currentTile)
        
        x = currentTile[0]
        y = currentTile[1]
        currentTile = (x + mazeVectors[x][y][0], y + mazeVectors[x][y][1])
    res.append(end)
    
    return res
