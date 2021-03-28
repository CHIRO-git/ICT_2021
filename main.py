# 1. import pygame
# open terminal, pip install pygame, pip install PyMySQL
import pygame
from pygame.locals import *
import random
import pymysql

conn = pymysql.connect(
    host='34.64.105.45',
    user='hyuntek',
    password='000000',
    db='studyrun',
    charset='utf8')

# 2. Initialize pygame
pygame.init()

# 3. Display Setting
Height = 350
Width = 700
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 250, 0)
yellow = (255, 225, 0)
smallerfont = pygame.font.SysFont('Corbel', 13, True)
regularfont = pygame.font.SysFont('Corbel', 20, True)
headingfont = pygame.font.SysFont('Verdana', 40)

displaysurface = pygame.display.set_mode((Width, Height))
xpbar = pygame.image.load("C:/Users/shhan/Desktop/sprite/xpbar.png").convert_alpha()
xpbar = pygame.transform.scale(xpbar, (xpbar.get_width(), int(xpbar.get_height()/2)))
pygame.display.set_caption("Game")


# 4. InGame Setting
vec = pygame.math.Vector2
Acc = 0.3
Fric = -0.10
FPS = 60
FPS_Clock = pygame.time.Clock()
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
hit_cooldown = pygame.USEREVENT + 1


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
            conn.close


xp = XP()


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
        self.cooldown = False
        self.attack_Frame = 0
        #self.time = 325
        #self.level = int(self.time / 60)
        #self.experience = self.time % 60


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
        if self.cooldown == False:
            self.cooldown = True
            pygame.time.set_timer(hit_cooldown, 1000)

            print("hit")
            pygame.display.update()


player = Player()
playergroup = pygame.sprite.Group()
playergroup.add(player)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/shhan/Desktop/sprite/Enemy.png")
        self.rect = self.image.get_rect()
        self.pos = vec (0, 0)
        self.vel = vec (0, 0)
        self.direction = random.randint(0, 1)
        self.vel.x = random.randint(2, 6) / 2
        self.cooldown = False
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
            if self.cooldown == False:
                self.cooldown = True
                pygame.time.set_timer(hit_cooldown, 1000)
                self.enemyhit = True
                print("enemy hit")
                pygame.display.update()



    def update(self):
        hits = pygame.sprite.spritecollide(enemy, playergroup, False)
        if hits and player.attacking == True:
            enemy.enemy_hit()
        elif hits and player.attacking == False:
            player.player_hit()


    def render(self):
        displaysurface.blit(self.image, (self.pos.x, self.pos.y))

enemy = Enemy()
enemygroup = pygame.sprite.Group
enemygroup.add(enemygroup)



#class StatusBar(pygame.sprite.Sprite):
#    def __init__(self):
#        super().__init__()
#        self.surf = pygame.Surface((100, 10))
#        self.rect = self.surf.get_rect(center=(100, 50))
#
#    def update_draw(self):
#        #text1 = smallerfont.render("Level: " + str(player.level), True, white)
#        text2 = smallerfont.render("EXP: " + str(xp.xp), True, black)
#        #displaysurface.blit(text1, (585, 7))
#        displaysurface.blit(text2, (585, 22))

#status_bar = StatusBar()

# 5. Main Event
while True:
    player.gravity_check()
    for event in pygame.event.get():
        if event.type == hit_cooldown:
            player.cooldown = False
            enemy.cooldown = False
            pygame.time.set_timer(hit_cooldown, 0)

        if event.type == QUIT:
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
    background.render()
    ground.render()
    xp.getxp()
    player.update()
    if player.attacking == True:
        player.attack()
    player.move()
    displaysurface.blit(player.image, player.rect)
 #   displaysurface.blit(status_bar.surf, (580, 25))
 #   status_bar.update_draw()
    enemy.update()
    enemy.move()
    if enemy.enemyhit == False:
        enemy.render()
    FPS_Clock.tick(FPS)

    pygame.draw.circle(displaysurface, black, [545, 17], 10)
    #pygame.draw.rect(displaysurface, black, pygame.Rect(560, 10, 120, 15))
    displaysurface.blit(xpbar, (560, 10))
    pygame.draw.rect(displaysurface, green, pygame.Rect(565, 13, xp.xp, 10))
    displaysurface.blit(xptext, (610, 12))
    displaysurface.blit(lvtext, (540, 9))
    pygame.display.flip()
    pygame.display.update()