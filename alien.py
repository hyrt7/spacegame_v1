import pygame, random

class Alien(pygame.sprite.Sprite):
    """Пришелец"""
    def  __init__(self, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.alien_image1 = pygame.image.load('images/alien1.png')
        self.alien_image2 = pygame.image.load('images/alien2.png')
        self.alien_image3 = pygame.image.load('images/alien3.png')
        self.image = random.choice([self.alien_image1, self.alien_image2, self.alien_image3])
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def draw(self):
        """Отрисовка пришельца"""
        self.screen.blit(self.image, self.rect)


    def update(self):
        """Перемещение пришельца"""
        self.y += 0.1
        self.rect.y = self.y
