#from Choose import Choose
import os
import random
import sys

import pygame


class Start:
    def __init__(self, width, height, screen):
        from Results import Results
        from Choose import Choose
        self.class_choose = Choose
        self.class_results = Results
        self.width = width
        self.height = height
        self.FPS = 50
        self.screen = screen

    def load_image(self, name, colorkey=None):
        fullname = os.path.join('data', name)
        image = pygame.image.load(fullname)
        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image

    def terminate(self):
        pygame.quit()
        sys.exit()

    def start_screen(self):
        pygame.init()
        intro_text = ["  Star Fighter", "",
                      "[Z]Играть",
                      "[S]Результаты",
                      "[X]Выход", ""]
        rights = ["© Made by Rblba20 and lapin01", "",
                  "All rights reserved"]

        fon = pygame.transform.scale(self.load_image('fon.jpg'), (self.width, self.height))
        self.screen.blit(fon, (0, 0))
        font = pygame.font.Font('data/text.ttf', 70)
        font_ = pygame.font.Font('data/text.ttf', 35)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            self.screen.blit(string_rendered, intro_rect)
        for line in rights:
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
                if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                    self.perehod('z')
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    self.perehod('s')
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                    self.terminate()
            pygame.display.flip()
            clock.tick(self.FPS)

    def perehod(self, key):
        time = 0
        running = True
        while running and time < 30:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fout = open("plane.txt", "wt", encoding="utf8")
                    fout.write("")
                    fout.close()
                    running = False
            clock = pygame.time.Clock()
            for i in range(10000):
                self.screen.fill(pygame.Color('black'),
                                 (random.random() * self.width,
                                  random.random() * self.height, 1, 1))
            pygame.display.flip()
            clock.tick(self.FPS)
            time += 0.1
        if time >= 30 and key == 'z':
            self.game_window()
            return
        if time >= 30 and key == 's':
            self.results()
            return

    def game_window(self):
        g = 1
        stars = []
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fout = open("plane.txt", "wt", encoding="utf8")
                    fout.write("")
                    fout.close()
                    running = False
            clock = pygame.time.Clock()
            if g <= 200:
                for i in range(25):
                    star_x = random.random() * self.width
                    star_y = random.random() * self.height
                    self.screen.fill(pygame.Color('white'),
                                     (star_x,
                                      star_y, 1, 1))
                    stars.append([star_x, star_y])
            else:
                for i in range(5000):
                    self.screen.fill(pygame.Color('white'),
                                     (stars[i][0],
                                      stars[i][1], 1, 1))
            pygame.display.flip()
            clock.tick(self.FPS)
            if g > 250:
                new_list = []
                for i in stars:
                    for j in i:
                        new_list.append(str(j) + '\n')
                with open('stars.txt', 'w') as f:
                    f.writelines(new_list)
                    choose = self.class_choose(self.screen)
                    choose.start_screen()
            g += 1

    def results(self):
        g = 1
        stars = []
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fout = open("plane.txt", "wt", encoding="utf8")
                    fout.write("")
                    fout.close()
                    running = False
            clock = pygame.time.Clock()
            if g <= 40:
                for i in range(25):
                    star_x = random.random() * self.width
                    star_y = random.random() * self.height
                    self.screen.fill(pygame.Color('white'),
                                     (star_x,
                                      star_y, 1, 1))
                    stars.append([star_x, star_y])
            else:
                for i in range(1000):
                    self.screen.fill(pygame.Color('white'),
                                     (stars[i][0],
                                      stars[i][1], 1, 1))
            pygame.display.flip()
            clock.tick(self.FPS)
            if g > 45:
                new_list = []
                for i in stars:
                    for j in i:
                        new_list.append(str(j) + '\n')
                with open('stars_res.txt', 'w') as f:
                    f.writelines(new_list)
                    results = self.class_results(self.screen, 650, 675)
                    results.start_screen()
            g += 1


#start = Start(650, 675, pygame.display.set_mode((650, 675)))
#start.start_screen()
