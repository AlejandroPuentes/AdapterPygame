from Character import Character
from AdaptedCharacter import *

class AdapterCharacter(Character, Bomberman):
    
    def __init__(self):
        Bomberman.__init__(self)
        Character.__init__(self)
        constructor = ConstructorPersonaje(FabricaBomberman())
        self.Set_imagenes(constructor.Get_sprites())
        self.images = self.imagenes
        self.image = self.images[self.dir][self.current]
        self.rect = self.image.get_rect()

    def moveRight(self):
        self.Move_Right()
        self.update()

    def moveLeft(self):
        self.Move_Left()
        self.update()

    def update(self):
        self.setImage(self.Get_ImageAc())
        self.setRectLeft(self.Get_posx())

    def place(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.posx = pos[0]

    def setImages(self, sprites):
        self.images = sprites