#botao 

import pygame 

class button():
    def __init__(self,color,x,y,width,height,text):
        self.smallfont = pygame.font.SysFont('Corbel',30) 
        self.width=width
        self.height=height
        self.rect=pygame.Rect((x,y),(width,height))
        self.color= color 
        self.x=x
        self.y=y
        self.text = self.smallfont.render(text,True, '#00FF00')
        self.text_rect=self.text.get_rect(center=self.rect.center)
    def draw(self,display):
        pygame.draw.rect(display,'#FFFFFF',self.rect)
        display.blit(self.text,self.text_rect)
    def posicao(self,mouse):
        if mouse[0] > self.x and mouse[0] <self.x + self.width:
            if mouse[1] >self.y and mouse[1]< self.y +self.height:
                return True
        return False





            
                