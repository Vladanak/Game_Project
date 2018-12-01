from Game_menu import *


class GameProcess:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.bird = pygame.Rect(65, 50, 50, 50)
        self.background = pygame.image.load("assets/background.png").convert_alpha()
        self.birdSprites = [pygame.image.load("assets/1.png").convert_alpha(),
                            pygame.image.load("assets/2.png").convert_alpha()]
        self.over = pygame.image.load("assets/game_over.jpg").convert_alpha()
        self.ring = pygame.image.load("assets/img_0603.png").convert_alpha()
        self.Text = ['Score:', 'Life:']
        self.gap = 130
        self.ringXfirst = self.ringXsecond = 800
        self.sprite = self.jump = self.counter = 0
        self.birdY = 350
        self.jumpSpeed = 10
        self.gravity = 5
        self.NumberOfDeath = 5
        self.NoMore = [0, 0]
        self.IsOver = self.IsMenu = False
        self.IsMore = [False, False]
        self.first_set = self.second_set = random.randint(200, 400)
        self.rand_first = self.rand_second = random.randint(0, 200)
        self.first_speed = self.second_speed = random.randint(1, 5)


    def update_first(self):
        self.ringXfirst -= self.first_speed
        if self.ringXfirst < -80:
            self.ringXfirst = 800
            self.first_set, self.rand_first, self.first_speed = randomize()
            if self.IsMore[0]:
                self.IsMore[0] = False
                self.NoMore[0] = 0
            else:
                self.NumberOfDeath -= 1


    def update_second(self):
        self.ringXsecond -= self.second_speed
        if self.ringXsecond < -80:
            self.ringXsecond = 800
            self.second_set, self.rand_second, self.second_speed = randomize()
            if self.IsMore[1]:
                self.IsMore[1] = False
                self.NoMore[1] = 0
            else:
                self.NumberOfDeath -= 1


    def is_death(self):
        if self.NumberOfDeath <= 0:
            self.IsOver = True


    def out_of_arena(self):
        if not 0 < self.bird[1] < 800:
            self.NumberOfDeath -= 1
            self.bird[1] = 50
            self.birdY = 50
            self.counter = 0
            self.ringXfirst = self.ringXsecond = 800
            self.gravity = 5


    def checking_colliderect(self, up_rect, down_rect): #пересечение кольца с птичкой
        if up_rect.colliderect(self.bird):
            if self.NoMore[0] < 1:
                self.IsMore[0] = True
                self.counter += 1
                self.NoMore[0] += 1
        if down_rect.colliderect(self.bird):
            if self.NoMore[1] < 1:
                self.IsMore[1] = True
                self.counter += 1
                self.NoMore[1] += 1


    def bird_update(self):
        if self.jump:
            self.jumpSpeed -= 1
            self.birdY -= self.jumpSpeed
            self.jump -= 1
        else:
            self.birdY += self.gravity
            self.gravity += 0.2
        self.bird[1] = self.birdY
        up_rect = pygame.Rect(self.ringXfirst,
                             self.first_set + self.rand_first,
                             self.ring.get_width() - 10,
                             self.ring.get_height())
        down_rect = pygame.Rect(self.ringXsecond,
                               self.second_set - self.rand_second,
                               self.ring.get_width() - 10,
                               self.ring.get_height())
        self.checking_colliderect(up_rect, down_rect)
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
                         (self.ringXfirst, self.first_set + self.rand_first))
        self.screen.blit(self.ring,
                         (self.ringXsecond, self.second_set - self.rand_second))


    def surprise_for_player(self):
        if self.counter % 10 == 0 and self.counter != 0:
            self.counter += 1
            self.NumberOfDeath += 1


    def status_bars(self, font):
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


    def end(self, clock):
        self.screen.blit(self.over, (0, 0))
        pygame.display.update()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                GameProcess().run()
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
            self.update_first()
            self.update_second()
            self.bird_update()
            self.is_death()
            if self.IsOver:
                self.end(clock)
            pygame.display.update()
        if self.IsMenu:
            self.IsMenu = False
            main()


def main():
    main_menu()
    GameProcess().run()


if __name__ == "__main__":
    main()