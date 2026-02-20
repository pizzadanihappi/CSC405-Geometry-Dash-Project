import sys
import pygame
import pygame.locals

from cube import Cube

def player():
    

def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))

    pygame.draw.rect(self.surface, "#FFDD40", (self.x, self.y, self.size, self.size))

    state = "start"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.locals.KEYDOWN:
                if event.key == pygame.K_SPACE: #make text display "press space to continue"
                    if state == "start":
                        state = "game"
                    elif state == "game":

                        
    if state == "game":
        screen.fill("#58A1F0")
    if state == "death":
        screen.fill("#e00c0c")  