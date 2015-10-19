import random

import pygame


class Galaga(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/galaga.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 550

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 12
        if key[pygame.K_RIGHT]:
            self.rect.x += dist
        elif key[pygame.K_LEFT]:
            self.rect.x -= dist

    def draw(self, surface):
        """ Draw on surface """
        surface.blit(self.image, (self.rect.x, self.rect.y))


class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """

    def __init__(self, origin):
        super().__init__()
        self.image = pygame.image.load("assets/images/galaga_bullet.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = origin.rect.x
        self.rect.y = origin.rect.y

    def update(self):
        """ Move the bullet. """
        self.rect.y -= 12


class Enemy1(pygame.sprite.Sprite):

    def __init__(self, originy):
        super().__init__()
        self.image = pygame.image.load("assets/images/enemy1.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.originx = 0
        self.originy = originy
        self.left = False
        self.rect.y = originy
        self.attack = False

    def update(self):
        """ move left - right """
        if self.left:
            self.rect.x -= 1
        else:
            self.rect.x += 1
        if abs(self.rect.x - self.originx) == 150:
            self.left = True
        elif abs(self.rect.x - self.originx) == 0:
            self.left = False

    def make_attack(self):
        """ attack the player aka galaga """
        if self.rect.y < 750:
            if self.left:
                self.rect.x -= 2
            else:
                self.rect.x += 2
            if abs(self.rect.x - self.originx) == 150:
                self.left = True
            elif abs(self.rect.x - self.originx) == 0:
                self.left = False
            self.rect.y += 5
        else: self.rect.y = self.originy


class Enemy2(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/enemy2.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.y = 35
        self.originx = 0
        self.originy = 0
        self.left = False
        self.attack = False

    def update(self):
        """ Moving back and fourth through space """

        # move left - right
        if self.left:
            self.rect.x -= 2
        else:
            self.rect.x += 2
        if abs(self.rect.x - self.originx) == 150:
            self.left = True
        elif abs(self.rect.x - self.originx) == 0:
            self.left = False
    
    def make_attack(self):
        """ attack the player aka galaga """
        
        rand = random.randrange(0, 3)
        if rand == 1:
            self.attack = True
        elif rand == 2:
            self.attack = False
        
        if self.attack:
            if self.rect.y < 750:
                if self.rect.y == 200:
                    self.rect.x += 100
                self.rect.y += 8
                self.rect.x += 5
            else:
                self.rect.y = 0
                self.rect.x -= 1

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
score = 0
running = True
clock = pygame.time.Clock()
size = (800, 600)
screen = pygame.display.set_mode(size)

# caption and mouse
pygame.display.set_caption("Galaga")
# pygame.mouse.set_visible(False)
pygame.font.init()
font_path = "assets/fonts/arcade.ttf"
fontobj = pygame.font.Font(font_path, 32)

# sprite lists
e_list = pygame.sprite.Group()
enemies = []
all_sprites_list = pygame.sprite.Group()

# create player
player = Galaga()
bullet_list = pygame.sprite.Group()

# create enemies
positions = [i for i in range(50, 750, 100)]
for i in range(6):
    e = Enemy1(originy=0)
    e.rect.x = positions[i]
    e.originx = e.rect.x
    e_list.add(e)
    all_sprites_list.add(e)
    enemies.append(e)
positions = [i for i in range(80, 750, 125)]
for i in range(5):
    e = Enemy2()
    e.rect.x = positions[i]
    e.originx = e.rect.x
    e_list.add(e)
    all_sprites_list.add(e)
    enemies.append(e)
positions = [i for i in range(50, 750, 100)]
for i in range(6):
    e = Enemy1(originy=70)
    e.rect.x = positions[i]
    e.originx = e.rect.x
    e_list.add(e)
    all_sprites_list.add(e)
    enemies.append(e)

rand_enemy_one = random.randrange(0, 4)
rand_enemy_two = random.randrange(5, 10)

def start_screen():
    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                return
        screen.fill(BLACK)
        label = fontobj.render("GALAGA BITCH", 1, (255, 255, 0))
        screen.blit(label, (300, 200))
        pygame.display.update()
        clock.tick(60)

def end_screen():
    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                finished = True
                pygame.quit()
        screen.fill(BLACK)
        label = fontobj.render("GAME OVER", 1, (255, 255, 0))
        screen.blit(label, (300, 200))
        pygame.display.update()
        clock.tick(60)

start_screen()
## Main Program Loop ##
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if len(bullet_list) <= 1:
                    info = {"origin": player}
                    bullet = Bullet(**info)
                    all_sprites_list.add(bullet)
                    bullet_list.add(bullet)

    screen.fill(BLACK)
    player.draw(screen)
    player.handle_keys()
    all_sprites_list.draw(screen)
    all_sprites_list.update()

    # win
    if not len(e_list):
        end_screen()
    # lose
    if pygame.sprite.spritecollide(player, e_list, True):
        end_screen()
        
    enemies[rand_enemy_one].make_attack()
    enemies[rand_enemy_two].make_attack()

    # get rid of bullets and collid with enemies
    for bullet in bullet_list:
        enemies_hit_list = pygame.sprite.spritecollide(bullet, e_list, True)
        for enemy in enemies_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print(score)
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    pygame.display.flip()
    clock.tick(60)
