'''
Created on Jan 3, 2018

@author: cdtafoya
'''
from Map import Component
from Map import Map
from Map import Pin
import Router

def makeSpace(x,y):
    space = []
    for i in range(x):
        space.append([])
        for j in range(y):
            space[i].append(' -')

    return space

def printMap(Map):
    """Print Map given in console.

    Map -- must be numpy.ndarray type
    """

    # Print column number line
    print(' =  ', end='')
    for i in range(0, len(Map)):
        if i < 10:
            print (' ' + str(i), end='')
        else:
            print(i, end='')
    print()

    # Print extra line
    for i in range(0, len(Map) + 2):
        print ("  ", end='')
    print()

    # Print Map with row number
    for x in range(len(Map[0])):
        if x < 10:
            print (' ' + str(x) + '  ', end='')
        else:
            print (str(x) + '  ', end='')
        for y in range(len(Map)):
            print (Map[y][x], end='')
        print()

if __name__ == '__main__':
    pass

c3 = Component((3, 3), (3, 3))
cs =[]
cs.append(c3)

start_pins = []
terminal_pins = []

start_pins.append(Pin('S1', (2, 3)))
terminal_pins.append(Pin('T1', (2, 5)))
x = 9
y = 9
map1 = Map(x, y, cs, start_pins, terminal_pins)

print(map1.space[3])

space = makeSpace(x,y)

printMap(map1.space)

workMap = Router.makeWorkMap(map1.space)
workMap[0][1] = ' o'
printMap(workMap)
printMap(map1.space)

ground_pin = Pin('GND',(0,0))


