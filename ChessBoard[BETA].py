#imports

import pygame
from pygame import mixer

from math import ceil

import random

from Pieces_BETA import*
from Text_BETA import*

#Phase Structure is as follows:
#Phase 0: Choose Piece
#Phase 1: Choose Square
#Phase 2: Press "READY!"
#Phase 3: Watch piece jump around
#Phase 4: Piece is back to original square, have option to choose piece (Phase 1), choose square (Phase 2) or quit

#Phase functions go here
def phase0():
    displaySelection()
    select = Text("freesansbold.ttf",32,(0,0,0),"Select a piece from below:")
    screen.blit(select.rendered,(900,600))
def phase1(piece):
    #So that the player can change their mind on what piece they want
    phase0()
    
    #text that will show regardless of piece
    squareSelect = Text("freesansbold.ttf",32,(0,0,0),"Then, select the starting square on the board.")
    screen.blit(squareSelect.rendered,(850,660))
    instruc = Text("freesansbold.ttf",32,(0,0,0),"The piece will choose its next (viable) square at random.")
    instruc2 = Text("freesansbold.ttf",32,(0,0,0),"It will do this until it returns to its starting square.")
    screen.blit(instruc.rendered,(810,170))
    screen.blit(instruc2.rendered,(810,200))
    
    #display a message based on what piece type it is
    if type(piece) == Knight:
        title = Text("freesansbold.ttf",50,(0,0,0),"KNIGHT:")
        info = Text("freesansbold.ttf",32,(0,0,0),"The knight will move in an L-shape.")
    if type(piece) == Rook:
        title = Text("freesansbold.ttf",50,(0,0,0),"ROOK:")
        info = Text("freesansbold.ttf",32,(0,0,0),"The rook will move along its row or column")
    if type(piece) == Bishop:
        title = Text("freesansbold.ttf",50,(0,0,0),"BISHOP:")
        info = Text("freesansbold.ttf",32,(0,0,0),"The bishop will move along its diagonal(s).")
    if type(piece) == Queen:
        title = Text("freesansbold.ttf",50,(0,0,0),"QUEEN:")
        info = Text("freesansbold.ttf",32,(0,0,0),"The queen will move along its row, column, or diagonal(s).")
    if type(piece) == King:
        title = Text("freesansbold.ttf",50,(0,0,0),"KING:")
        info = Text("freesansbold.ttf",32,(0,0,0),"The king will move to an adjacent square.")
    screen.blit(title.rendered,(810,100))
    screen.blit(info.rendered,(810,140))

def phase2(piece):
    #we still want to see the description
    phase1(piece)
    
    #we see the piece on a square in the board
    displayPiece(piece)
    
    #blue ready button and ready text
    screen.fill((0,0,255),(1000,400,210,50))
    ready = Text("freesansbold.ttf",50,(255,255,255),"READY!")
    screen.blit(ready.rendered,(1000,400))
    
    clickButton = Text("freesansbold.ttf",32,(0,0,0),"Click the button to begin:")
    screen.blit(clickButton.rendered,(1000,360))
    
    for i in piece.viable_moves():
        colorSquare(i,(0,255,0))

def phase3(piece):
    randomMovement(piece)
    num_of_moves.set_value(num_of_moves.get_value() + 1)
    screen.blit(num_of_moves.rendered,(1300,0))
def phase4(piece):
    displayPiece(piece)
    screen.blit(num_of_moves.rendered,(1300,0))
    

#Conversions from pixel to board coordinates
#   (and vice versa)
def squareToPixel(squareValue):
    x = squareValue[0]
    y = squareValue[1]
    pixelX = (x - 1) * 100 + 18
    pixelY = (y - 1) * 100 + 18
    return (pixelX, pixelY)
print(squareToPixel((1,1)))
def pixelToSquare(pixels):
    return (roundCell(pixels[0]), roundCell(pixels[1]))

def roundCell(coordinate):
    coordinate /= 100
    coordinate = ceil(coordinate)
    return coordinate



#Displaying Functions
def displayPiece(piece):
    #displays piece on the board
    screen.blit(piece.icon,(squareToPixel(piece.currentSquare)))
def randomMovement(piece):
    #piece moves to a random square based on viable moves
    nextPlace = random.choice(piece.viable_moves())
    piece.setCurrentSquare(nextPlace)
    displayPiece(piece)

def displaySelection():
    #displays the selection of pieces; doesn't happen during phase 3
    screen.blit(pygame.image.load("knight.png"),squareToPixel((11,8)))
    screen.blit(pygame.image.load("bishop.png"),squareToPixel((12,8)))
    screen.blit(pygame.image.load("rook.png"),squareToPixel((10,8)))
    screen.blit(pygame.image.load("king.png"),squareToPixel((13,8)))
    screen.blit(pygame.image.load("queen.png"),squareToPixel((14,8)))
    

def drawBlank():
    #draws chessboard
    screen.fill((0,0,0))
    for i in range(4):
        for j in range(4):
            for k in range(2):
                pygame.draw.rect(
                    screen, (255,255,255), (i * 200 + k * 100, j * 200 + k * 100, 100, 100))
def colorSquare(square,color):
    #takes a square and colors it
    topLeftX = (square[0] - 1)*100 + 10
    topLeftY = (square[1] - 1)*100 + 10
    screen.fill(color,(topLeftX,topLeftY,80,80))

#pixels in bounds
def pixelInDisplay(pixel):
    #determines if a click determines a choice in a chess piece
    square_version = pixelToSquare(pixel)
    return ((10<=square_version[0]<=14) and (8==square_version[1]))
def isInBounds(coordinate):
    #determines if a coordinate is in bounds
    return ((1 <= coordinate[0] <= 8) and (1 <= coordinate[1] <= 8))
def pixelInBoard(pixel):
    squareversion = pixelToSquare(pixel)
    return isInBounds(squareversion)

#Initializing
pygame.init()
screen = pygame.display.set_mode((1800,800))
pygame.display.set_caption("Markov Chess")
running = True
inPhase0 = True
inPhase1 = False
inPhase2 = False
inPhase3 = False
inPhase4 = False

knight = Knight(1,1)

num_of_moves = TextAndNumber("freesansbold.ttf",50,(0,0,0),"Moves: ")
myliking = 0
while True:
    
    #Setting up the screen window
    drawBlank()
    screen.fill((239,222,205),(800,0,1000,800))
    displaySelection()
    
    #Checking clicks
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        
        #choosing a piece
        if ((event.type == pygame.MOUSEBUTTONDOWN) and (inPhase3 == False)):
            if pixelInDisplay(pygame.mouse.get_pos()):
                if inPhase0:
                    inPhase0 = False
                    inPhase1 = True
                if pixelToSquare(pygame.mouse.get_pos()) == (10,8):
                    currentPiece = Rook(0,0)
                elif pixelToSquare(pygame.mouse.get_pos()) == (11,8):
                    currentPiece = Knight(0,0)
                elif pixelToSquare(pygame.mouse.get_pos()) == (12,8):
                    currentPiece = Bishop(0,0)
                elif pixelToSquare(pygame.mouse.get_pos()) == (13,8):
                    currentPiece = King(0,0)
                elif pixelToSquare(pygame.mouse.get_pos()) == (14,8):
                    currentPiece = Queen(0,0)
                if inPhase2:
                    currentPiece.setCurrentSquare(daSquare)
        #choosing a starting square
        if ((event.type == pygame.MOUSEBUTTONDOWN) and (inPhase1 or inPhase2)):
            if pixelInBoard(pygame.mouse.get_pos()):
                inPhase1 = False
                inPhase2 = True
                daSquare = pixelToSquare(pygame.mouse.get_pos())
                currentPiece.setCurrentSquare(daSquare)
        #clicking the "READY!" button
        if ((event.type == pygame.MOUSEBUTTONDOWN) and (inPhase2)):
            if (1000 <= pygame.mouse.get_pos()[0] <= 1210) and (400 <= pygame.mouse.get_pos()[1] <= 450):
                inPhase2 = False
                inPhase3 = True
                num_of_moves.set_value(0)
            
                
                
    
    #Runs through the phases
    if inPhase0:
        phase0()
    if inPhase1:
        phase1(currentPiece)
    if inPhase2:
        phase2(currentPiece)
        if myliking == 1:
            screen.blit(num_of_moves.rendered,(1300,0))
    if inPhase3:
        myliking = 1
        phase3(currentPiece)
        inPhase3 = (currentPiece.getCurrentSquare()!=daSquare) or (num_of_moves.get_value()==0)
        
        if inPhase3 == False:
            inPhase2 = True
    if inPhase4:
        phase4(currentPiece)
        
        
    
    
    
    pygame.display.update()
    
    