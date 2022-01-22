#!/usr/bin/env python
import pygame,sys,time,random
import record
from pygame.locals import *
from threading import Thread
import gc
import os
# ©wёqГC¦вЕЬјЖ
redColour = pygame.Color(255,0,0)
blackColour = pygame.Color(0,0,0)
whiteColour = pygame.Color(255,255,255)
greyColour = pygame.Color(150,150,150)
command = 'none'
rec = True
# ©wёqgameOverЁзјЖ
def gameOver(playSurface):
    #gameOverFont = pygame.font.Font('arial.ttf',72)
    #gameOverSurf = gameOverFont.render('Game Over', True, greyColour)
    # = gameOverSurf.get_rect()
    #gameOverRect.midtop = (320, 10)
    #playSurface.blit(gameOverSurf, gameOverRect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()

# ©wёqmainЁзјЖ
def get_command():
    global command,rec
    while rec:
        command=record.rec()
        print(command)
        gc.collect()
    
def main():
    # 初始化pygame
    global command
    pygame.init()
    fpsClock = pygame.time.Clock()
    # 創建pygame顯示層
    playSurface = pygame.display.set_mode((640,480))
    pygame.display.set_caption('Raspberry Snake')
    
     # background picture
    background_img = pygame.image.load(os.path.join("img", "snake_background.jpg")).convert()

    # 初始化變數
    snakePosition = [100,100]
    snakeSegments = [[100,100],[80,100],[60,100],[40,100],[20,100]]
    raspberryPositions = [[20,80],[560,380],[60,400],[300,200],[520,20],[20, 50],[300,260],[300,300],[80,420],[400, 200],[100, 460],
                          [600,500],[600,20],[20, 220],[220,140],[140,200]]
    #raspberryPositions = [300,300]
    raspberrySpawned = 1
    direction = 'right'
    changeDirection = 'none'
    command = 'none'
    update_cnt=0
    t1 = Thread(target=get_command)
    t1.start()
    #changeDirection = direction
    while True:
        # 檢測例如按鍵等pygame事件
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                # 判斷鍵盤事件
                if event.key == K_RIGHT or event.key == ord('d'):
                    changeDirection = 'right'
                if event.key == K_LEFT or event.key == ord('a'):
                    changeDirection = 'left'
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
        # 判斷是否輸入了反方向
        # if direction == 'right':
        #     snakePosition[0] += 20
        #     if changeDirection == 'right':
        #         snakePosition[0] -= 20
        #         direction = 'down'
        #         changeDirection = 'none'
            
        #     if changeDirection == 'left':
        #         snakePosition[0] -= 20
        #         direction = 'up'
        #         changeDirection = 'none'
        #     if snakePosition[0] > 620:
        #         snakePosition[0] = 0

        # if direction == 'left':
        #     snakePosition[0] -= 20
        #     if changeDirection == 'right':
        #         snakePosition[0] += 20
        #         direction = 'up'
        #         changeDirection = 'none'
        #     if changeDirection == 'left':
        #         snakePosition[0] += 20
        #         direction = 'down'
        #         changeDirection = 'none'
        #     if snakePosition[0] < 0:
        #         snakePosition[0] = 620

        # if direction == 'up':
        #     snakePosition[1] -= 20
        #     if changeDirection == 'right':
        #         #snakePosition[0] += 20
        #         direction = 'right'
        #         changeDirection = 'none'
        #     if changeDirection == 'left':
        #         #snakePosition[0] -= 20
        #         direction = 'left'
        #         changeDirection = 'none'
        #     if snakePosition[1] < 0:
        #         snakePosition[1] = 460
        # if direction == 'down':
        #     snakePosition[1] += 20
        #     if changeDirection == 'right':
        #         #snakePosition[0] -= 20
        #         direction = 'left'
        #         changeDirection = 'none'
        #     if changeDirection == 'left':
        #         #snakePosition[0] += 20
        #         direction = 'right'
        #         changeDirection = 'none'
        #     if snakePosition[1] > 460:
        #         snakePosition[1] = 0
                
        # 判斷是否吃掉了樹莓
        snakeSegments.insert(0,list(snakePosition))
        tmp = 0
        tmp = len(raspberryPositions)
        for i in range(tmp): 
            if snakePosition[0] == raspberryPositions[i][0] and snakePosition[1] == raspberryPositions[i][1]:
                raspberrySpawned = 0                
                #snakeSegments.pop(0,list(snakePosition))
                # decrease 蛇的長度
                snakeSegments.pop()
            #else:
            # 如果吃掉樹莓，則重新生成樹莓
            if raspberrySpawned == 0:
                x = random.randrange(1,32)
                y = random.randrange(1,24)
                #raspberryPositions[i] = [int(x*20),int(y*20)]
                raspberryPositions[i][0] = int(x*20)
                raspberryPositions[i][1] = int(y*20)
                
                raspberrySpawned = 1
        snakeSegments.pop()
        # 繪製pygame顯示層
        playSurface.fill(blackColour)
        playSurface.blit(background_img, (0,0))
        for position in snakeSegments:
            pygame.draw.rect(playSurface,whiteColour,Rect(position[0],position[1],20,20))
        for Positions in raspberryPositions:
            pygame.draw.rect(playSurface,redColour,Rect(Positions[0], Positions[1],20,20))

        # 刷新pygame顯示層
        pygame.display.flip()
        update_cnt+=1
        # 判斷是否死亡
   
            
        
        
        changeDirection=command
        command = 'none'
        #print("changeDirection",changeDirection)
        if direction == 'right':
            snakePosition[0] += 20
            if changeDirection == 'right':
                snakePosition[0] -= 20
                direction = 'down'
                changeDirection = 'none'
            
            if changeDirection == 'left':
                snakePosition[0] -= 20
                direction = 'up'
                changeDirection = 'none'
            if snakePosition[0] > 620:
                snakePosition[0] = 0

        if direction == 'left':
            snakePosition[0] -= 20
            if changeDirection == 'right':
                snakePosition[0] += 20
                direction = 'up'
                changeDirection = 'none'
            if changeDirection == 'left':
                snakePosition[0] += 20
                direction = 'down'
                changeDirection = 'none'
            if snakePosition[0] < 0:
                snakePosition[0] = 620

        if direction == 'up':
            snakePosition[1] -= 20
            if changeDirection == 'right':
                #snakePosition[0] += 20
                direction = 'right'
                changeDirection = 'none'
            if changeDirection == 'left':
                #snakePosition[0] -= 20
                direction = 'left'
                changeDirection = 'none'
            if snakePosition[1] < 0:
                snakePosition[1] = 460
        if direction == 'down':
            snakePosition[1] += 20
            if changeDirection == 'right':
                #snakePosition[0] -= 20
                direction = 'left'
                changeDirection = 'none'
            if changeDirection == 'left':
                #snakePosition[0] += 20
                direction = 'right'
                changeDirection = 'none'
            if snakePosition[1] > 460:
                snakePosition[1] = 0

        
        
        # §PВ_¬O§_¦є¤`
        #if snakePosition[0] > 620 or snakePosition[0] < 0:
        #    gameOver(playSurface)
        #if snakePosition[1] > 460 or snakePosition[1] < 0:
        for snakeBody in snakeSegments[1:]:
            if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
                gameOver(playSurface)
                rec = False
                
        ## 控制游戲速度
        fpsClock.tick(2)

if __name__ == "__main__":
    main()
