import pygame
import sys
import os
import random
import time
import cv2
import numpy as np
import newWebcam
# music
def play_music(x,n,y):
    # pygame.mixer.music.load(x)
    pygame.mixer.Channel(y).play(pygame.mixer.Sound(file=x),n)

# backgrnd
my_path = os.path.abspath(os.path.dirname(__file__))
bullet_img = pygame.image.load(os.path.join(my_path, "Image\\alo1234.png"))
my_image = pygame.image.load(os.path.join(my_path, "Image\\galaxy.jpg"))
ship_img = pygame.image.load(os.path.join(my_path, "Image\\nnn.png"))
enemy_img1 = pygame.image.load(os.path.join(my_path, "Image\\millennium_eye___render_by_alanmac95-daqixic.png"))
enemy_img2 = pygame.image.load(os.path.join(my_path, "Image\\img.png"))
enemy_img1 = pygame.transform.scale(enemy_img1,(20,20))
enemy_img2 = pygame.transform.scale(enemy_img2,(20,20))
ship_img = pygame.transform.scale(ship_img,(30,40))
bullet_img = pygame.transform.scale(bullet_img,(10,20))
#
WIDTH = 240
HEIGHT = 600
FPS = 34
shootdelay = 0.14
bulletspeed = -10
# define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
yellow = (153,153,0)
bright_yellow = (204,204,0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.blit(my_image, (100, 100))
pygame.display.set_caption("Space shooting")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = ship_img
        # self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT -20)
        self.lastshot = 0
    def update(self):
        if self.rect.x <0:
            self.rect.x = 0
        elif self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
        # elif self.rect.



    def shoot(self):
        self.bullet = Bullet(self.rect.centerx, self.rect.top)
        if time.time()-self.lastshot > shootdelay:
            self.lastshot = time.time()
            all_sprites.add(self.bullet)
            bullets.add(self.bullet)


class Enemy(pygame.sprite.Sprite):
    speedy_list = [5,10,5,10]
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img2
        # self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100,-40,step=10)
        self.speedy = self.speedy_list[random.randrange(-1,3)]
        self.speedx = random.randrange(-3,3)
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10 or self.rect.left < 0 or self.rect.right > WIDTH:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        # self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = bulletspeed
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top < 0:
            self.kill()
class ScoreBoard():
    def __init__(self, font_size=20, score=0):
        self.x = WIDTH - 150
        self.y = 20
        self.score = score
        self.font = pygame.font.Font('freesansbold.ttf', font_size)

    def display(self, score):
        result_srf = self.font.render('Score : %s' % score, True, WHITE)
        result_rect = result_srf.get_rect()
        result_rect.topleft = (WIDTH - 150, 20)
        screen.blit(result_srf, result_rect.topleft)

all_sprites = pygame.sprite.Group()
player = Player()
score = ScoreBoard()
enemy = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all_sprites.add(player)
for i in range(10):
    evil = Enemy()
    if evil.speedy <7: evil.image = enemy_img1
    all_sprites.add(evil)
    enemy.add(evil)


en = False
intro = True
running = True
c = -1

# intro and end

def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)

def play():
    global intro,running,en
    intro = False
    running = True
    en = False
    game_with_keyboard()

def play_com_vis():
    global intro,running,en
    en = False
    intro = False
    running = True
    game_with_comvis()

def quit():
    global intro,running,en
    en = False
    intro = False
    running = False
def again():
    global running,enemy,all_sprites,screen,FPS,score,x,intro,en
    score.score = 0
    FPS = 30
    running = True
    screen.fill(BLACK)
    screen.blit(my_image,(0,0))
    all_sprites.remove(enemy)
    enemy = pygame.sprite.Group()
    for i in range(10):
        evil = Enemy()
        if evil.speedy <7: evil.image = enemy_img1
        all_sprites.add(evil)
        enemy.add(evil)
    intro1()
    x = str(score.score)
    intro = True
    en = True

def intro1():
    global intro,running,en
    intro = True
    en = False
    running = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # screen.fill(WHITE)
        screen.blit(my_image,(0,0))
        largeText = pygame.font.Font('freesansbold.ttf', 30)
        TextSurf, TextRect = text_objects("Space shooter", largeText)
        TextRect.center = ((WIDTH / 2), (HEIGHT / 2))
        screen.blit(TextSurf, TextRect)

        button("Keyboard",80, 430, 100, 40,yellow,bright_yellow, play)
        button("Webcam", 80, 480, 100, 40, green, bright_green, play_com_vis)
        button("QUIT", 90, 530, 80, 40, red, bright_red,quit)
        # button("ABOUT",40,330,60,40, green,green, about)



        pygame.display.update()
        clock.tick(15)

def end():
    global running, intro,x,en
    en = True
    running = True
    intro = False
    while en:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(BLACK)
        largeText = pygame.font.Font('freesansbold.ttf', 30)
        TextSurf, TextRect = text_objects(x, largeText)
        TextSurf1, TextRect1 = text_objects("Your score :", largeText)
        TextRect1.center = ((WIDTH/2), (HEIGHT / 2))
        TextRect.center = ((WIDTH/2), (HEIGHT /1.75))
        screen.blit(TextSurf, TextRect)
        screen.blit(TextSurf1, TextRect1)

        button("CONTINUE", 40, 530, 65, 40, green, bright_green, again)
        button("QUIT", 150, 530, 65, 40, red, bright_red, quit)

        pygame.display.update()

# gameloop

def game_with_comvis():
    global score,running,c,FPS
    # keep loop running at the same speed
    vision = newWebcam.webcam()
    vision.thread_webcam()


    frame = vision.get_currentFrame()
    # print(posX,posY)

    # Process input (events)
    # posX = 50
    # posY = 50
    play_music(os.path.join(my_path, "Sound\\launch.wav"),-1,0)
    while running:
        posX, posY = vision.get_currentPos()
        clock.tick(FPS)
        for event in pygame.event.get():
            # closing window
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                c = -1
            if event.type == pygame.KEYDOWN:
                c = event.key
        # keys = pygame.key.get_pressed()

        # if c == keys[pygame.K_a]:
        #     player.rect.x -= 10
        # if c == keys[pygame.K_d]:
        #     player.rect.x += 10
        if c == pygame.K_UP:
            FPS += 3
            c = 0
        if c == pygame.K_DOWN:
            FPS -= 3
            c = 0
        if vision.get_len() != 0:
            player.shoot()
        if posX != 0 and posY != 0:
            player.rect.x = posX*2 -50
            player.rect.y = posY*2 + 250
        # Update
        all_sprites.update()

        # hits
        hits = pygame.sprite.groupcollide(bullets, enemy, True, True)
        for hit in hits:
            play_music(os.path.join(my_path, "Sound\\bullet.wav"),1,1)
            evil = Enemy()
            if evil.speedy <7: evil.image = enemy_img1
            all_sprites.add(evil)
            enemy.add(evil)
            FPS += 0.5
        hitst = pygame.sprite.spritecollide(player, enemy, False)
        if hitst:
            play_music(os.path.join(my_path, "Sound\\explosion.wav"),1,1)
            running = False
        # Draw / render
        screen.fill(BLACK)
        screen.blit(my_image, (0, 0))
        all_sprites.draw(screen)
        if hits: score.score += 1
        score.display(score.score)
        # *after* drawing everything, flip the display
        pygame.display.flip()

def game_with_keyboard():
    global score,running,c,FPS
    # keep loop running at the same speed

    # posX, posY = vision.get_currentPos()
    # frame = vision.get_currentFrame()
    # cv2.imshow("threadmain", frame)
    # print(posX,posY)

    # Process input (events)
    # posX = 50
    # posY = 50
    # score.score = 0
    play_music(os.path.join(my_path, "Sound\\launch.wav"),-1,0)
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            # closing window
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                c = 0
            if event.type == pygame.KEYDOWN:
                c = event.key
        player.shoot()
        if c == pygame.K_a:
            player.rect.x -= 5
        if c == pygame.K_d:
            player.rect.x += 5
        if c == pygame.K_UP:
            FPS += 3
            c = 0
        if c == pygame.K_DOWN:
            FPS -= 3
            c = 0
        # if posX != 0 and posY != 0:
        #     player.rect.x = posX -50
        #     player.rect.y = posY + 250
        # Update
        all_sprites.update()

        # hits
        hits = pygame.sprite.groupcollide(bullets, enemy, True, True)
        for hit in hits:
            play_music(os.path.join(my_path, "Sound\\bullet.wav"),1,1)
            evil = Enemy()
            if evil.speedy <7: evil.image = enemy_img1
            all_sprites.add(evil)
            enemy.add(evil)
            # global FPS
            FPS += 0.5
        hitst = pygame.sprite.spritecollide(player, enemy, False)
        if hitst:
            play_music(os.path.join(my_path, "Sound\\explosion.wav"),1,1)
            running = False
        # Draw / render
        screen.fill(BLACK)
        screen.blit(my_image, (0, 0))
        all_sprites.draw(screen)
        if hits: score.score += 1
        score.display(score.score)
        # *after* drawing everything, flip the display
        pygame.display.flip()

#

intro1()
x = str(score.score)
while True:
    end()
    if running == False and intro == False and en == False: break
# if running == False:
#     pygame.quit()


















