import sys
from operator import itemgetter
import sqlite3

import pygame

WIDTH = 650
HEIGHT = 675
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Star Fighter")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


running = True
results = []
con = sqlite3.connect("data/scores.db")
cur = con.cursor()
result = cur.execute("""SELECT * FROM results
            WHERE SCORE > 0""").fetchall()
for elem in result:
    results.append(elem)
results.sort(key=itemgetter(1), reverse=True)
con.close()


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    scores = []
    scores.append("Дата и время           Счет")
    if len(results) > 10:
        for i in range(len(results)):
            if i <= 10:
                res_ = results[i][0] + "     " + str(results[i][1])
                scores.append(res_)
    elif len(results) <= 10:
        for i in range(len(results)):
            res_ = results[i][0] + "     " + str(results[i][1])
            scores.append(res_)
    scores.append('    Вернуться назад[S]')
    stars = open("stars_res.txt", 'r', encoding='utf8').read()
    stars = stars.split('\n')
    title_text = ["   Лучшие результаты"]
    screen.fill(BLACK)
    for i in range(1000):
        screen.fill(pygame.Color('white'),
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
        screen.blit(string_rendered, intro_rect)
    for line in scores:
        string_rendered = font_.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                import test_game
        pygame.display.flip()
        clock.tick(FPS)



start_screen()
terminate()