import sys, pygame
from Character import mainCharacter
from AdapterCharacter import AdapterCharacter

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
CENTER = (200, 200) 
BLACK = 0,0,0
DELAY = 80


character = mainCharacter()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
playing = True
character.place(CENTER)


while playing:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character.moveLeft()
    elif keys[pygame.K_RIGHT]:
        character.moveRight()
    screen.fill(BLACK)
    character.draw(screen)
    pygame.time.delay(DELAY)
    pygame.display.flip()
    