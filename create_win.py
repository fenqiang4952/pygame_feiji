
import pygame
import time

def main():
    screen = pygame.display.set_mode((480,852),0,32)
    background = pygame.image.load('./resouce/background.png')
    hero = pygame.image.load('./resouce/hero1.png')
    while True: 
        screen.blit(background, (0,0))
        screen.blit(hero, (230,700))
        pygame.display.update()
        time.sleep(1)
main()
# if __name__ == "__main__":
#     main()