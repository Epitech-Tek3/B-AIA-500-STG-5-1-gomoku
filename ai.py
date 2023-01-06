
def sumArray(input):
    return sum(map(sum, input))

def sumLine(game, x, y):
    z = 0
    t = 0
    if (x < 0):
        z = x - x*2
        x = 0
    if (x > len(game) - 5):
        t = x - (len(game) - 5)
    
    a = 0
    tmpVal = 0
    nbOccur = 0
    for i in range(x, x + 5 - t - z):
        a += game[y][i]

    return a

def sumCol(game, x, y):
    z = 0
    t = 0
    if (y < 0):
        z = y - y*2
        y = 0
    if (y > len(game) - 5):
        t = y - (len(game) - 5)
    
    a = 0
    for i in range(y, y + 5 - t - z):
        a += game[i][x]

    return a

def sumDiag1(game, x, y):
    a = 0
    b = 0
    c = 0
    d = 0
    if (y < 0):
        a = y - y*2
    if (y > len(game) - 5):
        b = y - (len(game) - 5)

    if (x < 0):
        c = x - x*2
    if (x > len(game) - 5):
        d = x - (len(game) - 5)
    
    e = 0
    for i, j in zip(range(y + c, y + 5 - b - d), range(x + a, x + 5 - d - b)):
        e += game[i][j]

    return e

def sumDiag2(game, x, y):
    a = 0
    b = 0
    c = 0
    d = 0
    if (y < 0):
        a = y - y*2
        y = 0
    if (y > len(game) - 5):
        b = y - (len(game) - 5)

    if (x < 4):
        c = 4 - x
    if (x >= len(game)):
        d = x - len(game)
        x = len(game) - 1
    
    e = 0
    for i, j in zip(range(y + d, y + 5 - a - b - c), range(x - a, x - 5 + c + d, -1)):
        e += game[i][j]

    return e

def attackLine(game, x, y):
    z = 0
    t = 0
    if (x < 0):
        z = x - x*2
        x = 0
    if (x > len(game) - 5):
        t = x - (len(game) - 5)
    
    a = 0
    b = 0
    count = 0
    for i in range(x + 4 - t - z, x - 1, -1):
        if (count == 1 and game[y][i] == 1):
            a += 1
            b = a
        if (count > 1):
            if (game[y][i] == 1 and a != 0):
                a += 1
                if (b < a):
                    b = a
            else:
                a = 0
        count += 1
    return b

def attackLineRight(game, x, y):
    z = 0
    t = 0
    if (x < 0):
        z = x - x*2
        x = 0
    if (x > len(game) - 5):
        t = x - (len(game) - 5)

    a = 0
    b = 0
    count = 0
    for i in range(x, x + 5 - t - z):
        if (count == 1 and game[y][i] == 1):
            a += 1
            b = a
        if (count > 1):
            if (game[y][i] == 1 and a != 0):
                a += 1
                if (b < a):
                    b = a
            else:
                a = 0
        count += 1
    return b

def attackCol(game, x, y):
    z = 0
    t = 0
    if (y < 0):
        z = y - y*2
        y = 0
    if (y > len(game) - 5):
        t = y - (len(game) - 5)
    
    a = 0
    b = 0
    count = 0
    for i in range(y + 4 - t - z, y - 1, -1):
        if (count == 1 and game[i][x] == 1):
            a += 1
            b = a
        if (count > 1):
            if (game[i][x] == 1 and a != 0):
                a += 1
                if (b < a):
                    b = a
            else:
                a = 0
        count += 1

    return b

def attackColRight(game, x, y):
    z = 0
    t = 0
    if (y < 0):
        z = y - y*2
        y = 0
    if (y > len(game) - 5):
        t = y - (len(game) - 5)
    
    a = 0
    b = 0
    count = 0
    for i in range(y, y + 5 - t - z):
        if (count == 1 and game[i][x] == 1):
            a += 1
            b = a
        if (count > 1):
            if (game[i][x] == 1 and a != 0):
                a += 1
                if (b < a):
                    b = a
            else:
                a = 0
        count += 1

    return b

def attackDiag1(game, x, y):
    a = 0
    b = 0
    c = 0
    d = 0
    if (y < 0):
        a = y - y*2
    if (y > len(game) - 5):
        b = y - (len(game) - 5)

    if (x < 0):
        c = x - x*2
    if (x > len(game) - 5):
        d = x - (len(game) - 5)
    
    e = 0
    f = 0
    count = 0
    for i, j in zip(range(y + 4 - b - d, y + c - 1, -1), range(x + 4 - d - b, x + a - 1, -1)):
        if (count == 1 and game[i][j] == 1):
            e += 1
            f = e
        if (count > 1):
            if (game[i][j] == 1 and e != 0):
                e += 1
                if (f < e):
                    f = e
            else:
                e = 0
        count += 1
    return f

def attackDiag1Right(game, x, y):
    a = 0
    b = 0
    c = 0
    d = 0
    if (y < 0):
        a = y - y*2
    if (y > len(game) - 5):
        b = y - (len(game) - 5)

    if (x < 0):
        c = x - x*2
    if (x > len(game) - 5):
        d = x - (len(game) - 5)
    
    e = 0
    f = 0
    count = 0
    for i, j in zip(range(y + c, y + 5 - b - d), range(x + a, x + 5 - d - b)):
        if (count == 1 and game[i][j] == 1):
            e += 1
            f = e
        if (count > 1):
            if (game[i][j] == 1 and e != 0):
                e += 1
                if (f < e):
                    f = e
            else:
                e = 0
        count += 1
    return f

def attackDiag2(game, x, y):
    a = 0
    b = 0
    c = 0
    d = 0
    if (y < 0):
        a = y - y*2
        y = 0
    if (y > len(game) - 5):
        b = y - (len(game) - 5)

    if (x < 4):
        c = 4 - x
    if (x >= len(game)):
        d = x - len(game)
        x = len(game) - 1
    
    e = 0
    f = 0
    count = 0
    for i, j in zip(range(y + 4 - a - b - c, y + d - 1, -1), range(x - 4 + c + d, x - a + 1)):
        if (count == 1 and game[i][j] == 1):
            e += 1
            f = e
        if (count > 1):
            if (game[i][j] == 1 and e != 0):
                e += 1
                if (f < e):
                    f = e
            else:
                e = 0
        count += 1

    return f

def attackDiag2Left(game, x, y):
    a = 0
    b = 0
    c = 0
    d = 0
    if (y < 0):
        a = y - y*2
        y = 0
    if (y > len(game) - 5):
        b = y - (len(game) - 5)

    if (x < 4):
        c = 4 - x
    if (x >= len(game)):
        d = x - len(game)
        x = len(game) - 1

    e = 0
    f = 0
    count = 0
    for i, j in zip(range(y + d, y + 5 - a - b - c), range(x - a, x - 5 + c + d, -1)):
        if (count == 1 and game[i][j] == 1):
            e += 1
            f = e
        if (count > 1):
            if (game[i][j] == 1 and e != 0):
                e += 1
                if (f < e):
                    f = e
            else:
                e = 0
        count += 1

    return f

def defenseLine(game, x, y):
    z = 0
    t = 0
    if (x < 0):
        z = x - x*2
        x = 0
    if (x > len(game) - 5):
        t = x - (len(game) - 5)
    
    a = 0
    b = 0
    count = 0
    for i in range(x + 4 - t - z, x - 1, -1):
        if (count == 1 and game[y][i] == 1000):
            a += 1
            b = a
        if (count > 1):
            if (game[y][i] == 1000 and a != 0):
                a += 1
                if (b < a):
                    b = a
            else:
                a = 0
        count += 1
    return b

def defenseLineRight(game, x, y):
    z = 0
    t = 0
    if (x < 0):
        z = x - x*2
        x = 0
    if (x > len(game) - 5):
        t = x - (len(game) - 5)

    a = 0
    b = 0
    count = 0
    for i in range(x, x + 5 - t - z):
        if (count == 1 and game[y][i] == 1000):
            a += 1
            b = a
        if (count > 1):
            if (game[y][i] == 1000 and a != 0):
                a += 1
                if (b < a):
                    b = a
            else:
                a = 0
        count += 1
    return b

def defenseCol(game, x, y):
    z = 0
    t = 0
    if (y < 0):
        z = y - y*2
        y = 0
    if (y > len(game) - 5):
        t = y - (len(game) - 5)
    
    a = 0
    b = 0
    count = 0
    for i in range(y + 4 - t - z, y - 1, -1):
        if (count == 1 and game[i][x] == 1000):
            a += 1
            b = a
        if (count > 1):
            if (game[i][x] == 1000 and a != 0):
                a += 1
                if (b < a):
                    b = a
            else:
                a = 0
        count += 1

    return b

def defenseColRight(game, x, y):
    z = 0
    t = 0
    if (y < 0):
        z = y - y*2
        y = 0
    if (y > len(game) - 5):
        t = y - (len(game) - 5)
    
    a = 0
    b = 0
    count = 0
    for i in range(y, y + 5 - t - z):
        if (count == 1 and game[i][x] == 1000):
            a += 1
            b = a
        if (count > 1):
            if (game[i][x] == 1000 and a != 0):
                a += 1
                if (b < a):
                    b = a
            else:
                a = 0
        count += 1

    return b

def defenseDiag1(game, x, y):
    a = 0
    b = 0
    c = 0
    d = 0
    if (y < 0):
        a = y - y*2
    if (y > len(game) - 5):
        b = y - (len(game) - 5)

    if (x < 0):
        c = x - x*2
    if (x > len(game) - 5):
        d = x - (len(game) - 5)
    
    e = 0
    f = 0
    count = 0
    for i, j in zip(range(y + 4 - b - d, y + c - 1, -1), range(x + 4 - d - b, x + a - 1, -1)):
        if (count == 1 and game[i][j] == 1000):
            e += 1
            f = e
        if (count > 1):
            if (game[i][j] == 1000 and e != 0):
                e += 1
                if (f < e):
                    f = e
            else:
                e = 0
        count += 1
    return f

def defenseDiag1Right(game, x, y):
    a = 0
    b = 0
    c = 0
    d = 0
    if (y < 0):
        a = y - y*2
    if (y > len(game) - 5):
        b = y - (len(game) - 5)

    if (x < 0):
        c = x - x*2
    if (x > len(game) - 5):
        d = x - (len(game) - 5)
    
    e = 0
    f = 0
    count = 0
    for i, j in zip(range(y + c, y + 5 - b - d), range(x + a, x + 5 - d - b)):
        if (count == 1 and game[i][j] == 1000):
            e += 1
            f = e
        if (count > 1):
            if (game[i][j] == 1000 and e != 0):
                e += 1
                if (f < e):
                    f = e
            else:
                e = 0
        count += 1
    return f

def defenseDiag2(game, x, y):
    a = 0
    b = 0
    c = 0
    d = 0
    if (y < 0):
        a = y - y*2
        y = 0
    if (y > len(game) - 5):
        b = y - (len(game) - 5)

    if (x < 4):
        c = 4 - x
    if (x >= len(game)):
        d = x - len(game)
        x = len(game) - 1
    
    e = 0
    f = 0
    count = 0
    for i, j in zip(range(y + 4 - a - b - c, y + d - 1, -1), range(x - 4 + c + d, x - a + 1)):
        if (count == 1 and game[i][j] == 1000):
            e += 1
            f = e
        if (count > 1):
            if (game[i][j] == 1000 and e != 0):
                e += 1
                if (f < e):
                    f = e
            else:
                e = 0
        count += 1

    return f

def defenseDiag2Left(game, x, y):
    a = 0
    b = 0
    c = 0
    d = 0
    if (y < 0):
        a = y - y*2
        y = 0
    if (y > len(game) - 5):
        b = y - (len(game) - 5)

    if (x < 4):
        c = 4 - x
    if (x >= len(game)):
        d = x - len(game)
        x = len(game) - 1

    e = 0
    f = 0
    count = 0
    for i, j in zip(range(y + d, y + 5 - a - b - c), range(x - a, x - 5 + c + d, -1)):
        if (count == 1 and game[i][j] == 1000):
            e += 1
            f = e
        if (count > 1):
            if (game[i][j] == 1000 and e != 0):
                e += 1
                if (f < e):
                    f = e
            else:
                e = 0
        count += 1

    return f

def checkZero(game, x, y):
    if (x >= 0 and x < 20 and y >= 0 and y < 20):
        if (game[y][x] == 0):
            return 1
    return 0
        

def checkWin(game):
    x = 0
    y = 0
    for line in game:
        x = 0
        for cell in line:
            if (cell == 0):
                for i, j, k in zip(range(x, x - 5, -1), range(y, y - 5, -1), range(x, x + 5)):
                    if (sumLine(game, i, y) % 1000 == 4):
                        return x, y
                    if (sumCol(game, x, j) % 1000 == 4):
                        return x, y
                    if (sumDiag1(game, i, j) % 1000 == 4):
                        return x, y
                    if (sumDiag2(game, k, j) % 1000 == 4):
                        return x, y
            x += 1
        y += 1
    return -1, -1

def checkLose(game):
    x = 0
    y = 0
    for line in game:
        x = 0
        for cell in line:
            if (cell == 0):
                for i, j, k in zip(range(x, x - 5, -1), range(y, y - 5, -1), range(x, x + 5)):
                    if (sumLine(game, i, y) == 4000):
                        return x, y
                    if (sumCol(game, x, j) == 4000):
                        return x, y
                    if (sumDiag1(game, i, j) == 4000):
                        return x, y
                    if (sumDiag2(game, k, j) == 4000):
                        return x, y
            x += 1
        y += 1
    
    x = 0
    y = 0
    for line in game:
        x = 0
        for cell in line:
            if (cell == 0):
                if (defenseLine(game, x - 4, y) == 3 and checkZero(game, x - 4, y) == 1):
                    return x, y
                if (defenseLineRight(game, x, y) == 3 and checkZero(game, x + 4, y) == 1):
                    return x, y
                if (defenseCol(game, x, y - 4) == 3 and checkZero(game, x, y - 4) == 1):
                    return x, y
                if (defenseColRight(game, x, y) == 3 and checkZero(game, x, y + 4) == 1):
                    return x, y
                if (defenseDiag1(game, x - 4, y - 4) == 3 and checkZero(game, x - 4, y - 4) == 1):
                    return x, y
                if (defenseDiag1Right(game, x, y) == 3 and checkZero(game, x + 4, y + 4) == 1):
                    return x, y
                if (defenseDiag2(game, x + 4, y - 4) == 3 and checkZero(game, x + 4, y - 4) == 1):
                    return x, y
                if (defenseDiag2Left(game, x, y) == 3 and checkZero(game, x - 4, y + 4) == 1):
                    return x, y
            x += 1
        y += 1
    return -1, -1

def move(boardGame):
    attackTab = []
    defenseTab = []
    for h in range(len(boardGame)):
        attackTab.append([])
        defenseTab.append([])
        for o in range(len(boardGame)):
            attackTab[h].append([])
            defenseTab[h].append([])
    x = 0
    y = 0
    a = 0
    b = 0
    if (sumArray(boardGame) == 0):
        return int(len(boardGame) / 2), int(len(boardGame) / 2)
    a, b = checkWin(boardGame)
    # print("MESSAGE ", boardGame)
    # print("MESSAGE tot line", sumLine(boardGame, -4, 0))
    # print("MESSAGE tot col", sumCol(boardGame, 0, -4))
    # print("MESSAGE tot diag1", sumDiag1(boardGame, -4, -4))
    # print("MESSAGE tot diag2", sumDiag2(boardGame, 4, -4))
    if (a != -1):
        print("MESSAGE youhou it works")
        return a, b
    a, b = checkLose(boardGame)
    if (a != -1):
        print("MESSAGE youhou it works great")
        return a, b
    for line in boardGame:
        x = 0
        for cell in line:
            if (cell == 0):
                attackTab[y][x].append(attackLine(boardGame, x - 4, y) + attackLineRight(boardGame, x, y))
                attackTab[y][x].append(attackCol(boardGame, x, y - 4) + attackColRight(boardGame, x, y))
                attackTab[y][x].append(attackDiag1(boardGame, x - 4, y - 4) + attackDiag1Right(boardGame, x, y))
                attackTab[y][x].append(attackDiag2(boardGame, x + 4, y - 4) + attackDiag2Left(boardGame, x, y))
                defenseTab[y][x].append(defenseLine(boardGame, x - 4, y) + defenseLineRight(boardGame, x, y))
                defenseTab[y][x].append(defenseCol(boardGame, x, y - 4) + defenseColRight(boardGame, x, y))
                defenseTab[y][x].append(defenseDiag1(boardGame, x - 4, y - 4) + defenseDiag1Right(boardGame, x, y))
                defenseTab[y][x].append(defenseDiag2(boardGame, x + 4, y - 4) + defenseDiag2Left(boardGame, x, y))
            x += 1
        y += 1
    maxValAttack = 0
    maxValDefense = 0
    y = 0
    z = 0
    for line in attackTab:
        x = 0
        for cell in line:
            z = 0
            for nb in cell:
                if (maxValDefense < defenseTab[y][x][z]):
                    maxValDefense = defenseTab[y][x][z]
                if (maxValAttack < attackTab[y][x][z]):
                    maxValAttack = attackTab[y][x][z]
                z += 1
            x += 1
        y += 1
    resX = 0
    resY = 0
    tmpCoor = []
    tmpOccur = 0
    OccurMax = 0
    y = 0
    z = 0
    isAttack = 0
    if (maxValDefense >= maxValAttack):
        for line in defenseTab:
            x = 0
            for cell in line:
                z = 0
                tmpOccur = 0
                for nb in cell:
                    if maxValDefense == defenseTab[y][x][z]:
                        tmpOccur += 1
                    z += 1
                if (tmpOccur == OccurMax):
                    tmpCoor.append((x, y))
                if (tmpOccur > OccurMax):
                    tmpCoor = []
                    tmpCoor.append((x, y))
                    resX = x
                    resY = y
                    OccurMax = tmpOccur
                x += 1
            y += 1
    else:
        isAttack = 1
        for line in attackTab:
            x = 0
            for cell in line:
                z = 0
                tmpOccur = 0
                for nb in cell:
                    if maxValAttack == attackTab[y][x][z]:
                        tmpOccur += 1
                    z += 1
                if (tmpOccur == OccurMax):
                    tmpCoor.append((x, y))
                if (tmpOccur > OccurMax):
                    tmpCoor = []
                    tmpCoor.append((x, y))
                    resX = x
                    resY = y
                    OccurMax = tmpOccur
                x += 1
            y += 1
    tmpVal = 0
    for (coorX, coorY) in tmpCoor:
        if (isAttack == 1):
            print("MESSAGE Attaque: ", coorX, coorY)
            if (sum(attackTab[coorY][coorX]) > tmpVal):
                tmpVal = sum(attackTab[coorY][coorX])
                resX = coorX
                resY = coorY
        else:
            print("MESSAGE Defense: ", coorX, coorY)
            if (sum(defenseTab[coorY][coorX]) > tmpVal):
                tmpVal = sum(defenseTab[coorY][coorX])
                resX = coorX
                resY = coorY
    print("MESSAGE END TURN")
    return resX, resY