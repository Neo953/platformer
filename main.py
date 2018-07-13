import pygame
from pygame.locals import*
import sys
import platforms
import random
from platforms import Platforms
from player import Player




pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (255,255,179)
sprite_list = pygame.sprite.Group()
platforms = pygame.sprite.Group()
player = ''


def get_player_actions():
    p1_actions = {}
    p1_actions["p1_jump"] = pygame.image.load("image/p1_jump.png").convert()
    p1_actions["p1_jump"].set_colorkey((0,0,0))
    p1_actions["p1_hurt"] = pygame.image.load("image/p1_hurt.png").convert()
    p1_actions["p1_hurt"].set_colorkey((0,0,0))
    return p1_actions

def init(p1_actions):
    global player
    for i in range(height // 100):
        for j in range(width // 420):
            plat = Platforms((random.randint(5, (width-50) // 10) * 10, 120 * i), 'image/grassHalf.png', 70, 40)
            platforms.add(plat)
    player = Player((platforms.sprites()[-1].rect.centerx, platforms.sprites()[-1].rect.centery-300), p1_actions)
    sprite_list.add(player)
def main():
    global player, text, text_rect
    game_over = False
    p1_actions = get_player_actions()
    init(p1_actions)
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
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.left()
        if keys[pygame.K_RIGHT]:
            player.right()
        screen.fill(color)
        platforms.draw(screen)
        sprite_list.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()