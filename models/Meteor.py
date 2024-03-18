import pygame

class Meteor:
    def __init__(self) -> None:
        self.image = pygame.image.load('galaxy war/graphics/meteor.png')
        self.position = self.image.get_rect()
        self.speed = 10
        
    def draw(self, screen):
        screen.blit(self.image, self.position)
        
    def move(self):
        self.position.y += self.speed