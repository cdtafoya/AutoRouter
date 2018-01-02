'''
Created on Sep 27, 2017

@author: Carlos
'''


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
                    
                    