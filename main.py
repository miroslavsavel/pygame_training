import pygame, sys

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color):
        super().__init__()
        self.image = pygame.Surface([width,height]) #empty surface
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

#Pygame setup
pygame.init()
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

crosshair = Crosshair(50, 50, 100, 100, (255, 255, 255))
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    crosshair_group.draw(screen)
    clock.tick(60)