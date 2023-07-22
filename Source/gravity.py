import sys

import pygame

from Source.ball import Ball
from Source.constans import SIZE, FPS, ANY_KEY, FONT


class Engine:
    def __init__(self):
        self.__screen__ = pygame.display.set_mode(SIZE)
        self.__clock__ = pygame.time.Clock()

        self.__start__ = pygame.math.Vector2()
        self.__end__ = pygame.math.Vector2()
        self.__draw_line__ = False

        self.__balls__ = [
            Ball(SIZE // 2, 25, (0, 0), 5E3, (250, 237, 95)),
        ]
        self.balls_drawing = []

    def add_ball(self, coordinates: pygame.math.Vector2, velocity: pygame.math.Vector2, radius: int = 5,
                 mass: float = 15, color: tuple[int, int, int] = (175, 195, 227)):
        self.__balls__.append(Ball(coordinates, radius, velocity, mass, color))

    def draw_balls(self) -> None:
        for index, ball in enumerate(self.__balls__):
            pygame.draw.circle(self.__screen__, ball.get_color(), ball.get_coordinates(), ball.get_radius())
            text = FONT.render(f"Ball {index} Velocity: {round(ball.get_velocity(), 4)}", True, (255, 255, 255))

            self.__screen__.blit(text, (25, 25 + text.get_height() * 2 * index))

    def menu(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    self.run()

                if event.type == pygame.MOUSEBUTTONDOWN and not event.type == pygame.MOUSEBUTTONUP:
                    self.__start__.update(pygame.mouse.get_pos())
                    self.__draw_line__ = True
                    self.balls_drawing.append(self.__start__)

                if event.type == pygame.MOUSEBUTTONUP:
                    self.__end__.update(pygame.mouse.get_pos())
                    self.__draw_line__ = False
                    self.add_ball(self.__start__, (self.__end__ - self.__start__) / 50)

            self.__screen__.fill((20, 12, 46))
            self.draw_balls()

            for ball_drawing in self.balls_drawing:
                pygame.draw.circle(self.__screen__, (175, 195, 227), ball_drawing, 5)

            if self.__draw_line__:
                pygame.draw.line(self.__screen__, (255, 0, 0), self.__start__, pygame.mouse.get_pos(), 3)

            self.__screen__.blit(ANY_KEY, ((SIZE[0] - ANY_KEY.get_width()) / 2, SIZE[1] - 2 * ANY_KEY.get_height()))

            self.__clock__.tick(FPS)
            pygame.display.update()

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.__screen__.fill((20, 12, 46))

            for first in self.__balls__:
                for second in self.__balls__:
                    if first is second:
                        continue

                    first.update(second)

            self.draw_balls()

            self.__clock__.tick(FPS)
            pygame.display.update()
