import pygame, sys

# https://www.youtube.com/watch?v=MYaxPa_eZS0&list=PL8ui5HK3oSiHnIdi0XIAVXHAeulNmBrLy&index=3

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = [] # here we load the images
        self.is_animating = False
        self.sprites.append(pygame.image.load("./resources/images/animation/attack_1.png"))
        self.sprites.append(pygame.image.load("./resources/images/animation/attack_2.png"))
        self.sprites.append(pygame.image.load("./resources/images/animation/attack_3.png"))
        self.sprites.append(pygame.image.load("./resources/images/animation/attack_4.png"))
        self.sprites.append(pygame.image.load("./resources/images/animation/attack_5.png"))
        self.sprites.append(pygame.image.load("./resources/images/animation/attack_6.png"))
        self.sprites.append(pygame.image.load("./resources/images/animation/attack_7.png"))
        self.sprites.append(pygame.image.load("./resources/images/animation/attack_8.png"))
        self.sprites.append(pygame.image.load("./resources/images/animation/attack_9.png"))
        self.sprites.append(pygame.image.load("./resources/images/animation/attack_10.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def animate(self):
        self.is_animating = True

    def update(self):
        if self.is_animating == True:
            self.current_sprite += 1
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            self.image = self.sprites[self.current_sprite]

#Pygame setup
pygame.init()
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Sprite animation")
clock = pygame.time.Clock()

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(10, 10)
moving_sprites.add(player)
while True:
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            player.animate()
    #drawing
    screen.fill('black')
    moving_sprites.draw(screen)
    moving_sprites.update() # this will call update method on every sprite in the group
    pygame.display.flip()
    clock.tick(60)