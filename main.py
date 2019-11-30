import pygame
from pygame.locals import *
from models.car import Car
from utils import event_handler

GAME_WIDTH = 1280
GAME_HEIGHT = 720

def main():
    # Initialize Screen and Player Object
    pygame.init()
    screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    player = Car('left')
    pygame.display.set_caption(player.hidden_discord_tech)

    # Fill background
    bg = pygame.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((250, 250, 250))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render('Total Reward: ', 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = bg.get_rect().centerx
    bg.blit(text, textpos)

    # Initialize sprites
    player_sprite = pygame.sprite.RenderPlain(player)

    # Blit everything to the screen
    screen.blit(bg, (0, 0))
    pygame.display.flip()

    # Initialize clock
    clock = pygame.time.Clock()

    # Event loop
    while 1:
        # lock game to 60fps
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type != None:
                event_handler(event, player)

        screen.blit(bg, player.rect, player.rect)
        player_sprite.update()
        player_sprite.draw(screen)
        pygame.display.flip()



if __name__ == '__main__':
    main()