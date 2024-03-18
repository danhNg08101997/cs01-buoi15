import pygame

class Meteor:
    def __init__(self) -> None:
        self.image = pygame.image.load('galaxy war/graphics/meteor.png')
        self.position = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, self.position)