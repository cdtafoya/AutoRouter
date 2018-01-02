'''
Created on Jul 31, 2017

@author: Carlos
'''

class point:
    X = None
    Y = None

    def __init__(self, x, y):
        '''
        Constructor
        '''
        self.X = x
        self.Y = y
        self.pos = (x, y)

    def setX(self, x):
        self.X = x

    def setY(self, y):
        self.Y = y
