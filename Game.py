import pygame
import sys
import random


class Menu:
    def __init__(self, punkts):
        self.window = pygame.display.set_mode((800, 600))
        self.screen = pygame.image.load("assets/backmenu.jpg").convert_alpha()
        self.punkts = punkts
        self.text = 'Created by Муравейко Владислав.'
        self.settings = ['Menu - ESC','Jump - Space', 'Стрелки вверх и вниз для ориентации по списку или мышкой',
                         'Y - Да','N - Нет']
        self.done = True
        self.hide = True
        self.punkt = 0


    def render(self,poverhnost,font):
        for i in self.punkts:
            if self.punkt == i[5]:
                poverhnost.blit(font.render(i[2],1,i[4]),(i[0],i[1]))
            else:
                poverhnost.blit(font.render(i[2],1,i[3]),(i[0],i[1]))


    def choosing(self, font_author):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    sys.exit()
                if e.key == pygame.K_UP:
                    if self.punkt > 0:
                        self.punkt -= 1
                if e.key == pygame.K_DOWN:
                    if self.punkt < len(self.punkts) - 1:
                        self.punkt += 1
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                if self.punkt == 0:
                    self.done = False
                elif self.punkt == 1:
                    if self.hide:
                        self.hide = False
                        self.screen.blit(font_author.render(str(self.text),
                                                            -1,
                                                            (255, 255, 255)),
                                         (10, 550))
                    else:
                        self.hide = True
                        self.screen.blit(font_author.render(str(self.text),
                                                            -1,
                                                            (207, 200, 23)),
                                         (10, 550))
                elif self.punkt == 2:
                    self.screen.blit(font_author.render(str(self.settings[0]),
                                                        -1,
                                                        (255, 255, 255)),
                                     (610, 450))
                    self.screen.blit(font_author.render(str(self.settings[1]),
                                                        -1,
                                                        (255, 255, 255)),
                                     (600, 500))
                    self.screen.blit(font_author.render(str(self.settings[2]),
                                                        -1,
                                                        (255, 255, 255)),
                                     (360, 550))
                    self.screen.blit(font_author.render(str(self.settings[3]),
                                                        -1,
                                                        (255, 255, 255)),
                                     (620, 400))
                    self.screen.blit(font_author.render(str(self.settings[4]),
                                                        -1,
                                                        (255, 255, 255)),
                                     (620, 350))
                elif self.punkt == 3:
                    sys.exit()


    def menu(self):
        pygame.font.init()
        font_menu = pygame.font.Font('assets/12583.otf', 50)
        font_author = pygame.font.Font('assets/12583.otf', 20)
        while self.done:
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0]>i[0] and mp[0]<i[0]+155 and mp[1]>i[1] and mp[1]<i[1]+50:
                    self.punkt = i[5]
            self.render(self.screen,font_menu)
            self.choosing(font_author)
            self.window.blit(self.screen, (0, 0))
            pygame.display.flip()


class Game_Process:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.bird = pygame.Rect(65, 50, 50, 50)
        self.background = pygame.image.load("assets/background.png").convert_alpha()
        self.birdSprites = [pygame.image.load("assets/1.png").convert_alpha(),
                            pygame.image.load("assets/2.png").convert_alpha()]
        self.over = pygame.image.load("assets/game_over.jpg").convert_alpha()
        self.ring = pygame.image.load("assets/img_0603.png").convert_alpha()
        self.gap = 130
        self.wallxFirst = 800
        self.wallxSecond = 800
        self.birdY = 350
        self.jump = 0
        self.jumpSpeed = 10
        self.gravity = 5
        self.IsOver = False
        self.IsMenu = False
        self.NoMore = [0,0]
        self.IsMore = [False,False]
        self.sprite = 0
        self.Text = ['Score:', 'Life:']
        self.NumberOfDeath = 5
        self.counter = 0
        self.first_set = random.randint(200, 400)
        self.second_set = random.randint(200, 400)
        self.rand_first = random.randint(0, 200)
        self.rand_second = random.randint(0, 200)
        self.first_speed = random.randint(1,5)
        self.second_speed = random.randint(1, 5)


    def randomize(self):
        sett = random.randint(200, 400)
        randoming = random.randint(0, 200)
        speed = random.randint(1, 5)
        return sett,randoming,speed


    def updateFirst(self):
        self.wallxFirst -= self.first_speed
        if self.wallxFirst < -80:
            self.wallxFirst = 800
            temp = self.randomize()
            self.first_set = temp[0]
            self.rand_first = temp[1]
            self.first_speed = temp[2]
            if self.IsMore[0]:
                self.IsMore[0] = False
                self.NoMore[0] = 0
            else:
                self.NumberOfDeath -= 1


    def updateSecond(self):
        self.wallxSecond -= self.second_speed
        if self.wallxSecond < -80:
            self.wallxSecond = 800
            temp = self.randomize()
            self.second_set = temp[0]
            self.rand_second = temp[1]
            self.second_speed = temp[2]
            if self.IsMore[1]:
                self.IsMore[1] = False
                self.NoMore[1] = 0
            else:
                self.NumberOfDeath -= 1


    def out_of_arena(self):
        if not 0 < self.bird[1] < 800:
            if self.NumberOfDeath <= 0:
                self.IsOver = True
                return 0
            self.NumberOfDeath -= 1
            self.bird[1] = 50
            self.birdY = 50
            self.counter = 0
            self.wallxFirst = 800
            self.wallxSecond = 800
            self.gravity = 5


    def checking_colliderect(self, upRect, downRect):
        if upRect.colliderect(self.bird):
            if self.NoMore[0] <1:
                self.IsMore[0] = True
                self.counter += 1
                self.NoMore[0] += 1
        if downRect.colliderect(self.bird):
            if self.NoMore[1] < 1:
                self.IsMore[1] = True
                self.counter += 1
                self.NoMore[1] += 1


    def birdUpdate(self):
        if self.jump:
            self.jumpSpeed -= 1
            self.birdY -= self.jumpSpeed
            self.jump -= 1
        else:
            self.birdY += self.gravity
            self.gravity += 0.2
        self.bird[1] = self.birdY
        upRect = pygame.Rect(self.wallxFirst,
                             self.first_set + self.rand_first,
                             self.ring.get_width() - 10,
                             self.ring.get_height())
        downRect = pygame.Rect(self.wallxSecond,
                               self.second_set - self.rand_second,
                               self.ring.get_width() - 10,
                               self.ring.get_height())
        self.checking_colliderect(upRect, downRect)
        if self.bird[1] <= 0:
            self.birdY = 1
            self.bird[1] = 1
        self.out_of_arena()


    def control_and_settings(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.IsMenu = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.jump = 17
                self.gravity = 5
                self.jumpSpeed = 10


    def view(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.ring,
                         (self.wallxFirst, self.first_set + self.rand_first))
        self.screen.blit(self.ring,
                         (self.wallxSecond, self.second_set - self.rand_second))


    def surprise_for_player(self):
        if self.counter % 10 == 0 and self.counter != 0:
            self.counter += 1
            self.NumberOfDeath += 1


    def status_bars(self,font):
        self.screen.blit(font.render(str(self.counter),
                                     -1,
                                     (255, 255, 255)),
                         (750, 12))
        self.screen.blit(font.render(str(self.Text[0]),
                                     -1,
                                     (255, 255, 255)),
                         (580, 10))
        self.screen.blit(font.render(str(self.Text[1]),
                                     -1,
                                     (255, 255, 255)),
                         (50, 10))
        self.screen.blit(font.render(str(self.NumberOfDeath),
                                     -1,
                                     (255, 255, 255)),
                         (160, 10))


    def end(self,clock):
        self.screen.blit(self.over, (0, 0))
        pygame.display.update()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                Game_Process().run()
            elif event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_n):
                sys.exit()


    def run(self):
        clock = pygame.time.Clock()
        pygame.font.init()
        while True:
            clock.tick(60)
            self.control_and_settings()
            self.view()
            self.status_bars(pygame.font.SysFont("Arial", 50))
            if self.IsMenu:
                break
            if self.jump:
                self.sprite = 1
            self.surprise_for_player()
            self.screen.blit(self.birdSprites[self.sprite], (70, self.birdY))
            self.sprite = 0
            self.updateFirst()
            self.updateSecond()
            self.birdUpdate()
            if self.IsOver:
                self.end(clock)
            pygame.display.update()
        if self.IsMenu:
            self.IsMenu = False
            main()


def main():
    punkts = [
        (365, 180, 'Start', (250, 250, 30), (250, 30, 250), 0),
        (360, 260, 'About', (250, 250, 30), (250, 30, 250), 1),
        (370, 340, 'Help', (250, 250, 30), (250, 30, 250), 2),
        (370, 420, 'Quit', (250, 250, 30), (250, 30, 250), 3)
    ]
    game = Menu(punkts)
    game.menu()
    Game_Process().run()


if __name__ == "__main__":
    main()