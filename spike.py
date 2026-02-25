import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


class Spike:
    def __init__(self, x, y, width=40, height=40, speed=5):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = speed

    def update(self):

        self.x -= self.speed

        if self.x < -self.width:
            self.x = WIDTH

    def draw(self, surface):
        pygame.draw.polygon(surface, (255, 0, 0), [
            (self.x, self.y),
            (self.x + self.width // 2, self.y - self.height),
            (self.x + self.width, self.y)
        ])



spike = Spike(WIDTH, HEIGHT - 100)

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    spike.update()

    screen.fill((30, 30, 30))
    spike.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()