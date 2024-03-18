import pygame, sys
from models.Player import Player
from models.Bullet import Bullet
from models.Meteor import Meteor

pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Galaxy__oop')

# Khai báo player
player = Player()
bullet = Bullet()
meteor = Meteor()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player.move('UP')
    elif key[pygame.K_s]:
        player.move('DOWN')
    elif key[pygame.K_a]:
        player.move('LEFT')
    elif key[pygame.K_d]:
        player.move('RIGHT')
        
    # Background
    screen.fill((255,255,255))
    # Vẽ máy bay lên màn hình
    player.draw(screen)
    # Vẽ viên đạn lên màn hình
    bullet.draw(screen)
    # Vẽ thiên thạch lên màn hình
    meteor.draw(screen)
    pygame.display.flip()
pygame.quit()
sys.exit()

# 01:22:37/02:42:00