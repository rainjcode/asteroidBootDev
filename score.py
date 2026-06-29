import pygame
from constants import ASTEROID_POINT_VALUE
from constants import SCREEN_WIDTH

class Score():
    def __init__(self, font, size):
        self.font = font
        self.size = size
        self.points = 0
        self.text = pygame.font.SysFont(self.font, self.size)

    def draw(self, screen):
        score_text = self.text.render(f'{self.points}', False, 'white', None)
        screen.blit(score_text, (SCREEN_WIDTH / 2, 0))

    def add_score(self):
        self.points += ASTEROID_POINT_VALUE

    def get_score(self):
        return self.points