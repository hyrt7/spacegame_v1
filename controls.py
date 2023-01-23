import pygame, sys, pygame.font

import scores
from bullet import Bullet
from alien import Alien
import time


a = 12
def events(screen, gun, bullets):
    #обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #вправо
            if event.key == pygame.K_d:
                gun.move_right = True
            #влево
            elif event.key == pygame.K_a:
                gun.move_left = True
            #выстрел
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            #вправо
            if event.key == pygame.K_d:
                gun.move_right = False
            #влево
            elif event.key == pygame.K_a:
                gun.move_left = False


def update(bg_color, screen, stats, scores, gun, aliens, bullets):
    #обновление экрана
    screen.fill(bg_color)
    scores.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.draw_gun()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(screen, stats, scores, aliens, bullets):
    #обновление позиции пуль
    bullets.update()
    check_high_score(stats, scores)
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += 10 * len(aliens)
        scores.image_score()
        check_high_score(stats, scores)
    if len(aliens) == 0:
        bullets.empty()
        create_army(screen, aliens)


def gun_kill(stats, screen, gun, aliens, bullets, scores):
    #столкновение пушки и пришельцов
    stats.guns_lives_left -= 1
    if stats.guns_lives_left > 0:
        aliens.empty()
        bullets.empty()
        create_army(screen, aliens)
        gun.create_gun()
        time.sleep(1.5)
    else:
        time.sleep(3)
        sys.exit()


def update_aliens(stats, screen, gun, aliens, bullets, scores):
    #обновление позиции прищельцов
    aliens.update()
    if pygame.sprite.spritecollideany(gun, aliens):
        gun_kill(stats, screen, gun, aliens, bullets, scores)
    aliens_check(stats, screen, gun, aliens, bullets, scores)


def aliens_check(stats, screen, gun, aliens, bullets, scores):
    #если пришельцы доходят до края
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, gun, aliens, bullets, scores)
            break


def create_army(screen, aliens):
    global a
    a -= 1
    #создание армии пришельцов
    alien = Alien(screen)
    alien_width = alien.rect.width
    number_alien_x = int((700 - 2 * alien_width) / alien_width)
    alien_height = alien.rect.height
    number_alien_y = int((800 - 100 - 2 * alien_height) / alien_height)
    for row_number in range(number_alien_y - a):
        for alien_number in range(number_alien_x):
            alien = Alien(screen)
            alien.x = alien_width + (alien_width * alien_number)
            alien.y = alien_height + (alien_height * row_number)
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + alien.rect.height * row_number
            aliens.add(alien)


def check_high_score(stats, scores):
    f = open('1.txt', 'w')
    f.write(str(stats.highscore))
    if stats.score > stats.highscore:
        stats.highscore = stats.score
        scores.show_highscore()
        f = open('1.txt', 'w')
        f.write(str(stats.highscore))