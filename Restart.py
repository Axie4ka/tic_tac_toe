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
XO = -1  # -1 is X-player, 1 is O-player
move = None # numbers from 0 to 8
winner = None
turnX=0
turnO=0

text=""
a=[0, 0, 0, 0, 0, 0, 0, 0, 0]
def start():
    global XO, move, winner, turnX, turnO, text, a
    screen.blit(opening, (0, 0))
    XO = -1  # -1 is X-player, 1 is O-player
    move = None # numbers from 0 to 8
    winner = None
    turnX=0
    turnO=0
    text=""
    a=[0, 0, 0, 0, 0, 0, 0, 0, 0]
    pg.display.update()
def user_click(): # mouse click
    global move
    move = None
    # get coordinates of mouse click
    x, y = pg.mouse.get_pos()
    # get x,y of mouse click (cell 0-8)
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
def DrawXO(): # drawing of X or O, and after a sign will be reversed (XO => - XO) for player changing
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
def check():
    global a, winner, turnX, turnO
    if abs(a[0]+a[1]+a[2])==3:
        pg.draw.line(screen, black, (0,400//6), (400,400//6), width=15)
    elif abs(a[3]+a[4]+a[5])==3:
        pg.draw.line(screen, black, (0,400//6+400//3), (400,400//6+400//3), width=15)
    elif abs(a[6]+a[7]+a[8])==3:
        pg.draw.line(screen, black, (0,400//6+2*400//3), (400,400//6+2*400//3), width=15)
    elif abs(a[0]+a[3]+a[6])==3:
        pg.draw.line(screen, black, (400//6, 0), (400//6,400), width=15)
    elif abs(a[1]+a[4]+a[7])==3:
        pg.draw.line(screen, black, (400//6+400//3, 0), (400//6+400//3,400), width=15)
    elif abs(a[2]+a[5]+a[8])==3:
        pg.draw.line(screen, black, (400//6+2*400//3, 0), (400//6+2*400//3,400), width=15)
    elif abs(a[0]+a[4]+a[8])==3:
        pg.draw.line(screen, black, (0, 0), (400,400), width=15)
    elif abs(a[2]+a[4]+a[6])==3:
        pg.draw.line(screen, black, (400, 0), (0,400), width=15)
    
    if a[0]+a[1]+a[2]==3 or a[3]+a[4]+a[5]==3 or a[6]+a[7]+a[8]==3 or a[0]+a[3]+a[6]==3 or a[1]+a[4]+a[7]==3 or a[2]+a[5]+a[8]==3 or a[0]+a[4]+a[8]==3 or a[2]+a[4]+a[6]==3:
        winner=1
    elif a[0]+a[1]+a[2]==-3 or a[3]+a[4]+a[5]==-3 or a[6]+a[7]+a[8]==-3 or a[0]+a[3]+a[6]==-3 or a[1]+a[4]+a[7]==-3 or a[2]+a[5]+a[8]==-3 or a[0]+a[4]+a[8]==-3 or a[2]+a[4]+a[6]==-3:
        winner=-1
    elif turnX+turnO==9 and winner==None:
        winner=0
        print("draw")
    pg.display.update()
def check_winner():
    global winner, text
    f1 = pg.font.SysFont('Arial', 60)
    text1 = f1.render(text, 1, (180, 0, 0))
    if winner == -1:
        text="Победили X"
        screen.blit(text1, (70, 80))
    elif winner == 1:
        text="Победили O"
        screen.blit(text1, (70, 80))
    else:
        text="Ничья"
        screen.blit(text1, (120, 120))
    rect = pg.Rect(30, 175, 340, 60)
    pg.draw.rect(screen, (0,0,0), rect)
    img = f1.render("Начать заново", True, (255,255,255))
    screen.blit(img, (35, 170))
    pg.display.update()
    
screen.blit(opening, (0, 0))
pg.display.update()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        
        if event.type == pg.MOUSEBUTTONDOWN:
            user_click()  # click mouse button for Х's move
            if move == None:
                continue
            else:
                DrawXO()
                check()
        if winner != None:
            a=[2, 2, 2, 2, 2, 2, 2, 2, 2]
            check_winner()
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                if (175<y < 235) and (30<x < 370):
                    start()

