import pygame


class Gun():
    def __init__(self, screen):
        #инициализация пушки"""
        self.screen = screen
        self.image = pygame.image.load('images/gun.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.move_right = False
        self.move_left = False


    def draw_gun(self):
        #рисование пушки
        self.screen.blit(self.image, self.rect)


    def update_gun(self):
        #обновление пушки
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += 0.6
        if self.move_left and self.rect.left > self.screen_rect.left:
            self.center -= 0.6

        self.rect.centerx = self.center


    def create_gun(self):
        #воскресание пушки
        self.center = self.screen_rect.centerx