import pygame, sys

class Crosshair(pygame.sprite.Sprite):
    def __init__(self,  picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()

    def update(self):
        # method predefined in originla Sprite class
        self.rect.center = pygame.mouse.get_pos()


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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    screen.blit(background,(0,0))
    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(60)