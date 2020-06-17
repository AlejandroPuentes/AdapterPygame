import pygame

class Bomberman():
     
    def __init__(self):
        self.posx=0
        self.imagenes=[]
        self.imageAc=None
        self.contador =0     

    def Set_imagenes(self,imagenes):
        self.imagenes=imagenes

    def Get_imagenes(self):
        return self.imagenes        

    def Move_Right(self):
        if self.contador==0:
            self.posx=self.posx+5
            self.Set_ImageAc(self.Get_imagenes()[0][self.contador])
            self.contador=1
        elif self.contador==1:
            self.posx=self.posx+5 
            self.Set_ImageAc(self.Get_imagenes()[0][self.contador])
            self.contador=2
        elif self.contador==2:
            self.posx=self.posx+5 
            self.Set_ImageAc(self.Get_imagenes()[0][self.contador])
            self.contador=3
        elif self.contador==3:
            self.posx=self.posx+5 
            self.Set_ImageAc(self.Get_imagenes()[0][self.contador])
            self.contador=4
        elif self.contador==4:
            self.posx=self.posx+5 
            self.Set_ImageAc(self.Get_imagenes()[0][self.contador])
            self.contador=0        

    def Move_Left(self):
        if self.contador==0:
            self.posx=self.posx-5
            self.Set_ImageAc(self.Get_imagenes()[1][self.contador])
            self.contador=1
        elif self.contador==1:
            self.posx=self.posx-5 
            self.Set_ImageAc(self.Get_imagenes()[1][self.contador])
            self.contador=2
        elif self.contador==2:
            self.posx=self.posx-5 
            self.Set_ImageAc(self.Get_imagenes()[1][self.contador])
            self.contador=3
        elif self.contador==3:
            self.posx=self.posx-5 
            self.Set_ImageAc(self.Get_imagenes()[1][self.contador])
            self.contador=4
        elif self.contador==4:
            self.posx=self.posx-5 
            self.Set_ImageAc(self.Get_imagenes()[1][self.contador])
            self.contador=0    

    def Get_ImageAc(self):
        return self.imageAc

    def Set_ImageAc(self,imagen):
        self.imageAc=imagen
    
    def Get_posx(self):
        return self.posx

class ConstructorPersonaje():
    def __init__(self,fabrica):
        self.fabrica=fabrica

    def Get_sprites(self):
        return[self.fabrica.Mover_derecha(),
               self.fabrica.Mover_izqui()]

class FabricaAbstacta():
    def Mover_derecha(self):
        pass

    def Mover_izqui(self):
        pass

class FabricaBomberman(FabricaAbstacta):    
    def Mover_derecha(self):
        Spritesderecha =SpriteDerechaBo()
        return Spritesderecha.Sprites_ri()
   
    def Mover_izqui(self):
        SpritesIz= SpritesIzquiBo()
        return SpritesIz.Sprites_le()

class AbstractRight():
    def Sprites_ri(self):
        pass

class AbstractLeft():
    def Sprites_le(self):
        pass

class SpriteDerechaBo(AbstractRight):
    def Sprites_ri(self):
        return[pygame.image.load('Imagenes/31.gif'),
               pygame.image.load('Imagenes/32.gif'),
               pygame.image.load('Imagenes/33.gif'),
               pygame.image.load('Imagenes/34.gif'),
               pygame.image.load('Imagenes/35.gif')]    

class SpritesIzquiBo(AbstractLeft):
    def Sprites_le(self):
        return[pygame.image.load('Imagenes/21.gif'),
               pygame.image.load('Imagenes/22.gif'),
               pygame.image.load('Imagenes/23.gif'),
               pygame.image.load('Imagenes/24.gif'),
               pygame.image.load('Imagenes/25.gif')]