import pygame
from pygame.locals import*
import sys
import platforms
import random
from platforms import Platforms
pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)
clock = pygame.time.clock()
color = (255,255,179)
sprite_list = pygame.sprite.Group()
platforms = pygame.sprite.Group()

def init():
    for i in range(height // 100):
        for j in range(width // 420):
            plat = platforms((random.randint(5,0 (width-50) // 10) * 10, 120 * i), 'image/grassHalf.png', 70, 40)
            platforms.add(plat)

def main():
    game_over = False
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_f:
                    pygame.display.set_mode(size, FULLSCREEN)
                if event.key == K_ESCAPE:
                    pygame.display.set_mode(size)
        screen.fill(color)
        platforms.draw(screen)
        sprite_list.draw(screen)
        pygame.display.flip()


if __name__ = '__main__':
    main()