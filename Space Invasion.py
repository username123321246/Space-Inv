import pygame
import os
pygame.font.init()
pygame.mixer.init()


WIDTH = 900
HEIGHT = 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invasion")

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

BORDER = pygame.Rect(WIDTH//2, 0, 10, HEIGHT)
BULLET_HIT_SOUND = pygame.mixer.Sound("Assets/Grenade+1.mp3")
BULLET_FIRE_SOUND = pygame.mixer.Sound("Assets/Gun+Silencer.mp3")

HEALTH_FONT = pygame.font.SysFont("Eras Bold ITC", 30)
WIN_FONT = pygame.font.SysFont("Rockwell Extra Bold", 60)

VEL = 5
BULLET = 7
FPS = 50
MAX_BULLETS = 3
S_W = 50
S_H = 40

YELLOW_SPACESHIP = pygame.image.load(os.path.join("Assets","Yellow.png"))
RED_SPACESHIP = pygame.image.load(os.path.join("Assets","Red.png"))

print(os.path.join("Assets","Yellow.png"))














