from pygame import *

back = (200, 255, 255)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
display.set_caption('')

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed


player = Player('3.png', 5, 200, 10, 50, 150)
player1 = Player('3.png', 645, 200, 10, 50, 150)
ball = GameSprite('ball.png', 325, 200, 10, 50, 50)


speed_x = 1
speed_y = 1
finish = False
clock = time.Clock()
FPS = 60
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        player.update_l()
        player1.update_r()
        player.reset()
        player1.reset()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    display.update()
    clock.tick(FPS)