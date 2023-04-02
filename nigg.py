from pygame import *
from random import randint
import time as time_module

font.init()
window = display.set_mode((1000, 700))
display.set_caption('Пудж варс')
background = transform.scale(image.load('phone.jpg'), (1000, 700))
clock = time.Clock()
mixer.init()
lost = 0
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w, h))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > 700:
            self.rect.y = 0
            self.speed = randint(1,4)
            self.rect.x = randint(5, 895)
            lost += 1


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y == 700:
            self.kill()



class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if key_pressed[K_d] and self.rect.x < 1000 - 175 - 5:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('hok.png', self.rect.centerx - 30, self.rect.top,  5,  65,65)
        bullets.add(bullet)
        hook.play()






rel_time = False
num_fire = 0
finish = False
game = True
font = font.Font(None, 40)
mixer.music.load('music.ogg')
mixer.music.play(-1)
hook = mixer.Sound('hook.ogg')
kill = mixer.Sound('firstblood.ogg')
enemy_speed = randint(1,10)

hero = Player('hero.png', 435, 525, 7, 175, 175)
lose = font.render('You`re loser. Hehe!', True, (255, 215,0))
win = font.render('You`re winner. fuck!', True, (0, 215,0))
perezarzdka = font.render('Перезарядка 3 сек', True, (255,255,255))
monster1 = Enemy('enemy.png', randint(5, 895), 0, randint(1,3), 100,100)
monster2 = Enemy('enemy.png', randint(5, 895), 0, randint(1,3), 100,100)
monster3 = Enemy('enemy.png', randint(5, 895), 0, randint(1,3), 100,100)
monster4 = Enemy('enemy.png', randint(5, 895), 0, randint(1,3), 100,100)
monster5 = Enemy('enemy.png', randint(5, 895), 0, randint(1,3), 100,100)
crip1 = Enemy('crip.png', randint(5, 895), 0, randint(1,3), 100,100)
crip2 = Enemy('crip.png', randint(5, 895), 0, randint(1,3), 100,100)
crip3 = Enemy('crip.png', randint(5, 895), 0, randint(1,3), 100,100)
monsters = sprite.Group()
bullets = sprite.Group()
crips = sprite.Group()
monsters.add(monster1)
monsters.add(monster2)
monsters.add(monster3)
monsters.add(monster4)
monsters.add(monster5)
crips.add(crip1)
crips.add(crip2)
crips.add(crip3)
chet = 0
chettitif = font.render('Cчет:' + str(chet),True,(250,250,250))
start_time = 0

while game:
    for e in event.get():  # получить все события, происходящие в этот момент
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire < 5 and rel_time == False:
                    hero.fire()
                    num_fire += 1
                if num_fire >= 5 and rel_time == False:
                    rel_time = True
                    start_time = time_module.time()
                    num_fire = 0





    if finish != True:
        window.blit(background, (0, 0))
        hero.reset()
        monsters.draw(window)
        bullets.draw(window)
        crips.draw(window)
        if sprite.spritecollide(hero,monsters, False):
            finish = True
            window.blit(lose, (400, 300))
        if sprite.groupcollide(bullets, monsters, True, True):
            monster1 = Enemy('enemy.png', randint(5, 895), 0, randint(1, 4), 100, 100)
            monsters.add(monster1)
            kill.play()
            chet += 1
        hero.update()
        monsters.update()
        crips.update()
        propusk = font.render('Пропущено:' + str(lost), True, (250, 250, 250))
        chettitif = font.render('Cчет:' + str(chet), True, (250, 250, 250))
        window.blit(propusk, (10,50))
        window.blit(chettitif,(10,20))
        bullets.update()
    if lost >= 5:
        finish = True
        window.blit(lose,(400,300))
    if chet >= 10:
        finish = True
        window.blit(win, (400, 300))
    if sprite.spritecollide(hero, crips, False):
        finish = True
        window.blit(lose, (400, 300))

    end_time = time_module.time()
    if int(end_time - start_time) < 3:
        window.blit(perezarzdka, (350, 650))
    else:
        rel_time = False





    display.update()
    clock.tick(60)
