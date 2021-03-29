# 1. import pygame
# open terminal, pip install pygame, pip install PyMySQL
import pygame
from pygame.locals import *
import random
import pymysql

# db connection
conn = pymysql.connect(
    host='34.64.105.45',
    user='hyuntek',
    password='000000',
    db='studyrun',
    charset='utf8')

# 2. Initialize pygame
pygame.init()

# 3. Display Setting
# screen
Height = 350
Width = 700
displaysurface = pygame.display.set_mode((Width, Height))
xpbar = pygame.image.load("C:/Users/shhan/Desktop/sprite/blankbar.png").convert_alpha()
xpbar = pygame.transform.scale(xpbar, (xpbar.get_width(), int(xpbar.get_height()/2)))
coin = pygame.image.load("C:/Users/shhan/Desktop/sprite/5.png").convert_alpha()
coin = pygame.transform.scale(coin, (int(coin.get_width()*1.4), int(coin.get_height()*1.4)))
darkbar = pygame.image.load("C:/Users/shhan/Desktop/sprite/darkbar.png").convert_alpha()
darkbar = pygame.transform.scale(darkbar, (int(darkbar.get_width()/3.5), int(darkbar.get_height()/5)))
hpbar = pygame.image.load("C:/Users/shhan/Desktop/sprite/blankbar.png").convert_alpha()
hpbar = pygame.transform.scale(hpbar, (int(hpbar.get_width()/1.15) , int(hpbar.get_height()/1.2)))
pygame.display.set_caption("Game")

#color
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 250, 0)
yellow = (255, 225, 0)
red = (255, 0, 0)
pink = (255, 90, 90)

#font
smallerfont = pygame.font.SysFont('Corbel', 13, True)
regularfont = pygame.font.SysFont('Corbel', 20, True)
headingfont = pygame.font.SysFont('Verdana', 40)



# 4. InGame Setting
vec = pygame.math.Vector2
Acc = 0.3
Fric = -0.10
FPS = 60
count1 = 0
count2 = 0
FPS_Clock = pygame.time.Clock()
hit_cooltime = pygame.USEREVENT + 1


#animation
run_ani_R = [pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Sprite_R.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Sprite2_R.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Sprite3_R.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Sprite4_R.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Sprite5_R.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Sprite6_R.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Sprite_R.png").convert_alpha()]
run_ani_L = [pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Sprite_L.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Sprite2_L.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Sprite3_L.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Sprite4_L.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Sprite5_L.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Sprite6_L.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Sprite_L.png").convert_alpha()]
attack_ani_R =[pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Sprite_R.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Attack_R.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Attack2_R.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Attack2_R.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Attack3_R.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Attack3_R.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Attack4_R.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Attack4_R.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Attack5_R.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Attack5_R.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Sprite_R.png").convert_alpha()]
attack_ani_L = [pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Sprite_L.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Attack_L.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Attack2_L.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Attack2_L.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Attack3_L.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Attack3_L.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Attack4_L.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Attack4_L.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Attack5_L.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Attack5_L.png").convert_alpha(),
             pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Sprite_L.png").convert_alpha()]



# Class
class XP:
    def __init__(self):
        super().__init__()
        self.userNo = '1'
        self.time = 0
        self.lv = 0
        self.xp = 0

    def getxp(self):
        if conn.open:
            curs = conn.cursor()
            curs.execute("select XP from user_data where userNo = %s", self.userNo)
            self.time = curs.fetchone()[0]
            self.lv = int(self.time / 60)
            self.xp = self.time % 60



xp = XP()
xp.getxp()

class money:
    def __init__(self):
        super().__init__()
        self.userNo = '1'
        self.money = 0


    def getmoney(self):
        if conn.open:
            curs = conn.cursor()
            curs.execute("select money from user_data where userNo = %s", self.userNo)
            self.money = curs.fetchone()[0]


    def uploadmoney(self):
        if conn.open:
            curs = conn.cursor()
            curs.execute("update user_data set money = %s" % self.money + " where userNo = %s", self.userNo)
            conn.commit()
            conn.close()

money = money()
money.getmoney()

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bgimage = pygame.image.load("C:/Users/shhan/Desktop/sprite/Background.png").convert_alpha()
        self.bgX = 0
        self.bgY = 0

    def render(self):
        displaysurface.blit(self.bgimage, (self.bgX, self.bgY))


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/shhan/Desktop/sprite/Ground.png").convert_alpha()
        self.rect = self.image.get_rect(center=(350, 350))

    def render(self):
        displaysurface.blit(self.image, (self.rect.x, self.rect.y))


background = Background()
ground = Ground()
ground_group = pygame.sprite.Group()
ground_group.add(ground)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/shhan/Desktop/sprite/Player_Sprite_R.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.vx = 0
        self.pos = vec((340, 240))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.direction = "RIGHT"
        self.running = False
        self.jumping = False
        self.move_Frame =  0
        self.attacking = False
        self.cooltime = False
        self.attack_Frame = 0
        self.hp = 100


    def move(self):
        self.acc = vec(0, 0.5)

        if abs(self.vel.x) > 0.3:
            self.running = True
        else:
            self.running = False

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.acc.x = -Acc
        if pressed_keys[K_RIGHT]:
            self.acc.x = Acc

        self.acc.x += self.vel.x * Fric
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > Width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = Width
        self.rect.midbottom = self.pos

    def gravity_check(self):
        hits = pygame.sprite.spritecollide(player, ground_group, False)
        if self.vel.y > 0:
            if hits:
                lowest = hits[0]
                if self.pos.y < lowest.rect.bottom:
                    self.pos.y = lowest.rect.top + 1
                    self.vel.y = 0
                    self.jumping = False

    def jump(self):
        self.rect.y += 1
        hits = pygame.sprite.spritecollide(player, ground_group, False)
        self.rect.y -= 1

        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -12

    def update(self):
        if self.move_Frame > 6:
            self.move_Frame = 0
            return

        if self.jumping == False and self.running == True:
            if self.vel.x > 0:
                self.image = run_ani_R[self.move_Frame]
                self.direction = "RIGHT"

            elif self.vel.x < 0:
                self.image = run_ani_L[self.move_Frame]
                self.direction = "LEFT"

            self.move_Frame += 1

            if abs(self.vel.x) < 0.4 and self.move_Frame != 0:
                self.move_Frame = 0
                if self.direction == "RIGHT":
                    self.image = run_ani_R[self.move_Frame]
                elif self.direction == "LEFT":
                    self.image = run_ani_L[self.move_Frame]

    def correction(self):
        if self.attack_Frame == 1:
            self.pos.x -= 20
        if self.attack_Frame == 10:
            self.pos.x += 20

    def attack(self):
        if self.attack_Frame > 10:
            self.attack_Frame = 0
            self.attacking = False

        if self.direction == "RIGHT":
            self.image = attack_ani_R[self.attack_Frame]
        elif self.direction == "LEFT":
            self.correction()
            self.image = attack_ani_L[self.attack_Frame]

        self.attack_Frame += 1

    def player_hit(self):
        if self.cooltime == False:
            self.cooltime = True
            pygame.time.set_timer(hit_cooltime, 1000)
            self.hp -= 10
            print("hit")
            pygame.display.update()


player = Player()
playergroup = pygame.sprite.Group()
playergroup.add(player)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_R = pygame.image.load("C:/Users/shhan/Desktop/sprite/wolf_R.png").convert_alpha()
        self.image_R = pygame.transform.scale(self.image_R, (int(self.image_R.get_width()/5), int(self.image_R.get_height()/4.5)))
        self.image_L = pygame.image.load("C:/Users/shhan/Desktop/sprite/wolf_L.png").convert_alpha()
        self.image_L = pygame.transform.scale(self.image_L, (int(self.image_L.get_width() / 5), int(self.image_L.get_height() / 4.5)))
        self.blank = pygame.image.load("C:/Users/shhan/Desktop/sprite/blank.png").convert_alpha()
        self.rect = self.image_R.get_rect()
        self.pos = vec(0, 0)
        self.vel = vec(0, 0)
        self.direction = random.randint(0, 1)
        self.vel.x = random.randint(2, 6) / 2
        self.cooltime = False
        self.enemyhit = False

        if self.direction == 0:
            self.pos.x = 0
            self.pos.y = 235
        elif self.direction == 1:
            self.pos.x = 700
            self.pos.y = 235

    def move(self):
        if self.pos.x >= (Width-20):
            self.direction = 1
        elif self.pos.x <= 0:
            self.direction = 0

        if self.direction == 0:
            self.pos.x += self.vel.x
        elif self.direction == 1:
            self.pos.x -= self.vel.x
        self.rect.center = self.pos


    def enemy_hit(self):
            if self.cooltime == False:
                self.cooltime = True
                pygame.time.set_timer(hit_cooltime, 1000)
                self.enemyhit = True
                print("enemy hit")
                pygame.display.update()


    def render(self):
        if self.direction == 0:
            displaysurface.blit(self.image_R, (self.pos.x, self.pos.y))
        elif self.direction == 1:
            displaysurface.blit(self.image_L, (self.pos.x, self.pos.y))


    def render2(self):
        displaysurface.blit(self.blank, (self.pos.x, 10))

    def update(self):
        hits = pygame.sprite.spritecollide(self, playergroup, False)
        if hits and player.attacking == True:
            enemy.enemy_hit()
        elif hits and player.attacking == False:
            player.player_hit()


enemy = Enemy()
enemygroup = pygame.sprite.Group
enemygroup.add(enemy)



# 5. Main Event
while True:
    player.gravity_check()
    for event in pygame.event.get():
        if event.type == hit_cooltime:
            player.cooltime = False
            enemy.cooltime = False
            pygame.time.set_timer(hit_cooltime, 0)

        if event.type == QUIT:
            money.uploadmoney()
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LALT:
                player.jump()
            if event.key == pygame.K_LCTRL:
                if player.attacking == False:
                    player.attack()
                    player.attacking = True

    xptext = smallerfont.render(str(xp.xp) + "/60", True, white)
    lvtext = regularfont.render(str(xp.lv), True, yellow)
    moneytext = smallerfont.render(str(money.money), True, white)
    background.render()
    ground.render()

    player.update()
    if player.attacking == True:
        player.attack()
    player.move()
    displaysurface.blit(player.image, player.rect)


    if enemy.enemyhit == False:
        enemy.move()
        enemy.update()
        enemy.render()
    elif enemy.enemyhit == True:
        enemy.move()
        enemy.render2()
        count1 += 1
        if count1 == 1:
            money.money += 10
            if player.hp <= 90:
                  player.hp += 10
        if count1 == 180:
            enemy.enemyhit = False
            count1 = 0

    FPS_Clock.tick(FPS)

    pygame.draw.circle(displaysurface, black, [545, 17], 10)
    displaysurface.blit(xpbar, (560, 10))
    displaysurface.blit(hpbar, (10, 10))
    pygame.draw.rect(displaysurface, red, pygame.Rect(16, 15, player.hp, 16))
    pygame.draw.rect(displaysurface, pink, pygame.Rect(16, 15, player.hp, 8))
    pygame.draw.rect(displaysurface, green, pygame.Rect(565, 13, xp.xp, 10))
    displaysurface.blit(xptext, (610, 12))
    displaysurface.blit(lvtext, (540, 9))
    displaysurface.blit(coin, (415, 8))
    displaysurface.blit(darkbar, (415, 3))
    displaysurface.blit(moneytext, (465, 13))
    pygame.display.update()
