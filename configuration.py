import pygame as pg
from random import randint

# Initializing Pygame
pg.init()

# Importing required images
seabg = pg.image.load('assets/seabg.png')
grass = pg.image.load('assets/grass.png')
brown = pg.image.load('assets/grassborder.png')
end = pg.image.load('assets/END.png')
gameover = pg.image.load('assets/gameover.png')
gamestart=pg.image.load('assets/gamestartbg.png')
p1cont=pg.image.load('assets/p1cont.png')
p2cont=pg.image.load('assets/p2cont.png')
icon=pg.image.load('assets/icon.png')

# Initializing the fonts
font1 = pg.font.Font('assets/comicsansms.ttf', 25)
font2 = pg.font.Font('assets/courier.ttf', 25)
font3 = pg.font.Font('assets/algerian.ttf', 40)
font4 = pg.font.Font('assets/comicsansms.ttf', 40)

# Creating a list to check which row player is on
row=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
rowcross=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Initializing player 1
player1img = pg.image.load('assets/player1.png')
p1wins = 0
player1X = 380
player1ch = 0
player1Y = 610
player1disp = True
scorep1 = 0
p1scorelist=[]
p1play = 0
p1crash = False

# Initializing player 2
player2img = pg.image.load('assets/player2.png')
p2wins = 0
player2X = 380
player2ch = 0
player2Y = 80
player2disp = True
scorep2 = 0
p2scorelist=[]
p2play = 0
p2crash = False

# Initializing ships
shipY = [545, 439, 333, 227, 121]
boatY = [545, 439, 333, 227, 121]
shipimg = [ ]
boatimg = [ ]
shipX = [ ]
boatX = [ ]
shipspeed = [2, 2, 2, 2, 2]
boatspeed = [3, 3, 3, 3, 3]
for i in range(0, 5):
    shipimg.append(pg.image.load('assets/ship.png'))
    shipX.append(randint(10, 550))
    boatimg.append(pg.image.load('assets/boat.png'))
    if shipX[i] - 500 >= 0:
        boatX.append(shipX[i] - 500)
    else:
        boatX.append(shipX[i] + 500)

# Initializing rocks
rockimg = pg.image.load('assets/cave.png')
rockimg = pg.transform.scale(rockimg, (55, 55))
rockY = [595, 489, 383, 277, 171, 489, 383, 277, 171, 65]
rockX = [ ]
for i in range(0, 10):
    if rockY[i] == 595 or rockY[i] == 65:
        while True:
            rock = randint(0, 730)
            if rock > 450 or rock < 310:
                rockX.append(rock)
                break
    else:
        rockX.append(randint(0, 730))

# Miscellaneous
rowY = [610, 557, 504, 451, 398, 345, 292, 239, 186, 133, 80]
grassY = [610, 500, 394, 288, 182, 76]
brownY = [650, 610, 540, 500, 434, 394, 328, 288, 222, 182, 116, 76]
gameovervar = False
gameloop = True
roundplay = 1
game_start = False