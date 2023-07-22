import numpy
import pygame.font
pygame.init()

SIZE = numpy.array([1480, 800])
FPS = 240

FONT = pygame.font.SysFont("Montserrat", 24)
ANY_KEY = FONT.render("Press Any Key", True, (255, 255, 255))

BACKGROUND_COLOR = (20, 12, 46)
STAR_COLOR = (250, 237, 95)
BALL_COLOR = (175, 195, 227)
TEXT_COLOR = (255, 255, 255)
LINE_COLOR = (255, 0, 0)