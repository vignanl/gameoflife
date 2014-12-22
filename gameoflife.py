import pygame, sys
from pygame.locals import *
import random

FPS = 10

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 10

assert WINDOWWIDTH % CELLSIZE == 0
assert WINDOWHEIGHT % CELLSIZE == 0
CELLWIDTH = WINDOWWIDTH / CELLSIZE
CELLHEIGHT = WINDOWHEIGHT / CELLSIZE

BLACK = (0,0,0)
WHITE = (255,255,255)
DARKGRAY = (40,40,40)
GREEN = (0,255,0)

def drawgrid():
    for x in range(0,WINDOWWIDTH,CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x,0),(x,WINDOWHEIGHT))
    for y in range (0,WINDOWHEIGHT,CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0,y), (WINDOWWIDTH,y))


def blankgrid():
    gridDict = {}
    for y in range(CELLHEIGHT):
        for x in range(CELLWIDTH):
            gridDict[x,y] = 0

    
    return gridDict


def startrandom(lifeDict):

    for item in lifeDict:
        lifeDict[item] = random.randint(0,1)

    return lifeDict

def colorgrid(item, lifeDict):
    
    x = item[0]
    y = item[1]
    x = x * CELLSIZE
    y = y * CELLSIZE

    if lifeDict[item] == 0:
        pygame.draw.rect(DISPLAYSURF,WHITE,(x,y,CELLSIZE,CELLSIZE))
    if lifeDict[item] == 1:
        pygame.draw.rect(DISPLAYSURF,GREEN,(x,y,CELLSIZE,CELLSIZE))
    
    return None

def getneighbours(item,lifeDict):

    neighbours = 0

    for x in range(-1,2):
        for y in range(-1,2):
            checkcell = (item[0]+x, item[1]+y)
            if checkcell[0] >= 0 and checkcell[0] < CELLWIDTH:
                if checkcell[1] >= 0 and checkcell[1] < CELLHEIGHT:
                    if lifeDict[checkcell] == 1:
                        if x == 0 and y == 0:
                            neighbours += 0
                        else:
                            neighbours += 1
                            
                        
   
    return neighbours

def tick(lifeDict):

    newtick = {}
    
    for item in lifeDict:
        numberneighbour = getneighbours(item,lifeDict)
        if lifeDict[item] == 1:
            if numberneighbour < 2:
                newtick[item] = 0
            elif numberneighbour > 3:
                newtick[item] = 0
            else:
                newtick[item] = 1
          
        elif lifeDict[item] == 0:
            if numberneighbour == 3:
                newtick[item] = 1
            else:
                newtick[item] = 0
        

    return newtick

def main():
    pygame.init()
    global DISPLAYSURF
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption('Game of Life')

    DISPLAYSURF.fill(WHITE)

    lifeDict = blankgrid()
    lifedict = startrandom(lifeDict)


    for item in lifeDict:
        colorgrid(item,lifeDict)
    
    drawgrid()
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        lifeDict = tick(lifeDict)
        for item in lifeDict:
            colorgrid(item,lifeDict)

        drawgrid()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
    
