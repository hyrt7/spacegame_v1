import pygame


class Stats():
    #Статистика
    def __init__(self):
        #инициализация статистики
        self.reset_stats()
        self.run_game = True
        f = open('1.txt')
        self.highscore = int(f.readline())


    def reset_stats(self):
        #статистика которая изменяется во время игры
        self.guns_lives_left = 1
        self.score = 0