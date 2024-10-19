import pygame as pg
import sys

pg.init()
pg.display.set_caption('Крестики-нолики')
screen = pg.display.set_mode((400, 400))

white = (255, 255, 255)
black = (0, 0, 0)
width=400
height=400
opening = pg.image.load('pole.png')
x_img1 = pg.image.load('krest.png')
o_img1 = pg.image.load('nole.png')
x_img1 = pg.transform.scale(x_img1, (80, 80))
o_img1 = pg.transform.scale(o_img1, (80, 80))
x_img2 = pg.image.load('krest.png')
o_img2 = pg.image.load('nole.png')
x_img2 = pg.transform.scale(x_img2, (80, 80))
o_img2 = pg.transform.scale(o_img2, (80, 80))
x_img3 = pg.image.load('krest.png')
o_img3 = pg.image.load('nole.png')
x_img3 = pg.transform.scale(x_img3, (80, 80))
o_img3 = pg.transform.scale(o_img3, (80, 80))
x_img4 = pg.image.load('krest.png')
o_img4 = pg.image.load('nole.png')
x_img4 = pg.transform.scale(x_img4, (80, 80))
o_img4 = pg.transform.scale(o_img4, (80, 80))
x_img5 = pg.image.load('krest.png')
o_img5 = pg.image.load('nole.png')
x_img5 = pg.transform.scale(x_img5, (80, 80))
o_img5 = pg.transform.scale(o_img5, (80, 80))
X=[x_img1, x_img2, x_img3, x_img4, x_img5]
O=[o_img1, o_img2, o_img3, o_img4, o_img5]
opening = pg.transform.scale(opening, (400, 400))
XO = -1
move = None

turnX=0
turnO=0

a=[0, 0, 0, 0, 0, 0, 0, 0, 0]

def user_click():
    global move
    move = None
    x, y = pg.mouse.get_pos()
    if (y < height / 3) and (x < width / 3):
        move = 0
    elif (y < height / 3) and (x < width / 3 * 2):
        move = 1
    elif (y < height / 3) and (x < width):
        move = 2

    elif (y < height / 3 * 2) and (x < width / 3):
        move = 3
    elif (y < height / 3 * 2) and (x < width / 3 * 2):
        move = 4
    elif (y < height / 3 * 2) and (x < width):
        move = 5

    elif (y < height) and (x < width / 3):
        move = 6
    elif (y < height) and (x < width / 3 * 2):
        move = 7
    elif (y < height) and (x < width):
        move = 8
def DrawXO(): 
    global  XO, move, turnX,turnO, O, X, a
    
    if move == 0:
        posx = 30
        posy = 30
    if move == 1:
        posx = width / 3 + 30
        posy = 30
    if move == 2:
        posx = width / 3 * 2 + 30
        posy = 30

    if move == 3:
        posx = 30
        posy = height / 3 + 30
    if move == 4:
        posx = width / 3 + 30
        posy = height / 3 + 30
    if move == 5:
        posx = width / 3 * 2 + 30
        posy = height / 3 + 30

    if move == 6:
        posx = 30
        posy = height / 3 * 2 + 30
    if move == 7:
        posx = width / 3 + 30
        posy = height / 3 * 2 + 30
    if move == 8:
        posx = width / 3 * 2 + 30
        posy = height / 3 * 2 + 30
    if a[move]==0:
        if XO == -1:
            screen.blit(X[turnX], (posx, posy))
            turnX+=1
        else:
            screen.blit(O[turnO], (posx, posy))
            turnO+=1
        a[move]=XO
        XO = -1*XO
    pg.display.update()

    
screen.blit(opening, (0, 0))
pg.display.update()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        
        if event.type == pg.MOUSEBUTTONDOWN:
            user_click() 
            if move == None:
                continue
            else:
                DrawXO()
       

