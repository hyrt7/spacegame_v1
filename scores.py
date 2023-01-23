import pygame.font


class Scores():
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (0, 255, 9)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.show_highscore()
        self.show_score()


    def show_highscore(self):
        self.highscore_img = self.font.render(str(self.stats.highscore), True, self.text_color, (0, 0, 0))
        self.highscore_rect = self.highscore_img.get_rect()
        self.highscore_rect.centerx = self.screen_rect.centerx
        self.highscore_rect.top = self.screen_rect.top + 20


    def image_score(self):
        self.score_image = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highscore_img, self.highscore_rect)