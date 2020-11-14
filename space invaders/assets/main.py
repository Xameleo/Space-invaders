import pygame
import os
import time
import random


WIDTH, HEIGHT = 770, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter Tutorial")

#load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))

#Player img
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_ship_red.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_ship_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_ship_blue.png"))

#Background

BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")),  (WIDTH, HEIGHT) )


def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0,0))
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window();
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False