import random

import pygame, sys

class Crosshair(pygame.sprite.Sprite):
    def __init__(self,  picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("./resources/sounds/gunshot_1.wav")

    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True) # it will checks two groups of sprites

    def update(self):
        # method predefined in originla Sprite class
        self.rect.center = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

#Pygame setup
pygame.init()
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
background = pygame.image.load("./resources/images/bg_blue.png")
background = pygame.transform.scale(background, (screen_width, screen_height))
pygame.mouse.set_visible(False)

# Crosshair
crosshair = Crosshair("./resources/images/crosshair_red_small.png")
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

#Target
target_group = pygame.sprite.Group()
for target in range(20):
    #create new target in random position
    new_target = Target("./resources/images/target_colored.png", random.randrange(0, screen_width), random.randrange(0, screen_height))
    target_group.add(new_target)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()

    pygame.display.flip()
    screen.blit(background,(0,0))
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(60)