import random
import math
import pygame

def player(x,y):
    screen.blit(playerUFO, (x,y))
def enemy(x,y,i):
    screen.blit(enemyUFO[i], (x,y))
def fire_laser(x,y):
    global laser_state
    laser_state = "fire"
    screen.blit(laserIMG,(x-2,y+5))
    screen.blit(laserIMG,(x+35,y+5))
def isCollision(enemyX,enemyY,laserX,laserY):
    destance= math.sqrt((math.pow(enemyX-laserX,2))+(math.pow(enemyY-laserY,2)))
    if destance<27:
        return True
    else:
        return False
def show_score(x,y):
    scoree=font.render("SCORE :"+str(score),True,(0,255,0))
    screen.blit(scoree,(x,y))
def game_over_text():
    over_text=over_font.render("GAME OVER",True,(255,0,0))
    screen.blit(over_text, (350, 300))
    
def restart_game():
    global playerX, playerY, playerX_change, enemyX, enemyY, enemyX_change, enemyY_change, score, laserX, laserY, laser_state, menuONOFF, menuESC
    
    playerX = 370
    playerY = 580
    playerX_change = 0
    
    for i in range(number_of_enemys):
        enemyX[i] = random.randint(0, 1216)
        enemyY[i] = random.randint(50, 200)
        enemyX_change[i] = 4
        enemyY_change[i] = 25

    laserX = 0
    laserY = 580
    laser_state = "ready"
    
    score = 0
    menuONOFF = False
    menuESC = 0
    
def main_menu(menuImg,x,y):
    global menuONOFF, menuESC
    screen.blit(menuImg, (x, y))
    font_title=pygame.font.Font("Alien Mine Italic.otf",50)
    font1=pygame.font.Font("Alien Mine Italic.otf", 20)
    font2=pygame.font.Font("conthrax-sb.otf", 20)
    title_menu=font_title.render("ATTACK IN SPACE",True,(0,255,0))
    screen.blit(title_menu,(300,100))
    creator=font2.render("by PrRed (apostolos petrokokkinos)",True,(255,0,0))
    screen.blit(creator,(300,680))
    pygame.draw.rect(screen, light_green, (450, 300, 300, 50))
    text_resume=font.render("RESUME",True,(250,250,250))
    screen.blit(text_resume,(500,305))
    pygame.draw.rect(screen, light_orange, (450, 400, 300, 50))
    text_restart=font.render("RESTART",True,(250,250,250))
    screen.blit(text_restart,(490,405))
    pygame.draw.rect(screen, light_red, (450, 500, 300, 50))
    text_Exit=font.render("EXIT",True,(250,250,250))
    screen.blit(text_Exit,(540,505))
    #RESUME BUTTON
    if 450 + 300 > mouse[0] > 450 and 300 + 50 > mouse[1] > 300: #x to prwto y to deytero                        
        pygame.draw.rect(screen, green, (450, 300, 300, 50))# X-Y-x-y
        text_resume=font.render("RESUME",True,(58,58,58))
        screen.blit(text_resume,(500,305))
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if menuESC == 0 :
                    menuONOFF=True
                    menuESC=1
                else:
                    menuONOFF=False
                    menuESC=0
                main_menu(menuImg, menuX, menuY)
    #EXIT BUTTON
    if 450 + 300 > mouse[0] > 450 and 500 + 50 > mouse[1] > 500:
        pygame.draw.rect(screen, red, (450, 500, 300, 50))
        text_Exit=font.render("EXIT",True,(58,58,58))
        screen.blit(text_Exit,(540,505))
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                pygame.quit()
    #RESTART GAME BUTTON (ayto den exei ginei akoma)
    if 450 + 300 > mouse[0] > 450 and 400 + 50 > mouse[1] > 400:
        pygame.draw.rect(screen, orange, (450, 400, 300, 50))
        text_restart = font.render("RESTART", True, (58, 58, 58))
        screen.blit(text_restart, (490, 405))
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                restart_game()
        

pygame.init()
#GameWindow1
screen =pygame.display.set_mode((1280,720))
#Background image
background=pygame.image.load('space2.jpg')

#Title&IconOnWindow
pygame.display.set_caption("Attack_In_Space")
icon=pygame.image.load('SpaceShipAlien.png')
pygame.display.set_icon(icon)

#COLORS
green=(0,250,0)
light_green=(0,150,0)
red=(250,0,0)
light_red=(150,0,0)
orange=(255,172,28)
light_orange=(204,85,0)


#MAIN MENU
menuImg=pygame.image.load("black.jpg")
menuX=276
menuY=-287
menuESC=0
menuONOFF=False

#PLAYER
playerUFO=pygame.image.load("1789873(2).png")
playerX=370
playerY=580
playerX_change=0

#ENEMY
enemyUFO=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
number_of_enemys=6
for i in range(number_of_enemys):
    enemyUFO.append(pygame.image.load("SpaceShipAlien.png"))
    enemyX.append(random.randint(0,900))
    enemyY.append(random.randint(50,200))
    enemyX_change.append(4)
    enemyY_change.append(25)

#LASER
laserIMG=pygame.image.load("red laser1.png")
laserX=0
laserY=580
laserX_change=0
laserY_change=10
laser_state = "ready" #ready-unvisble fire-moving

#SCORE
score=0
font=pygame.font.Font("Alien Mine Italic.otf",32)
textX=10
textY=10
difficulty_increase1=0.12
difficulty_increase2=-0.12

#GAME OVER FONT
over_font=pygame.font.Font("Alien Mine Italic.otf",64)

#GameLoop
running=True
while running:
    # RGBonWindow(background color)
    screen.fill((0, 0, 20))
    #Background Image
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        #KEYMAPING
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-2
                playerUFO = pygame.image.load("1789873(left).png")
            if event.key==pygame.K_RIGHT:
                playerX_change=2
                playerUFO = pygame.image.load("1789873(right).png")
            if event.key==pygame.K_SPACE:
                if laser_state == "ready":
                    laserX=playerX
                    fire_laser(laserX,laserY)
            if event.key==pygame.K_ESCAPE:
                if menuESC == 0 :
                    menuONOFF=True
                    menuESC=1
                else:
                    menuONOFF=False
                    menuESC=0
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0
                playerUFO = pygame.image.load("1789873(2).png")
    #MOUSE
    mouse=pygame.mouse.get_pos()
    #print(mouse)

    if menuONOFF is False: #PAUSE/UNPAUSE THE GAME
        #BORDER LIMITS

        playerX +=playerX_change
        if playerX <=0:
            playerX=0
        elif playerX >=1216:
            playerX=1216
        #ENEMY MOVEMENT

        for i in range(number_of_enemys):
            if enemyY[i]>440:
                for j in range(number_of_enemys):
                    enemyY[j]=2000
                game_over_text()
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <=0:
                enemyX_change[i] =0.5
                enemyY[i]+=enemyY_change[i]
            elif enemyX[i] >=1216:
                enemyX_change[i] =-0.5
                enemyY[i]+=enemyY_change[i]
                
            # Collision
            collision = isCollision(enemyX[i], enemyY[i], laserX, laserY)
            if collision:
                laserY = 580
                laser_state = "ready"
                score += 1
                enemyX[i] = random.randint(0, 1216)
                enemyY[i] = random.randint(50, 100)
            enemy(enemyX[i], enemyY[i],i)

        player(playerX, playerY)

        #LASER MOVEMENT
        if laserY<=0:
            laserY=580
            laser_state="ready"
        if laser_state == "fire":
            fire_laser(laserX,laserY)
            laserY-=laserY_change
        show_score(textX, textY)

    #MENU
    if menuONOFF is True:
        main_menu(menuImg, menuX, menuY)
    pygame.display.update()
