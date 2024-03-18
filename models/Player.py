import pygame, json
from models.Bullet import Bullet

class Player:
    def __init__(self) -> None:
        self.avatar = pygame.image.load('./galaxy war/graphics/air_craft.png')
        self.score = 0
        self.position = self.avatar.get_rect()
        self.speed = 10
        self.list_bullet:list[Bullet] = []
        self.file_game = 'save_file.json'
        
    def draw(self, screen):
        screen.blit(self.avatar, self.position)
        # Xử lý load điểm
        f_game = pygame.font.Font('./galaxy war/graphics/subatomic.ttf',32)
        score_title = f_game.render(f'Score: {self.score}', True, 'Red')
        screen.blit(score_title, (0,0))
        # Vẽ đạn
        for bullet in self.list_bullet:
            bullet.draw(screen)
            bullet.move()
            # Xóa đạn khỏi list để tối ưu
            if bullet.position.y < 0:
                self.list_bullet.remove(bullet)
            
    def move(self, direction):
        if direction == 'UP':
            self.position.y -= self.speed
        elif direction == 'DOWN':
            self.position.y += self.speed
        elif direction == 'LEFT':
            self.position.x -= self.speed
        elif direction == 'RIGHT':
            self.position.x += self.speed
            
    def attack(self):
        # Tạo đạn và đưa đạn vào list đạn
        new_bullet = Bullet()
        # Gán tọa độ viên đạn thành tọa độ máy bay
        new_bullet.position.x = self.position.x + self.position.width / 2 - 5
        new_bullet.position.y = self.position.y
        self.list_bullet.append(new_bullet)
        
    def save_game(self):
        data ={"score":self.score}
        with open(self.file_game, 'w') as json_file:
            json.dump(data, json_file)
            
    def load_game(self):
        with open(self.file_game, 'r') as json_file:
            data = json.load(json_file)
            self.score = data["score"]