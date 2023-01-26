import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, gun):
        #пуля из пушки
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 5 , 12)
        self.color = 0, 255, 9
        self.speed = 4
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)


    def update(self):
        #перемещение пушки вверх
        self.y -= self.speed
        self. rect.y = self.y


    def draw_bullet(self):
        #рисование пули на экране
        pygame.draw.rect(self.screen, self.color, self.rect)
