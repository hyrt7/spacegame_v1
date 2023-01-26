import pygame, sys, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption('Звездные Защитники')
    icon = pygame.image.load('images/alien2.png')
    pygame.display.set_icon(icon)
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    aliens = Group()
    controls.create_army(screen, aliens)
    stats = Stats()
    scores = Scores(screen, stats)
    controls.start_screen(screen)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, scores, gun, aliens, bullets)
            controls.update_bullets(screen,stats, scores, aliens, bullets)
            controls.update_aliens(stats, screen, gun, aliens, bullets, scores)


run()