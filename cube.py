import pygame


class Cube:
    def __init__(self, surface: pygame.Surface, x: float, y: float, size: float, ground: float) -> None:
        self.surface = surface
        self.x, self.y = x, y
        self.size = size
        self.ground = ground
        self.color = "#FFDD40"
        self.alive = True

        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.rect(self.image, self.color, (0, 0, self.size, self.size))
        self.mask = pygame.mask.from_surface(self.image)

        self.vy = 0
        self.g = 0.3
        self.jump_vel = -8

        self.scale_x = 1
        self.scale_y = 1
        self.jiggle_speed = 0.15

        if self.y + self.size >= self.ground:
            self.y = self.ground - self.size
            self.on_ground = True
        else:
            self.on_ground = False

    def jump(self, on_surface=False) -> None:
        if self.alive and (self.on_ground or on_surface):
            self.vy = self.jump_vel
            self.on_ground = False

            self.scale_x = 0.8
            self.scale_y = 1.2

    def update(self) -> None:
        if not self.alive:
            return

        previous_vy = self.vy

        self.vy += self.g
        self.y += self.vy

        if self.y + self.size >= self.ground:
            if previous_vy > 1:
                self.scale_x = 1.3
                self.scale_y = 0.7

            self.y = self.ground - self.size
            self.vy = 0
            self.on_ground = True

        self.scale_x += (1 - self.scale_x) * self.jiggle_speed
        self.scale_y += (1 - self.scale_y) * self.jiggle_speed

    def hitbox(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def dead(self) -> None:
        self.color = "#3C3E32"

    def display(self) -> None:
        width = int(self.size * self.scale_x)
        height = int(self.size * self.scale_y)

        draw_x = self.x + (self.size - width) / 2
        draw_y = self.y + (self.size - height) / 2

        pygame.draw.rect(self.surface, self.color, (draw_x, draw_y, width, height))