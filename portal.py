import pygame

class Portal:
    def __init__(self, surface: pygame.Surface, x, y, mode, width = 30, height = 120, speed = 5):
        self.surface = surface
        self.rect = pygame.Rect(x, y - height, width, height)
        self.speed = speed
        self.mode = mode
        self.colors = {"cube": "#FFDD40", "ufo": "#AE2BFF", "ship": "#00DA74"}
        self.color = self.colors.get(mode, "#FFFFFF")

    def update(self):
        self.rect.x -= self.speed

    def display(self):
        pygame.draw.rect(self.surface, self.color, self.rect)

    def hitbox(self):
        return self.rect