import pygame

class Text:
    def __init__(self, style, size, color, content):
        self.style = style
        self.size = size
        self.color = color
        self.content = content
        self.display = pygame.font.Font(style,size)
        self.rendered = self.display.render(content,True,color)
class TextAndNumber(Text):
    def __init__(self,style,size,color,content):
        Text.__init__(self,style,size,color,content)
        self.value = 0
        self.rendered = self.display.render(content + str(self.value),True,color)
        
    def get_value(self):
        return self.value
    def set_value(self,newValue):
        self.value = newValue
        self.rendered = self.display.render(self.content + str(self.value),True,self.color)
        
    
    