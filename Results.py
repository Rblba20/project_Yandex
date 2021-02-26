from Start import *
import sqlite3
import sys
from operator import itemgetter

import pygame


class Results(Start):
    def __init__(self, screen, width, height):
        super().__init__(width, height, screen)
        self.font_name = pygame.font.match_font('arial')
        self.WHITE = (255, 255, 255)
        self.results = []
        self.scores = []
        self.BLACK = (0, 0, 0)
        self.FPS = 50
        self.screen = screen
        con = sqlite3.connect("data/scores.db")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM results
                    WHERE SCORE > 0""").fetchall()
        for elem in result:
            self.results.append(elem)
        self.results.sort(key=itemgetter(1), reverse=True)
        con.close()

    def draw_text(self, surf, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    def terminate(self):
        pygame.quit()
        sys.exit()

    def start_screen(self):
        self.scores.append("Дата и время           Счет")
        if len(self.results) > 10:
            for i in range(len(self.results)):
                if i <= 10:
                    res_ = self.results[i][0] + "     " + str(self.results[i][1])
                    self.scores.append(res_)
        elif len(self.results) <= 10:
            for i in range(len(self.results)):
                res_ = self.results[i][0] + "     " + str(self.results[i][1])
                self.scores.append(res_)
        self.scores.append('    Вернуться назад[S]')
        stars = open("stars_res.txt", 'r', encoding='utf8').read()
        stars = stars.split('\n')
        title_text = ["   Лучшие результаты"]
        self.screen.fill(self.BLACK)
        for i in range(1000):
            self.screen.fill(pygame.Color('white'),
                             (float(stars[i + 0]),
                              float(stars[i + 1]), 1, 1))
        font = pygame.font.Font('data/text.ttf', 50)
        font_ = pygame.font.Font('data/text.ttf', 35)
        text_coord = 10
        for line in title_text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            self.screen.blit(string_rendered, intro_rect)
        for line in self.scores:
            string_rendered = font_.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            self.screen.blit(string_rendered, intro_rect)
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fout = open("plane.txt", "wt", encoding="utf8")
                    fout.write("")
                    fout.close()
                    self.terminate()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    start = Start(650, 675, self.screen)
                    start.start_screen()
            pygame.display.flip()
            clock.tick(self.FPS)
