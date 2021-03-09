from Border import *from Enemy import *from Explosion import *from Mob import *from Player import *from Pow import *import datetimeimport sqlite3import pygameimport randomfrom os import pathclass Main:    def __init__(self):        from Start import Start        self.class_start = Start        self.img_dir = path.join(path.dirname(__file__), 'data')        self.snd_dir = path.join(path.dirname(__file__), 'data')        self.width, self.height = 650, 675        self.FPS = 60        self.POWERUP_TIME = 5000        self.score = 0        self.all_sprites = pygame.sprite.Group()        self.WHITE = (255, 255, 255)        self.BLACK = (0, 0, 0)        self.GREEN = (0, 255, 0)        pygame.init()        pygame.mixer.init()        self.screen = pygame.display.set_mode((self.width, self.height))        pygame.display.set_caption("Star Fighter")        self.clock = pygame.time.Clock()        self.font_name = pygame.font.match_font('arial')    def draw_text(self, surf, text, size, x, y):        font = pygame.font.Font(self.font_name, size)        text_surface = font.render(text, True, self.WHITE)        text_rect = text_surface.get_rect()        text_rect.midtop = (x, y)        surf.blit(text_surface, text_rect)    def draw_hp_bar(self, surf, x, y, pct):        if pct < 0:            pct = 0        BAR_LENGTH = 100        BAR_HEIGHT = 10        fill = (pct / 100) * BAR_LENGTH        outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)        pygame.draw.rect(surf, self.GREEN, fill_rect)        pygame.draw.rect(surf, self.WHITE, outline_rect, 2)    def draw_lives(self, surf, x, y, lives, img):        for i in range(lives):            img_rect = img.get_rect()            img_rect.x = x + 30 * i            img_rect.y = y            surf.blit(img, img_rect)    def show_end_screen(self):        if self.start > 0:            background = pygame.image.load(path.join(self.img_dir, "fon.jpg")).convert()            background_rect = background.get_rect()            self.screen.blit(background, background_rect)            self.draw_text(self.screen, "GAME OVER", 64, self.width / 2, self.height / 4)            self.draw_text(self.screen, f"Вас счет: {self.score}", 22,                           self.width / 2, self.height / 2)            self.draw_text(self.screen, "Нажмите F, чтобы продолжить", 18, self.width / 2, self.height * 3 / 4)            pygame.display.flip()            waiting = True            while waiting:                self.clock.tick(self.FPS)                for event in pygame.event.get():                    if event.type == pygame.QUIT:                        fout = open("plane.txt", "wt", encoding="utf8")                        fout.write("")                        fout.close()                        pygame.quit()                    if event.type == pygame.KEYDOWN and event.key == pygame.K_f:                        waiting = False            s = self.class_start(self.width, self.height, self.screen)            s.start_screen()    def interface(self):        self.delay = []        for i in range(1000, 1750):            self.delay.append(i)        self.point = []        for i in range(10, 500):            self.point.append(i)        self.bullet_images = []        bullet_list = ['laserBlue05.png', 'laserGreen05.png', 'laserRed01.png',                       'laserRed05.png']        for img in bullet_list:            self.bullet_images.append(pygame.image.load(path.join(self.img_dir, img)).convert())        self.bullet_img = pygame.image.load(path.join(self.img_dir, "laserBlue05.png")).convert()        self.enemy_images = []        enemy_list = ['enemyBlack1.png', 'enemyBlue2.png', 'enemyGreen3.png',                      'enemyRed4.png']        for img in enemy_list:            self.enemy_images.append(pygame.image.load(path.join(self.img_dir, img)).convert())        self.horizontal_borders = pygame.sprite.Group()        self.vertical_borders = pygame.sprite.Group()        self.all_sprites_list = pygame.sprite.Group()        self.projectiles = pygame.sprite.Group()        enemy_sprites = pygame.sprite.Group()        self.shoot_sound = pygame.mixer.Sound(path.join(self.snd_dir, 'pew.wav'))        if self.score > 0:            enemy = Enemy(20, 100, 100, 150, 150, self.projectiles, self.enemy_images, self.delay, self.point,                          self.all_sprites, self.width, self.height,                          self.horizontal_borders, self.vertical_borders, self.bullet_images, self.shoot_sound)            enemy_sprites.add(enemy)        Border(5, 5, self.width - 5, 5, self.all_sprites, self.vertical_borders, self.horizontal_borders)        Border(5, self.height / 2, self.width - 5, self.height / 2, self.all_sprites, self.vertical_borders,               self.horizontal_borders)        Border(5, 5, 5, self.height - 5, self.all_sprites, self.vertical_borders, self.horizontal_borders)        Border(self.width - 5, 5, self.width - 5, self.height - 5, self.all_sprites, self.vertical_borders,               self.horizontal_borders)        if self.score > 0:            for i in range(10):                Enemy(20, 100, 100, 150, 150, self.projectiles, self.enemy_images, self.delay,                      self.point, self.all_sprites,                      self.width, self.height, self.horizontal_borders,                      self.vertical_borders, self.bullet_images, self.shoot_sound)        text = open("plane.txt", encoding='utf8').read()        if text != "":            player_img = pygame.image.load(path.join(self.img_dir, text)).convert()            player_mini_img = pygame.transform.scale(player_img, (25, 19))            player_mini_img.set_colorkey(self.BLACK)        if text == "":            player_img = pygame.image.load(path.join(self.img_dir, 'playerShip2_blue.png')).convert()            player_mini_img = pygame.transform.scale(player_img, (25, 19))            player_mini_img.set_colorkey(self.BLACK)        self.bullet_img = pygame.image.load(path.join(self.img_dir, "laserRed05.png")).convert()        self.meteor_images = []        meteor_list = ['meteorBrown_big1.png', 'meteorBrown_med1.png', 'meteorBrown_med1.png',                       'meteorBrown_med3.png', 'meteorBrown_small1.png', 'meteorBrown_small2.png',                       'meteorBrown_tiny1.png']        for img in meteor_list:            self.meteor_images.append(pygame.image.load(path.join(self.img_dir, img)).convert())        explosion_anim = {}        explosion_anim['lg'] = []        explosion_anim['sm'] = []        explosion_anim['player'] = []        for i in range(9):            filename = 'regularExplosion0{}.png'.format(i)            img = pygame.image.load(path.join(self.img_dir, filename)).convert()            img.set_colorkey(self.BLACK)            img_lg = pygame.transform.scale(img, (75, 75))            explosion_anim['lg'].append(img_lg)            img_sm = pygame.transform.scale(img, (32, 32))            explosion_anim['sm'].append(img_sm)            filename = 'sonicExplosion0{}.png'.format(i)            img = pygame.image.load(path.join(self.img_dir, filename)).convert()            img.set_colorkey(self.BLACK)            explosion_anim['player'].append(img)        powerup_images = {}        powerup_images['shield'] = \            pygame.image.load(                path.join(self.img_dir, '3668853-ambulance-expense-healthcare-medicine_1080161.png')).convert()        powerup_images['gun'] = pygame.image.load(path.join(self.img_dir, 'bolt_gold.png')).convert()        self.shoot_sound = pygame.mixer.Sound(path.join(self.snd_dir, 'pew.wav'))        shield_sound = pygame.mixer.Sound(path.join(self.snd_dir, 'Powerup4.wav'))        power_sound = pygame.mixer.Sound(path.join(self.snd_dir, 'Powerup5.wav'))        expl_sounds = []        for snd in ['expl3.wav', 'expl6.wav']:            expl_sounds.append(pygame.mixer.Sound(path.join(self.snd_dir, snd)))        self.all_sprites = pygame.sprite.Group()        self.mobs = pygame.sprite.Group()        bullets = pygame.sprite.Group()        powerups = pygame.sprite.Group()        player = Player(self.width, self.height, player_img, self.POWERUP_TIME,                        self.all_sprites, bullets, self.shoot_sound, self.bullet_img)        self.all_sprites.add(player)        for i in range(8):            self.newmob()        self.score = 0        game_over = True        running = True        stars = open("stars.txt", 'r', encoding='utf8').read()        stars = stars.split('\n')        check = open("plane.txt", 'r', encoding='utf8').read()        if check == "":            self.start = 0        elif check != "":            self.start = 50        while running:            if game_over:                if self.score != 0:                    data_time = datetime.datetime.now()                    fout = open("plane.txt", "wt", encoding="utf8")                    fout.write("")                    fout.close()                    conn = sqlite3.connect('data/scores.db')                    cr = conn.cursor()                    similar = cr.execute("""SELECT * FROM results WHERE SCORE == ?""",                                         (self.score,)).fetchall()                    print(similar)                    if similar == []:                        cr.execute("""DELETE from results where SCORE == ?""",                                   (self.score,))                    cr.execute("""INSERT INTO results(DATE_TIME,SCORE) VALUES(?,?)""",                               (data_time.strftime('%d-%m-%Y %H:%M:%S'), self.score))                    # SELECT SCORE FROM results                    #     WHERE SCORE > 0                    conn.commit()                    conn.close()                    print(self.score)                    print(data_time.strftime('%d-%m-%Y %H:%M:%S'))                    self.show_end_screen()                game_over = False                #      all_sprites = pygame.sprite.Group()                #      mobs = pygame.sprite.Group()                #     bullets = pygame.sprite.Group()                #    powerups = pygame.sprite.Group()                #    player = Player(width, height, player_img, POWERUP_TIME, all_sprites, bullets, shoot_sound, bullet_img)                #    all_sprites.add(player)                #   for i in range(8):                #       newmob()                self.score = 0                if ((self.score == 0 and self.start == 0) or (self.score == 0 and self.start % 2 != 0)) \                        and self.start != 50:                    s = self.class_start(self.width, self.height, self.screen)                    s.start_screen()                    self.start += 1            self.clock.tick(self.FPS)            for event in pygame.event.get():                if event.type == pygame.QUIT:                    fout = open("plane.txt", "wt", encoding="utf8")                    fout.write("")                    fout.close()                    running = False                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:                    self.draw_text(self.screen, "Пауза", 64, self.width / 2, self.height / 4)                    self.draw_text(self.screen, "Нажмите F, чтобы продолжить", 18, self.width / 2, self.height * 3 / 4)                    pygame.display.flip()                    waiting = True                    while waiting:                        self.clock.tick(self.FPS)                        for event in pygame.event.get():                            if event.type == pygame.QUIT:                                fout = open("plane.txt", "wt", encoding="utf8")                                fout.write("")                                fout.close()                                pygame.quit()                            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:                                waiting = False            self.all_sprites.update()            hits = pygame.sprite.groupcollide(self.mobs, bullets, True, True)            for hit in hits:                self.score += 50 - hit.radius                random.choice(expl_sounds).play()                expl = Explosion(hit.rect.center, 'lg', explosion_anim)                self.all_sprites.add(expl)                if random.random() > 0.9:                    pow = Pow(hit.rect.center, self.height, powerup_images)                    self.all_sprites.add(pow)                    powerups.add(pow)                if self.score <= 500:                    self.newmob()                elif self.score > 500:                    self.newenemy()            hits = pygame.sprite.spritecollide(player, self.mobs, True, pygame.sprite.collide_circle)            for hit in hits:                player.shield -= hit.radius * 2                expl = Explosion(hit.rect.center, 'sm', explosion_anim)                self.all_sprites.add(expl)                self.newmob()                if player.shield <= 0:                    death_explosion = Explosion(player.rect.center, 'player', explosion_anim)                    self.all_sprites.add(death_explosion)                    player.hide()                    player.lives -= 1                    player.shield = 100            hits = pygame.sprite.spritecollide(player, self.projectiles, True, pygame.sprite.collide_circle)            for hit in hits:                player.shield -= hit.radius * 2                if player.shield <= 0:                    death_explosion = Explosion(player.rect.center, 'player', explosion_anim)                    self.all_sprites.add(death_explosion)                    player.hide()                    player.lives -= 1                    player.shield = 100            hits = pygame.sprite.spritecollide(player, powerups, True)            for hit in hits:                if hit.type == 'shield':                    player.shield += random.randrange(10, 30)                    shield_sound.play()                    if player.shield >= 100:                        player.shield = 100                if hit.type == 'gun':                    player.powerup()                    power_sound.play()            if player.lives == 0 and not death_explosion.alive():                game_over = True            self.screen.fill(self.BLACK)            for i in range(5000):                self.screen.fill(pygame.Color('white'),                                 (float(stars[i + 0]),                                  float(stars[i + 1]), 1, 1))            self.all_sprites.draw(self.screen)            self.draw_text(self.screen, str(self.score), 18, self.width / 2, 10)            self.draw_hp_bar(self.screen, 5, 5, player.shield)            self.draw_lives(self.screen, self.width - 100, 5, player.lives,                            player_mini_img)            self.horizontal_borders.draw(self.screen)            self.vertical_borders.draw(self.screen)            self.all_sprites.draw(self.screen)            self.all_sprites.update()            self.all_sprites_list.update()            self.projectiles.update()            enemy_sprites.update()            self.all_sprites_list.draw(self.screen)            self.projectiles.draw(self.screen)            enemy_sprites.draw(self.screen)            pygame.display.flip()        pygame.quit()    def newmob(self):        m = Mob(self.meteor_images, self.width, self.height)        self.all_sprites.add(m)        self.mobs.add(m)    def newenemy(self):        if self.score > 0:            m = Enemy(20, 100, 100, 150, 150, self.projectiles, self.enemy_images, self.delay, self.point,                      self.all_sprites, self.width, self.height,                      self.horizontal_borders, self.vertical_borders, self.bullet_images, self.shoot_sound)            self.all_sprites.add(m)            self.mobs.add(m)if __name__ == '__main__':    main_ = Main()    main_.interface()# import os# import random# import sys# import pygame# pygame.init()# pygame.display.set_caption('Star Fighter')# size = width, height = 650, 675# screen = pygame.display.set_mode(size)# start_screen()# terminate()