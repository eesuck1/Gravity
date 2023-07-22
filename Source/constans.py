import numpy
import pygame.font
pygame.init()

SIZE = numpy.array([1480, 800])
FPS = 240
FONT = pygame.font.SysFont("Montserrat", 24)
ANY_KEY = FONT.render("Press Any Key", True, (255, 255, 255))
