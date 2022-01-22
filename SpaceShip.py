import pygame
import random
import os
import record
from pygame import draw
from threading import Thread
import gc
def main():
    FPS = 60
    WIDTH = 500
    HEIGHT = 600

    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255,0,0)
    YELLOW = (255, 255 ,0)
    BLACK = (0, 0, 0)

    #遊戲初始化 & 創建視窗
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("太空生存戰")
    clock =pygame.time.Clock()

    #載入圖片
    backgroud_img = pygame.image.load(os.path.join("img", "background.png")).convert()
    player_img = pygame.image.load(os.path.join("img", "player.png")).convert()
    #rock_img = pygame.image.load(os.path.join("img", "rock.png")).convert()
    bullet_img = pygame.image.load(os.path.join("img", "bullet.png")).convert()
    rock_imgs = []
    for i in range(7):
        rock_imgs.append(pygame.image.load(os.path.join("img", f"rock{i}.png")).convert())
    expl_anim = {}
    expl_anim['lg'] = []
    expl_anim['sm'] = []
    for i in range(9):
        expl_img = pygame.image.load(os.path.join("img", f"expl{i}.png")).convert()
        expl_img.set_colorkey(BLACK)
        expl_anim['lg'].append(pygame.transform.scale(expl_img, (75, 75)))
        expl_anim['sm'].append(pygame.transform.scale(expl_img, (30, 30)))
    power_imgs = {}
    power_imgs['heart'] = pygame.image.load(os.path.join("img", "heart.png")).convert()
    power_imgs['gun'] = pygame.image.load(os.path.join("img", "gun.png")).convert()

     #載入音效
    #shoot_sound = pygame.mixer.Sound(os.path.join("sound", "shoot.wav"))
    #expl_sounds = [
    #    pygame.mixer.Sound(os.path.join("sound", "expl0.wav")),
    #    pygame.mixer.Sound(os.path.join("sound", "expl1.wav"))
    #]
    #pygame.mixer.music.load(os.path.join("sound","background.ogg"))
    #pygame.mixer.music.set_volume(0.4)

    font_name = pygame.font.match_font('arial')
    def draw_text(surf, text, size, x ,y):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.centerx = x
        text_rect.top = y
        surf.blit(text_surface, text_rect)

    def new_rock():
        r = Rock()
        all_sprites.add(r)
        rocks.add(r)

    def draw_health(surf, hp, x, y):
        if hp < 0:
            hp = 0
        BAR_LENGTH =100
        BAR_HEIGHT =10
        fill = (hp/100)*BAR_LENGTH
        outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
        pygame.draw.rect(surf, GREEN, fill_rect)
        pygame.draw.rect(surf, WHITE, outline_rect, 2)

    def draw_init():
        draw_text(screen, 'Space Survival!', 50, WIDTH/2, HEIGHT/4)
        draw_text(screen, 'You can use voice to control the space ship.', 22, WIDTH/2, HEIGHT/2)
        draw_text(screen, 'Press any key to start...', 18, WIDTH/2, HEIGHT*3/4)
        pygame.display.update()
        waiting = True
        while waiting:
            clock.tick(FPS)
            # get the input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYUP:
                    waiting = False

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(player_img, (50,38))
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.radius = 20
            #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
            self.rect.centerx = (WIDTH/2)
            self.rect.bottom = HEIGHT - 10
            self.speedx = 8 
            self.health = 100
            self.gun = 1
            self.gun_time = 0
            self.cnt=0
            self.command = 'none'
            self.rec = True
            
        def get_command(self):
                while self.rec:
                    self.command=record.rec()
                    print(self.command)
                    self.cnt = 0
                    gc.collect()

        def shoot(self):
            if self.gun == 1:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
            elif self.gun >=2:
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
        # shoot_sound.play()      
            
            
        def update(self):
            now = pygame.time.get_ticks()
            if self.gun > 1 and now - self.gun_time > 5000:
                self.gun -= 1
                self.gun_time = now

            if self.cnt%10 == 0:
                self.shoot()
            if self.cnt >=130 :
                 self.cnt = 0
            #     t1 = Thread(target=self.get_command)
            #     t1.start()
            
            if self.cnt > 15:
                 self.command = 'none'
            
          
            
           
            self.cnt = self.cnt + 1
            if self.command == 'right':
                self.rect.x += self.speedx
            if self.command == 'left':
                self.rect.x -= self.speedx
            key_pressed = pygame.key.get_pressed()
            
            
            if key_pressed[pygame.K_RIGHT]:
                self.rect.x += self.speedx
            if key_pressed[pygame.K_LEFT]:
                self.rect.x -= self.speedx
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0
        def gunup(self):
            self.gun += 1
            self.gun_time = pygame.time.get_ticks()

        

    class Rock(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image_ori = random.choice(rock_imgs)
            self.image = self.image_ori.copy()
            self.image_ori.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.radius = int (self.rect.width*0.85 /2)
            #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-180, -100)
            self.speedy = random.randrange(2, 10) 
            self.speedx = random.randrange(-3, 3) 
            self.total_degree = 0
            self.rot_degree = random.randrange(-3, 3) 
        
        def rotate(self):
            self.total_degree += self.rot_degree
            self.total_degree = self.total_degree % 360
            self.image = pygame.transform.rotate(self.image_ori, self.total_degree)
            center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = center

        def update(self):
            self.rotate()
            self.rect.y += self.speedy
            self.rect.x += self.speedx
            if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
                self.rect.x = random.randrange(0, WIDTH - self.rect.width)
                self.rect.y = random.randrange(-100, -40)
                self.speedy = random.randrange(2, 10) #* (pygame.time.get_ticks()/5000)
                self.speedx = random.randrange(-3, 3) #* (pygame.time.get_ticks()/5000)            

    class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = bullet_img
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.bottom = y
            self.speedy = -10 

        def update(self):
            self.rect.y += self.speedy
            if self.rect.bottom < 0:
                self.kill() 

    class Power(pygame.sprite.Sprite):
        def __init__(self, center):
            pygame.sprite.Sprite.__init__(self)
            self.type = random.choice(['heart','gun'])
            self.image = power_imgs[self.type]
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.speedy = 3

        def update(self):
            self.rect.y += self.speedy
            if self.rect.top > HEIGHT:
                self.kill() 

    #加入群組
    all_sprites = pygame.sprite.Group()
    rocks = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    powers = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    for i in range(8):
        new_rock()
    score = 0
    # pygame.mixer.music.play(-1)
    t1 = Thread(target=player.get_command)
    t1.start()

    #遊戲迴圈
    show_init = True
    running = True
    while running:

        # show the initial page
        if show_init:
            draw_init()
            show_init = False

        #一秒鐘內最多被執行十次
        clock.tick(FPS)
        # 取得輸入
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running =False
            elif event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_SPACE:
                    player.shoot()
            
        #更新遊戲
        all_sprites.update()
        #判斷石頭、子彈是否相撞
        hits = pygame.sprite.groupcollide(rocks, bullets, True, True)
        for hit in hits:
            # random.choice(expl_sounds).play()
            score += hit.radius
            if random.random() > 0.9:
                pow = Power(hit.rect.center)
                all_sprites.add(pow)
                powers.add(pow)
            new_rock()
        #判斷石頭、戰機是否相撞
        hits = pygame.sprite.spritecollide(player, rocks, True, pygame.sprite.collide_circle)
        for hit in hits:
            new_rock()
            player.health -= hit.radius
            if player.health<=0:
                running = False
                player.rec = False

        #判斷寶物、戰機是否相撞
        hits = pygame.sprite.spritecollide(player, powers,True)
        for hit in hits:
            if hit.type == 'heart':
                player.health += 20
                if player.health > 100:
                    player.health = 100
            elif hit.type == 'gun':
                player.gunup()

        #畫面顯示
        screen.fill(BLACK)
        screen.blit(backgroud_img, (0,0))
        all_sprites.draw(screen)
        draw_text(screen, str(score), 18, WIDTH/2 , 10)
        draw_health(screen, player.health, 5, 15)
        pygame.display.update()
    
    pygame.quit()
    player.rec = False
main()
