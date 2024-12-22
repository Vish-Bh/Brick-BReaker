import pygame
import random
import math
import numpy
tickpersec=60
count=0
complete=False
score=0
level = 0
width, height = 600, 800
widthpanel=60
balcol,tilescol=(255,165,0),(138,54,15)
scorecol,scoreback=(255,140,0),(85,107,47)
blackcol, whitecol, redcol, greencol, bluecol, goldcol,lavencol,stblue ,chicol= (40, 40, 40), (255, 255, 255), (205, 92, 92), (0, 255, 0), (0, 0, 255), (255,215,0), (235, 215, 195),(205,50,35),(240,240,240)
pygame.init()
alive = True
game_over = False
speedx, speedy = 1, 2
screen = pygame.display.set_mode((width, height))
scorepanel=pygame.Rect(0,0, width, height/10)
panel = pygame.Rect(0, 0, widthpanel, 10, border=2)
death = pygame.Rect(0, 99.8*height/100, width, 50)
panel.center = (width / 2, 0.95 * height)
welcomepanel=pygame.Rect(0, (height/2)-50, width, 13*height/100 )
gameball = pygame.Rect(random.randint(int(width/3),int( width/3+100)), random.randint(int(height/2)+50, int(height/2+50+50) ), 15, 15)
pygame.display.set_caption("A Game I Guess")
listo = []
obas = 0
clock = pygame.time.Clock()
levelclear=False


    
def panel1(): 
    global listo, level,count
    count=1
    for j in range(int(height/10+15), 300, 30):
        for i in range(0, 600, 60):
            obas = pygame.Rect(i, j, 55, 10)
            listo.append(obas)

def panel2(): 
    global listo, level, count
    count = 1
    for x,i in zip(range(10, width, 20), range(29)):
        obas=pygame.Rect(x, height/10+5, 19, 40)
        if i in range(5)or i in range(8, 13)or i in range(16, 21)or i in range(24,29):
            listo.append(obas)
    for x,i in zip(range(10, width, 20), range(29)):
        obas=pygame.Rect(x, height/10+5+40+5, 19, 40)
        if i in range(1,4)or i in range(9,12)or i in range(17, 20)or i in range(25,28):
            listo.append(obas)
    for x,i in zip(range(10, width, 20), range(29)):
        obas=pygame.Rect(x, height/10+5+40+5+40+5, 19, 40)
        if i==2 or  i==10 or i ==18 or i==26:
            listo.append(obas)   
    for x,i in zip(range(10, width, 20), range(29)):
        obas=pygame.Rect(x, height/10+5+40+5+40+5+45, 19, 40)
        listo.append(obas) 
    for x,i in zip(range(10, width, 20), range(29)):
        obas=pygame.Rect(x, height/10+5+40+5+40+5+90, 19, 40)
        if i in range(2,11) or i in range(18,27):
            listo.append(obas)
    for x,i in zip(range(10, width, 20), range(29)):
        obas=pygame.Rect(x, height/10+5+40+5+40+5+90+45, 19, 40)
        if i in range(4,9) or i in range(20,25):
            listo.append(obas)

def panel3(): 
    global listo, level,count
    count=1
    for x,i in zip(range(10, width, 20), range(29)):
        obas=pygame.Rect(x, height/10+5, 19, 40)
        if i ==12 or i== 13 or i==14 or i== 15 or i==16 or  i==11:
            continue
        else:
            listo.append(obas)
    for x,i in zip(range(10, width, 20), range(29)):
        obas=pygame.Rect(x, height/10+5+45, 19, 40)
        if i in range(9, 19):
            listo.append(obas)

    for x,i in zip(range(10, width, 20), range(29)):
        obas=pygame.Rect(x, height/10+5+90, 19, 40)
        if i in range(8)or i in range(23,29):
            listo.append(obas)
    for x,i in zip(range(10, width, 20), range(29)):
        obas=pygame.Rect(x, height/10+5+90+45, 19, 40)
        if i in range(6)or i in range(20,29):
            listo.append(obas)
    for x,i in zip(range(10, width, 20), range(29)):
        obas=pygame.Rect(x, height/10+5+90+90, 19, 40)
        if i in range(10)or i in range(22,29)or i in range(13,15):
            listo.append(obas)
    for x,i in zip(range(10, width, 20), range(29)):
        obas=pygame.Rect(x, height/10+5+90+90+45, 19, 40)
        if i in range(5)or i in range(18,29)or i in range(11,17):
            listo.append(obas)
    for x,i in zip(range(10, width, 20), range(29)):
        obas=pygame.Rect(x, height/10+5+90+90+90, 19, 40)
        if i in range(9,19):
            listo.append(obas)

def panel4(): 
    global listo, level, count
    count = 1
    for j in range(int(height/10+15), 350, 35):
        for i in range(0, 600, 40):
            obas = pygame.Rect(i, j, 40, 25)
            if random.choices([True, False], weights=[0.6, 0.4])[0]:
                listo.append(obas)

def panel5(): 
    global listo, level,count
    count=1
    for x,i in zip(range(10, width, 20), range(29)):
        obas=pygame.Rect(x, height/10+5, 19, 40)
        if i in range(9,20):
            listo.append(obas)
    for x,i in zip(range(10, width, 20), range(29)):
        obas=pygame.Rect(x, height/10+50, 19, 40)
        if i in range(11,18):
            listo.append(obas) 
    for x,i in zip(range(10, width, 20), range(29)):
        obas=pygame.Rect(x, height/10+50+45, 19, 40)
        if i in range(13,16):
            listo.append(obas) 
    for x,i in zip(range(10, width, 20), range(29)):
        obas=pygame.Rect(x, height/10+5+90+45, 19, 40)
        if i in range(9, 20):
            listo.append(obas)
    for x,i in zip(range(10, width, 20), range(29)):
        obas=pygame.Rect(x, height/10+5+90+90, 19, 40)
        if i in range(5)or i in range(23, 29):
            listo.append(obas)
    for x,i in zip(range(10, width, 20), range(29)):
        obas=pygame.Rect(x, height/10+5+45+90+90, 19, 40)
        if i in range(9)or i in range(20, 29):
            listo.append(obas) 
    for x,i in zip(range(10, width, 20), range(29)):
        obas=pygame.Rect(x, height/10+5+90+90+90, 19, 40)
        if i in range(8,21):
            listo.append(obas) 
    

def panel7(): 
    global listo, level,count
    count=1
    for x,i in zip(range(5, width, 10), range(59)):
       for y,j in zip(range(85, 350, 25), range(10)):
        obas=pygame.Rect(x, y, 8, 30)
        if  j ==0:
            if i%2==0:
                listo.append(obas)
        if j==1:
            listo.append(obas)
        if j==2:
            if i%2!=0:
                listo.append(obas)
        if j==3:
            listo.append(obas)
        if  j ==4:
            if i%2==0:
                listo.append(obas)
        if j==5:
            listo.append(obas)
        if j==6:
            if i%2!=0:
                listo.append(obas)
        if j==7:
            listo.append(obas)
        if  j ==8:
            if i%2==0:
                listo.append(obas)
        if j==9:
            listo.append(obas)
        

def panel6(): 
    global listo, level,count
    count=1
    for i in range(0, 600, 20): 
       for p in range(int(height/10+50), 350, 55):
            op = random.uniform(0.001, 0.5)
            j = p + 50 * math.sin(i * 0.1)
            obas = pygame.Rect(i, j, 15, 10)
            listo.append(obas)

# MOUSE POSITION (281, 401)
def load_level():
    global level, count

    if count == 0:   
        gameball = pygame.Rect(random.randint(int(width/3),int( width/3+100)), random.randint(int(height/2)+50, int(height/2+50+50) ), 15, 15)

        listo.clear()
        if level == 1:
            count += 1
            panel1()
        elif level == 2:
            count += 1
            panel2()
        elif level == 3:
            count += 1
            panel3()
        elif level == 4:
            count += 1
            panel4()
        elif level == 5:
            count += 1
            panel5()
        elif level == 6:
            count += 1
            panel6()
        elif level == 7:
            count += 1
            panel7()
        if level==8:
            
            complete=True
            pass
        if level<8:
            level +=1
        
    
while alive:
    # levelclear=False
    # print(pygame.mouse.get_pos())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            alive = False
    if level == 0:
        levelclear=False
        score=0
        speedx, speedy = 1, 2
        screen.fill(scoreback)
        font = pygame.font.Font(None, 36)
        text_col = (255, 255, 255)
        
        line1 = "Hello, welcome to the game!"
        line2 = "  Press SPACE to continue"
        
        text1 = font.render(line1, True, (score))
        text2 = font.render(line2, True, (score))
        
        text1_rect = text1.get_rect(center=(width / 2, height / 2 - 20))
        text2_rect = text2.get_rect(center=(width / 2, height / 2 + 20))

        waiting = True
        while waiting:
            screen.fill(stblue)
            pygame.draw.rect(screen, (lavencol), welcomepanel)
            screen.blit(text1, text1_rect)
            screen.blit(text2, text2_rect)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    alive = False
                    waiting = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        level = 1
                        waiting = False

    



    while game_over:
        score=0
        listo=[]
        count=0
        level=0
        levelclear= False
        load_level()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                alive = False
                game_over = False 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    level =1
                    game_over = False
                    levelclear= False
                    gameball = pygame.Rect(random.randint(int(width/3),int( width/3+100)), random.randint(int(height/2)+50, int(height/2+50+50) ), 15, 15)
                    speedx, speedy = 1, 2
        font1=pygame.font .Font(None, 40)
        text = font1.render("Game Over! Press space to Restart", True, text_col)
        text_rect = text.get_rect(center=(width / 2, 1.05 * height / 2))
        screen.blit(text, text_rect)
        pygame.display.update()
        # print(level)
    
    while levelclear and not game_over:
        if not game_over:
            screen.fill(blackcol)
            font2=pygame.font .Font(None, 40)
            if level==8:
                text = font2.render("You WON!! Press Space to retsart", True, goldcol)
                text_rect = text.get_rect(center=(width / 2, 1.05 * height / 2))
                screen.blit(text, text_rect)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        alive = False
                        levelclear = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            levelclear = False
                            level=0
   
            else:
                if level<8 and not game_over:
                    text = font2.render("Level Clear! Press space to Continue", True, goldcol)
                    text_rect = text.get_rect(center=(width / 2, 1.05 * height / 2))
                    screen.blit(text, text_rect)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            alive = False
                            levelclear = False
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                levelclear = False
                                load_level()      
            pygame.display.flip()

    else:
        load_level()
        keo = pygame.key.get_pressed()
        realball_center=gameball.center

        if keo[pygame.K_l]:
            gameball = pygame.Rect(random.randint(int(width/3),int( width/3+100)), random.randint(int(height/2)+50, int(height/2+50+50) ), 15, 15)

            listo=[]
            pygame.time.delay(500)
        if len(listo)==0:
            levelclear=True
            count=0
            print(level)
        

        screen.fill(blackcol)
        pygame.draw.circle(screen, balcol, realball_center, 8)
        pygame.draw.rect(screen, whitecol, panel)
        pygame.draw.rect(screen, scoreback, scorepanel)
        # pygame.draw.rect(screen, whitecol, gameball)
        font = pygame.font.Font(None, 56)
        text_col = (255, 0, 0)
        line3 = " Score: "
        line4 = f"{score:05}"
        line5=f"Level: {level-1:02}"
        text3 = font.render(line3, True, scorecol)
        text4 = font.render(line4, True, blackcol)
        text5 = font.render(line5, True, goldcol)
        text3_rect = text3.get_rect(topleft=(0,33))
        text4_rect = text4.get_rect(topleft=(140,34))
        text5_rect = text5.get_rect(topleft=(400,34))
        screen.blit(text3, text3_rect)
        screen.blit(text4, text4_rect)
        screen.blit(text5, text5_rect)
        

        # pygame.draw.rect(screen, redcol, death)
        for i in listo:
            pygame.draw.rect(screen, tilescol, i)

        gameball.x -= speedx
        gameball.y -= speedy
        # print(listo,"ushd")
        if gameball.colliderect(death)or keo[pygame.K_o ]:
            gameball = pygame.Rect(random.randint(int(width/3),int( width/3+100)), random.randint(int(height/2), int(height/2+50) ), 15, 15)

            speedx, speedy = 1, 2
            listo=[]
            count=0
            level=1
            game_over = True
            continue
        else:
            hit_index = gameball.collidelist(listo)
            if hit_index >= 0:
                print(score)
                score+=1
                hit_block = listo[hit_index]
                if abs(gameball.bottom - hit_block.top) < 10 or abs(gameball.top - hit_block.bottom) < 10:
                    speedy *= -1.01
                    speedx*=1.01
                elif abs(gameball.right - hit_block.left) < 10 or abs(gameball.left - hit_block.right) < 10:
                    speedx *= -1.01
                    speedy *=1.01
                listo.pop(hit_index)
                if len(listo)==0:
                    levelclear=True

        if keo[pygame.K_LEFT]:
            panel.x -= 3
            if panel.x < 10:
                panel.x = 0
        elif keo[pygame.K_RIGHT]:
            panel.x += 3
            if panel.x > width - panel.width - 10:
                panel.x = width - panel.width

        if gameball.colliderect(panel):
            print(speedx, speedy    )
            print(level)
            speedy *= -1.01
            if keo[pygame.K_LEFT]:
                gameball.x -= 3
                if gameball.x < 10:
                    panel.x += 1.03
            elif keo[pygame.K_RIGHT]:
                gameball.x += 3
                if gameball.x > width - panel.width - 10:
                    gameball.x -= 1

        if gameball.x < 8 or gameball.x > width - gameball.width:
            speedx *= -1
        if gameball.y < 73 or gameball.y > height - gameball.height:
            speedy *= -1

    clock.tick(tickpersec)
    pygame.display.flip()

pygame.quit()
