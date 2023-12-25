import pygame
pygame.init()

class Station(pygame.sprite.Sprite):
    def __init__(self, size, names, center):
        super().__init__()
        self.image = pygame.Surface(size)
        self.names = names
        self.rect = self.image.get_rect()
        self.rect.center = center

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("DGMetro Beta Build 1")

running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()
