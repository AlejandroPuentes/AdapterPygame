import pygame
from pygame import *
from Util import *









class Character(pygame.sprite.Sprite):

    def __init__(self):
        self.velocity = 10
        self.image = None
        self.dir = 0
        self.images = []
        self.current = 0

    def moveRight(self):
        pass

    def moveLeft(self):
        pass

    def update(self):
        self.image = self.images[self.dir][self.current]
        self.current += 1
        self.current %= len(self.images[self.dir])


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def place(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def setImages(self, sprites):
        pass

    def setImage(self, image):
        self.image = image

    def setRectLeft(self, pos):
        self.rect.left = pos














class mainCharacter(Character):

    sprites = [
                ['Static/R0.png', 'Static/R1.png', 'Static/R2.png', 'Static/R3.png',
                 'Static/R4.png', 'Static/R5.png'],

                ['Static/L0.png', 'Static/L1.png', 'Static/L2.png', 'Static/L3.png', 
                'Static/L4.png', 'Static/L5.png']
                                                                                    ]

    def __init__(self):
        Character.__init__(self)
        self.setImages(self.sprites)
        self.image = self.images[self.dir][self.current]
        self.rect = self.image.get_rect()



    def moveRight(self):
        self.rect.left += self.velocity
        self.dir = 0
        self.update()

    def moveLeft(self):
        self.rect.left -= self.velocity
        self.dir = 1
        self.update()

    def setImages(self, sprites):
        self.images = loadImages(sprites)
        
