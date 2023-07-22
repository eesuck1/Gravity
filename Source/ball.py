import pygame
import numpy


class Ball:
    def __init__(self, coordinates: tuple[int, int] | pygame.math.Vector2, radius: int,
                 velocity: tuple[float, float] | pygame.math.Vector2, mass: float, color: tuple[int, int, int]):
        self._radius_ = radius
        self._mass_ = mass
        self._rect_ = pygame.rect.Rect(*coordinates, 2 * radius, 2 * radius)
        self._velocity_ = pygame.math.Vector2(velocity)
        self._color_ = color

    def set_coordinates(self, vector: tuple[int, int] | numpy.ndarray | pygame.math.Vector2) -> None:
        self._rect_.x = vector[0]
        self._rect_.y = vector[1]

    def change_coordinates(self, vector: tuple[float, float] | numpy.ndarray | pygame.math.Vector2) -> None:
        self._rect_.x += vector[0]
        self._rect_.y += vector[1]

    def update(self, other) -> None:
        distance = self.get_coordinates().distance_to(other.get_coordinates()) + 0.001
        momentum = (other.get_coordinates() - self.get_coordinates()) / distance

        self._velocity_ += other.get_mass() * momentum / distance ** 2

        self.change_coordinates(self._velocity_)

    def get_coordinates(self) -> pygame.math.Vector2:
        return pygame.math.Vector2(self._rect_.x, self._rect_.y)

    def get_center(self) -> tuple[int, int]:
        return self._rect_.center

    def get_radius(self) -> float:
        return self._radius_

    def get_mass(self) -> float:
        return self._mass_

    def get_color(self) -> tuple[int, int, int]:
        return self._color_

    def get_velocity(self) -> pygame.math.Vector2:
        return self._velocity_
