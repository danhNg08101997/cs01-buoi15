import pygame
class Player:
    def __init__(self) -> None:
        self.avatar = pygame.image.load('./galaxy war/graphics/air_craft.png')
        self.score = 0
        self.position = self.avatar.get_rect()
        self.speed = 1
        self.list_bullet = []
    def draw(self, screen):
        screen.blit(self.avatar, self.position)
        # Xử lý load điểm
        f_game = pygame.font.Font('./galaxy war/graphics/subatomic.ttf',32)
        score_title = f_game.render(f'Score: {self.score}', True, 'Red')
        screen.blit(score_title, (0,0))
    def move(self, direction):
        if direction == 'UP':
            self.position.y -= self.speed
        elif direction == 'DOWN':
            self.position.y += self.speed
        elif direction == 'LEFT':
            self.position.x -= self.speed
        elif direction == 'RIGHT':
            self.position.x += self.speed