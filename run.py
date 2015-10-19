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
        dist = 12 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_RIGHT]: # right key
            self.rect.x += dist # move right
        elif key[pygame.K_LEFT]: # left key
            self.rect.x -= dist # move left

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.rect.x, self.rect.y))


class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.image.load("assets/images/galaga_bullet.png").convert()
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the bullet. """
        self.rect.y -= 3


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/enemy1.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()


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

# sprite lists
e_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
# create player
player = Galaga()
bullet_list = pygame.sprite.Group()

# create enemies
positions = [i for i in range(25, 700, 50)]
for i in range(14):
    e = Enemy()
    e.rect.x = positions[i]
    # e.rect.y = positions[i]
    e_list.add(e)
    all_sprites_list.add(e)

## Main Program Loop ##
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet()
            # Set the bullet so it is where the player is
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)

    player.handle_keys()
    all_sprites_list.update()
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

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)
    player.draw(screen)
    all_sprites_list.draw(screen)
    # Update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(60)