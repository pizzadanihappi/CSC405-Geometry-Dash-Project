import pygame

class Ship:
    def __init__(self, surface: pygame.Surface, x: float, y: float, size: float, ground: float) -> None:
        self.surface = surface
        self.x, self.y = x, y
        self.size = size
        self.vy = 0.5
        self.g = 0.5
        self.thrust = -0.8
        self.ground = ground
        self.color = "#00DA74"

        self.image = pygame.image.load("icons/ship.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.vy += self.thrust
        else:
            self.vy += self.g
        
        self.vy = max(-10, min(10, self.vy))
        self.y += self.vy

        if self.y < 0:
            self.y = 0
            self.vy = 0
        elif self.y + self.size > 600:
            self.y = 600 - self.size
            self.vy = 0
        if self.y + self.size >= self.ground:
            self.y = self.ground - self.size
            self.vy = 0

    def display(self):
        self.surface.blit(self.image, (self.x, self.y))

    def hitbox(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def dead(self):
        self.colour = "#3C3E32"