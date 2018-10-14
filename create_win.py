
import pygame
from pygame.locals import *
import time

class Base(object):
    def __init__(self, screen_temp, x, y, image_name):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_name)
        self.screen = screen_temp

class BasePlane(Base):
    def __init__(self, screen_temp, x, y, image_name):
        super().__init__(screen_temp, x, y, image_name)
        self.bullet_list = []
    def display(self):
        self.screen.blit(self.image, (self.x,self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)

class HeroPlane(BasePlane):
    def __init__(self, screen_temp):
        super().__init__(screen_temp, 200, 700, './resouce/hero1.png')

    def move_left(self):
        self.x -= 5
    def move_right(self):
        self.x += 5
    def fire(self):
        self.bullet_list.append(Bullet(self.screen,(self.x,self.y)))


class EnemyPlane(BasePlane):
    def __init__(self, screen_temp):
        super().__init__(screen_temp, 200, 0, './resouce/enemy0.png')
        self.direction = 'right'
    def move(self):
        # self.y += 2

        if self.direction == 'right' :
            self.x += 2
        else :
            self.x -= 2
        
        if self.x > 430:
            self.direction = 'left'
        elif self.x < 0:
            self.direction = 'right'

    def fire(self):
        self.bullet_list.append(EnemyBullet(self.screen,(self.x,self.y)))
        

class BaseBullet(Base):
    def __init__(self, screen_temp, x, y, image_name):
        super().__init__(screen_temp, x, y, image_name)
    def display(self):
        self.screen.blit(self.image, (self.x,self.y))

class Bullet(BaseBullet):
    def __init__(self, screen_temp,xy):
        super().__init__(screen_temp, xy[0] + 40, xy[1] - 20, './resouce/bullet.png')
    def move(self):
        self.y -= 5
    def judge(self):
        return self.y > 852

class EnemyBullet(BaseBullet):
    def __init__(self, screen_temp,xy):
        super().__init__(screen_temp, xy[0] + 25, xy[1] + 40, './resouce/bullet1.png')
    def display(self):
        self.screen.blit(self.image, (self.x,self.y))
    def move(self):
        self.y += 5
    def judge(self):
        return self.y < 0



def key_control(plane):
    for event in pygame.event.get():
        #判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        #判断是否是按下了键
        elif event.type == KEYDOWN:
            #检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                plane.x -= 5

            #检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                plane.x += 5

            #检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                plane.fire()

def main():
    screen = pygame.display.set_mode((480,852),0,32)
    background = pygame.image.load('./resouce/background.png')
    hero = HeroPlane(screen)
    enemy = EnemyPlane(screen)
    while True: 
        screen.blit(background, (0,0))
        hero.display()
        enemy.display()
        enemy.move()
        enemy.fire()
        #获取事件，比如按键等
        key_control(hero)
        pygame.display.update()
        time.sleep(0.01)
# main()
if __name__ == "__main__":
    main()