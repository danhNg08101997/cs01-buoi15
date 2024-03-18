import pygame
class Bullet:
    def __init__(self) -> None:
        self.image = pygame.image.load('./galaxy war/graphics/laser.png')
        self.position = self.image.get_rect()
        self.speed = 20
        
    def draw(self, screen):
        screen.blit(self.image, self.position)
        
    def move(self):
        self.position.y -= self.speed