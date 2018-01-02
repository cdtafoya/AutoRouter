'''
Created on Sep 21, 2017

@author: Carlos
'''
from Map import Component
from Map import Map
from Pin import Pin
import numpy as np
from point import point
import sys
from builtins import type




class Pin(object):
    '''
    classdocs
    '''


    def __init__(self, name, position):
        '''
        Constructor
        '''
        self.name = name
        self.id = 0
        self.extension = 0 # Length of extension from component
        self.pos = position
        self.x = position[0]
        self.y = position[1]
        self.oppos = None # Points to Pin object that this Pin must connect to
        self.attached = True # Pin is attached to component

    def setExtension(self, direction):
        self.extension = direction
        
    def setPosition(self, position):
        self.pos = position

    def setOpposite(self, opposite):
        self.oppos = opposite
        
    def setAttached(self, attached):
        self.attached = attached
    
    def setX(self, x):
        self.pos = (x, self.y)
        self.x = x
        
    def setY(self, y):
        self.pos = (self.x, y)
        self.y = y   
        

def change(x):
    x[0][2] = 4
    
    return x

if __name__ == '__main__':
    
    p1 = Pin('S!', (2,5))
    print (p1.pos)
    p1.setX(3)
    print(p1.pos, p1.x)
    
    
    
    import numpy as np
    x = np.array([[1, 2, 3], [3,4,5]])
    x = change(x)
    print (x)
    
    #(1,0)
    #(1, 10)
    
    for i in range(0,10+1):
        for j in range(1,1 + 1):
            print (i,j)
    
    
    
    
    

