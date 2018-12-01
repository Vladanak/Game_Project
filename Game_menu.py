from libs import *


def main_menu():
    punkts = [
        (365, 180, 'Start', (250, 250, 30), (250, 30, 250), 0),
        (360, 260, 'About', (250, 250, 30), (250, 30, 250), 1),
        (370, 340, 'Help', (250, 250, 30), (250, 30, 250), 2),
        (370, 420, 'Quit', (250, 250, 30), (250, 30, 250), 3)
    ]
    game = Menu(punkts)
    game.menu()


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


    def render_text(self,font,text,tuple): #для отображения текса расширение сделал
        self.screen.blit(font.render(text, -1, (255, 255, 255)), tuple)


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
                        self.render_text(font_author, text=str(self.text), tuple=(10, 550))
                    else:
                        self.hide = True
                        self.screen.blit(font_author.render(str(self.text),
                                                            -1,
                                                            (207, 200, 23)),
                                         (10, 550))
                elif self.punkt == 2:
                    self.render_text(font_author, text=str(self.settings[0]), tuple=(610, 450))
                    self.render_text(font_author, text=str(self.settings[1]), tuple=(600, 500))
                    self.render_text(font_author, text=str(self.settings[2]), tuple=(360, 550))
                    self.render_text(font_author, text=str(self.settings[3]), tuple=(620, 400))
                    self.render_text(font_author, text=str(self.settings[4]), tuple=(620, 350))
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
