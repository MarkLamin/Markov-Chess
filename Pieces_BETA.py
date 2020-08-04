import pygame

class Piece:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.currentSquare = (x,y)
    
    #Accessors and Mutators for currentSquare
    def getCurrentSquare(self):
        #returns a tuple of where knight is now (in x,y coordinates)
        return self.currentSquare
    def setCurrentSquare(self,square):
        self.currentSquare = square
        self.x = square[0]
        self.y = square[1]
        
class Knight(Piece):
    
    def __init__(self,x,y):
        Piece.__init__(self,x,y)
        self.icon = pygame.image.load("knight.png")
    
    def viable_moves(self):
        x = self.x
        y = self.y
        #returns a list of coordinates to where the piece could theoretically go based on where it is right now
        #is differentiated by class type
        
        #we will return this
        movesList = []
        
        #if the chess board were infinite
        theoretical = [(x+2,y+1),(x+2,y-1),(x+1,y+2),(x+1,y-2),(x-1,y+2),(x-1,y-2),(x-2,y+1),(x-2,y-1)]
        
        #checks for restrictions
        for spot in theoretical:
            if isInBounds(spot):
                movesList.append(spot)
        
        return movesList

class King(Piece):
    
    def __init__(self,x,y):
        Piece.__init__(self,x,y)
        self.icon = pygame.image.load("king.png")
    
    def viable_moves(self):
        x = self.x
        y = self.y
        #returns a list of coordinates to where the piece could theoretically go based on where it is right now
        #is differentiated by class type
        
        #we will return this
        movesList = []
        
        #if the chess board were infinite
        theoretical = [(x,y+1),(x+1,y+1),(x+1,y),(x+1,y-1),(x,y-1),(x-1,y-1),(x-1,y),(x-1,y+1)]
        
        #checks for restrictions
        for spot in theoretical:
            if isInBounds(spot):
                movesList.append(spot)
        
        return movesList

class Rook(Piece):
    def __init__(self,x,y):
        Piece.__init__(self,x,y)
        self.icon = pygame.image.load("rook.png")
    
    def viable_moves(self):
        x = self.x
        y = self.y
        #returns a list of coordinates to where the piece could theoretically go based on where it is right now
        #is differentiated by class type
        
        #we will return this
        movesList = []
        
        #if the chess board were infinite
        theoretical = theoreticalMovesR(x,y)
        
        #checks for restrictions
        for spot in theoretical:
            if isInBounds(spot):
                movesList.append(spot)
        
        return movesList

class Bishop(Piece):
    def __init__(self,x,y):
        Piece.__init__(self,x,y)
        self.icon = pygame.image.load("bishop.png")
    
    def viable_moves(self):
        x = self.x
        y = self.y
        #returns a list of coordinates to where the piece could theoretically go based on where it is right now
        #is differentiated by class type
        
        #we will return this
        movesList = []
        
        #if the chess board were infinite
        theoretical = theoreticalMovesB(x,y)
        
        #checks for restrictions
        for spot in theoretical:
            if isInBounds(spot):
                movesList.append(spot)
        
        return movesList
    
class Queen(Piece):
    def __init__(self,x,y):
        Piece.__init__(self,x,y)
        self.icon = pygame.image.load("queen.png")
    
    def viable_moves(self):
        x = self.x
        y = self.y
        #returns a list of coordinates to where the piece could theoretically go based on where it is right now
        #is differentiated by class type
        
        #we will return this
        movesList = []
        
        #if the chess board were infinite
        theoretical = theoreticalMovesQ(x,y)
        
        #checks for restrictions
        for spot in theoretical:
            if isInBounds(spot):
                movesList.append(spot)
        
        return movesList
    
def theoreticalMovesR(x,y):
    #returns a list of theoretical coordinates based on row/column
    #intentionally does not include (x,y)
    
    #we will return this list
    theList = []
    
    #adding everything in the same row
    for i in range(1,9):
        if i!= x:
            theList.append((i,y))
    
    for j in range(1,9):
        if j!=y:
            theList.append((x,j))
    
    return theList
   
def theoreticalMovesB(x,y):
    #returns a list of theoretical coordinates based on the diagonal(s)
    #intentionally does not include x or y
    #range is always 7 as that is the max length of a diagonal
    
    #return this
    theList = []
    
    i=x
    j=y
    
    #checks up-right direction
    for k in range(7):
        i += 1
        j += 1
        if ((0<i<9) and (0<j<9)):
            theList.append((i,j))
    
    i=x
    j=y
    
    #checks up-left direction
    for k in range(7):
        i -= 1
        j += 1
        if ((0<i<9) and (0<j<9)):
            theList.append((i,j))
    
    i=x
    j=y
    
    #checks down-right direction
    for k in range(7):
        i+=1
        j-=1
        if ((0<i<9) and (0<j<9)):
            theList.append((i,j))
    
    i=x
    j=y
    
    #checks down-left direction
    for k in range(7):
        i-=1
        j-=1
        if ((0<i<9) and (0<j<9)):
            theList.append((i,j))
    
    return theList 
        
def theoreticalMovesQ(x,y):
    #theoretical moves for the queen
    
    #return this
    theList = []
    
    for item in theoreticalMovesR(x,y):
        theList.append(item)
    for item in theoreticalMovesB(x,y):
        theList.append(item)
    return theList
            
def isInBounds(coordinate):
    #determines if a coordinate is in bounds
    return ((1 <= coordinate[0] <= 8) and (1 <= coordinate[1] <= 8))
    
    