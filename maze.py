from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_h - 80:
            self.rect.y += self.speed
        if keys[K_d] and self.rect.x < win_w - 80:
            self.rect.x += self.speed
        if keys[K_a] and self.rect.x > 10:
            self.rect.x -= self.speed

class Enemy(GameSprite):
    nap = 'left'
    def update(self):
        if self.rect.x <= 450:
            self.nap = 'right'
        if self.rect.x >= win_w - 80:
            self.nap = 'left'

        if self.nap == 'right':
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed



win_w = 700
win_h = 500
window = display.set_mode((win_w,win_h))
display.set_caption('Лабиринт')
background= transform.scale(image.load('background.jpg'),(win_w,win_h))

player = Player('hero.png',5,win_h - 80,4)
monster = Enemy('cyborg.png',3, win_w - 80, 280)
gold = GameSprite('treasure.png',0,win_w - 120, win_h-80)

game = True 
FPS = 60
clock = time.Clock()

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    window.blit(background,(0,0))

    player.update()
    monster.update()

    player.reset()
    monster.reset()
    gold.reset()

    display.update()
    clock.tick(FPS)