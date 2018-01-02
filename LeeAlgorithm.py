'''
Created on Aug 25, 2017

@author: Carlos
'''
from __future__ import print_function
import numpy
import sys
from point import point

if __name__ == '__main__':
    pass


def copyMap(Map):
    newMap = numpy.empty((len(Map), len(Map[0])), dtype=numpy.object)
    for i in range(len(Map)):
        for j in range(len(Map[0])):
            newMap[i][j] = Map[i][j]
    
    return newMap

def printMap(Map):

    print(' =  ', end='')
    for i in range(0, len(Map)):
        if i < 10:
            print (' ' + str(i), end='')
        else:
            print(i, end='')
    print()

    for i in range(0, len(Map)+2):
        print ("  ", end='')
    print()

    for x in range(len(Map[0])):
        if x < 10:
            print (' ' + str(x) + '  ', end='')
        else:
            print (str(x) + '  ', end='')
        for y in range(len(Map)):
            print (Map[y][x], end='')
        print()


def addComponent(x1, x2, y1, y2, cLetter, Map):
    print ("iin add componenct")
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            Map[i][j] = cLetter

def bubble(start, Map):

    workingPoints = []
    workingPoints.append(start)
    found = False
    iteration = 0
    temp = []
    c = 0
    iFound = None
    #sys.exit(0)
    while found is False:

        # print("iteration: " + str(iteration))
        
        for each in workingPoints:

            #print ("Working Point X: " + str(each.X) + " Y: " +str(each.Y))
            
            directions = []

            directions.append(point(each.X, each.Y - 1))  # above
            directions.append(point(each.X, each.Y + 1))  # below
            directions.append(point(each.X + 1, each.Y))  # right
            directions.append(point(each.X - 1, each.Y))  # left

            for dir in directions:

                if dir.X < 0 or dir.X > len(Map) - 1:
                    break
                if dir.Y < 0 or dir.Y >len(Map[0]) - 1:
                    break


                #print ("X: " + str(dir.X) + " Y: " +str(dir.Y))
                if Map[dir.X][dir.Y] == ' -':

                    if iteration < 10:
                        Map[dir.X][dir.Y] = " " + str(iteration)
                    #else:
                    #    Map[dir.X][dir.Y] =  str(iteration)
                    
                    temp.append(dir)
                    #print("----------------- True -------------------")

                if Map[dir.X][dir.Y] == ' T':
                    print (" Found at: "+ str(dir.X) + " , " + str(dir.Y))
                    found = True
                    iFound = iteration
                    break

        #=======================================================================
        # Here, if temp is empty, it means there are no more workingpoints
        # which means there is nowhere else to go and no path has been found.
        #=======================================================================
        workingPoints = temp
        temp = []

        #printMap(Map)
        #iteration += 1
        iteration = (iteration + 1) % 10

    return iFound, Map

def getNextPos(dir, cur, Map):
    
    if dir == 0:
        nextX = cur.X
        nextY = cur.Y -1
    elif dir == 1:
        nextX = cur.X +1
        nextY = cur.Y
    elif dir == 2:
        nextX = cur.X
        nextY = cur.Y +1
    elif dir == 3:
        nextX = cur.X -1
        nextY = cur.Y


    if nextX not in range(len(Map)) or nextY not in range(len(Map[0])):
        return -1, -1

    return nextX, nextY


def line (dir, current, label, Map):
    
    valid = True
    tracePoints = []
    tracePoints.append(current) # start by adding first point in line 

    print ("starting line w/ label: " +str(label))

    while valid is True:

        expectedLabel = (label - 1) % 10

        nextX, nextY = getNextPos(dir, current, Map)
        nextLabel = Map[nextX][nextY][1]

        print(type(nextLabel))
        print ( "expectedLabeL: " + str(expectedLabel) + " vs  actualLabeL: " + str(nextLabel))

        if nextLabel is  'S':
            print("Glorious has been found")
            # tracePoints.append(point(nextX, nextY))      # uncomment to include S point
            return tracePoints, True # return points collected, and goalFound = True

        if nextLabel.isdigit():

            nextLabel = int(nextLabel)

            if int(nextLabel) == expectedLabel:                tracePoints.append(point(nextX, nextY))
                current = point(nextX, nextY)
                label = nextLabel
            else:
                tracePoints += setDirection(current, label, Map)
                return tracePoints, True
                
        else:
            tracePoints += setDirection(current, label, Map)
            return tracePoints, True

def setDirection(turnPoint, label, Map):
    
    print ("Looking for direction at: " + str(turnPoint.X) + " , " + str(turnPoint.Y))
    directions = [0, 1, 2, 3]
    dirFound = False
    dir = 0 # start looking above start point
    expectedLabel = (label - 1) % 10
    tracePoints = []
    linePoints = []
    goalFound = False
    
    # while dirFound is False:
    for dir in directions:
        
        print ("dir: " + str(dir))
        
        startX, startY = getNextPos(dir, turnPoint, Map)
        actualLabel = Map[startX][startY][1]
        # print (type(actualLabel))
        
        print ("start X and Y: " + str(startX) + ", " + str(startY))
        print ("actualLabel: " + str(actualLabel))
        
        if startX == -1: # if next point exceeds limits, then try next direction
            print ("exceeds limits")
            continue
        
        if not actualLabel.isdigit(): # if next point is not a number, then we cannot go through it, and try next direction
            print (" not number")
            continue
        else: 
            actualLabel = int(actualLabel)
            
        
        if actualLabel != expectedLabel: #if next point is not a step closer to the origin, try next direction
            print ("expectedLabel: "+ str(expectedLabel))
            continue
        
        print ("Success!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        linePoints, goalFound = line(dir, point(startX, startY), actualLabel, Map)
        print("size of linepoitns reutrned: " + str(len(linePoints)))
        tracePoints += linePoints
        
        if goalFound is True:
            print ("Set Direction has been found part")
            break
        
    return tracePoints
            
        
    
def trace(end, label, Map):
    
    print ("in trace method")
    tracePoints = setDirection(end, label, Map)
    
    return tracePoints

def orderSets(S, T):
    
    print ("in order sets")
    pinsInBox = [0] * len(S)
    for i, each in enumerate(S):
        
        for j in xrange(len(S) - 1):
    
            j = (i + j + 1) % len(S)
            
            xs = S[i].X
            ys = S[i].Y
            xt = T[i].X
            yt = T[i].Y
            
            print ("looking at point with coordinates")
            print ("S "  + str(xs) + " " + str(ys))
            print("T " + str(xt)+ " " + str(yt))
            
            if xs > xt:
                stepX = -1
            else:
                stepX = 1
                
            if ys > yt:
                stepY = -1
            else:
                stepY = 1
                
            if S[j].X in xrange(xs, xt + stepX, stepX) and S[j].Y in xrange(ys, yt + stepY, stepY):
                pinsInBox[i] += 1
                
            if T[j].X in xrange(xs, xt + stepX, stepX) and T[j].Y in xrange(ys, yt + stepY, stepY):
                pinsInBox[i] += 1

    for idx, p in enumerate(pinsInBox):
        print( "Set "+str(idx)+ " has inside of it pins: " +str(p))
        
    #===========================================================================
    # Insert Sort, Depending on whteher i want to maintain the pins initial IDs,
    # The part inside the if clause should change so as to only keep track of the order
    # and not actually move the pinds around
    #===========================================================================

    for index, each in enumerate(pinsInBox):
        while index > 0:
            if pinsInBox[index] < pinsInBox[index - 1]:

                pinsInBox[index], pinsInBox[index - 1] = pinsInBox[index - 1], pinsInBox[index]

                S[index], S[index - 1] = S[index - 1], S[index]
                T[index], T[index - 1] = T[index - 1], T[index]

            index += -1
    print( "_--------")
    for each in pinsInBox:
        print (each)
    for i in xrange(len(S)):
        print(str(S[i].X) + "  " + str(S[i].Y))
        print(str(T[i].X) + "  " + str(T[i].Y))
    #sys.exit(0)

    return S, T
        
Map = numpy.empty((40, 30), dtype=numpy.object)

Map.fill(' -')

addComponent(16, 23, 3, 12, ' o', Map)
#addComponent(11, 15, 16, 29, ' o', Map)
addComponent(3, 9, 17, 26, ' o', Map)
addComponent(26, 35, 16, 25, ' o', Map)

printMap(Map)

# Start Points
S1 = point(2, 2)
S2 = point(33, 3)
S3 = point(5, 16)
S4 = point(10, 25)
S5 = point(13, 20)
S6 = point(5, 5)

# Terminal Points
T1 = point(23, 23)
T2 = point(10, 10)
T3 = point(33, 29)
T4 = point(39, 29)
T5 = point(26, 6)
T6 = point(34, 8)

Ss = []
Ss.append(S1)
Ss.append(S2)
Ss.append(S3)
Ss.append(S4)
Ss.append(S5)
Ss.append(S6)

Ts = []
Ts.append(T1)
Ts.append(T2)
Ts.append(T3)
Ts.append(T4)
Ts.append(T5)
Ts.append(T6)

for i in xrange(len(Ss)):
    Map[Ss[i].X][Ss[i].Y] = 'S' + str(i+1)
    Map[Ts[i].X][Ts[i].Y] = 'T' + str(i+1)
    
printMap(Map)

s2, t2 = orderSets(Ss, Ts)

for i in xrange(len(Ss)):
    Map[Ss[i].X][Ss[i].Y] = 'S' + str(i+1)
    Map[Ts[i].X][Ts[i].Y] = 'T' + str(i+1)
    
printMap(Map)

for i in range(len(Ss)):
    
    WorkMap = copyMap(Map)
    
    WorkMap[Ss[i].X][Ss[i].Y] = ' S'
    WorkMap[Ts[i].X][Ts[i].Y] = ' T'

    # printMap(Map)
    
    iFound, WorkMap = bubble(Ss[i], WorkMap)
    
    printMap(WorkMap)
    
    points = trace(Ts[i], iFound, WorkMap)

    for p in points:
        #Map[p.X][p.Y] = str(i) +'c'
        Map[p.X][p.Y] = ' c'
        
    printMap(Map)
    
printMap(Map)




