import pygame, sys, random, copy, os.path
from models.Player import Player
from models.Bullet import Bullet
from models.Meteor import Meteor

pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Galaxy__oop')

clock = pygame.time.Clock()

# Khai báo player
player = Player()
# set position cho player
player.position.x = WIDTH/2 - 50
player.position.y = HEIGHT/2 + 200
# check file đã lưu có tồn tại không rồi mới load game
path = './save_file.json'
check_file = os.path.isfile(path)
check_access = os.access(path, os.R_OK)
if check_file and check_access:
    player.load_game()
# Khai báo đạn
# bullet = Bullet()
# # Khai báo thiên thạch
# meteor = Meteor()
# Tạo ra lst_meteor
lst_meteor: list[Meteor] = []
meteor_time_start =  0
meteor_time_span = 1000
# Tạo background
bg_game = pygame.image.load('./galaxy war/graphics/background_space.jpg')
bg_game = pygame.transform.scale(bg_game, (WIDTH, HEIGHT))

running = True
while running:
    # Background
    # screen.fill((255,255,255))
    screen.blit(bg_game,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player.save_game()
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player.attack()
                
    # setup thiên thạch rơi
    meteor_time_current = pygame.time.get_ticks()
    if meteor_time_current - meteor_time_start >= meteor_time_span:
        # Tạo ra meteor
        new_meteor = Meteor()
        new_meteor.position.y = 0
        new_meteor.position.x = random.randint(0, WIDTH - new_meteor.position.width)
        # cho rơi
        lst_meteor.append(new_meteor)
        meteor_time_start = meteor_time_current
    for meteor_instance in lst_meteor:
        meteor_instance.draw(screen)
        meteor_instance.move()
        # Thiên thạch va chạm đạn sẽ + điểm
        for bullet_instance in player.list_bullet:
            if bullet_instance.position.colliderect(meteor_instance.position):
                player.score += 100
                # Remove đạn và thiên thạch sau khi va chạm
                player.list_bullet.remove(bullet_instance)
                lst_meteor.remove(meteor_instance)
        # Xóa thiên thạch khỏi list để tối ưu
        if meteor_instance.position.y + meteor_instance.position.width > HEIGHT:
            lst_meteor.remove(meteor_instance)
            
    # Setup player di chuyển
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and player.position.y > 0:
        player.move('UP')
    elif key[pygame.K_s] and player.position.y < HEIGHT- player.avatar.get_height():
        player.move('DOWN')
    elif key[pygame.K_a] and player.position.x > 0:
        player.move('LEFT')
    elif key[pygame.K_d] and player.position.x < WIDTH - player.avatar.get_width():
        player.move('RIGHT')
        
    # Vẽ máy bay lên màn hình
    player.draw(screen)
    # Vẽ viên đạn lên màn hình
    # bullet.draw(screen)
    # # Vẽ thiên thạch lên màn hình
    # meteor.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
sys.exit()