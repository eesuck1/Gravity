import pygame
import numpy

from constans import FPS, SIZE


class Ball:
    def __init__(self, coordinates: tuple[int, int] | pygame.math.Vector2, radius: int,
                 velocity: tuple[float, float] | pygame.math.Vector2, mass: float, color: tuple[int, int, int]):
        self.__radius__ = radius
        self.__mass__ = mass
        self.__rect__ = pygame.rect.Rect(*coordinates, 2 * radius, 2 * radius)
        self.__velocity__ = pygame.math.Vector2(velocity)
        self.__color__ = color

    def set_coordinates(self, vector: tuple[int, int] | numpy.ndarray | pygame.math.Vector2) -> None:
        self.__rect__.x = vector[0]
        self.__rect__.y = vector[1]

    def change_coordinates(self, vector: tuple[float, float] | numpy.ndarray | pygame.math.Vector2) -> None:
        self.__rect__.x += vector[0]
        self.__rect__.y += vector[1]

    def get_coordinates(self) -> pygame.math.Vector2:
        return pygame.math.Vector2(self.__rect__.x, self.__rect__.y)

    def update(self, other) -> None:
        distance = self.get_coordinates().distance_to(other.get_coordinates()) + 0.001
        momentum = (other.get_coordinates() - self.get_coordinates()) / distance

        self.__velocity__ += other.get_mass() * momentum / distance ** 2

        self.change_coordinates(self.__velocity__)

    def get_center(self) -> tuple[int, int]:
        return self.__rect__.center

    def get_radius(self) -> float:
        return self.__radius__

    def get_mass(self) -> float:
        return self.__mass__

    def handle_box(self) -> None:
        if not (0 < self.__rect__.x < SIZE[0] - self.__rect__.width):
            self.__velocity__[0] *= -0.75
        if not (0 < self.__rect__.y < SIZE[1] - self.__rect__.height):
            self.__velocity__[0] *= 0.99
            self.__velocity__[1] *= -0.75

    def get_color(self) -> tuple[int, int, int]:
        return self.__color__

    def get_velocity(self) -> pygame.math.Vector2:
        return self.__velocity__
