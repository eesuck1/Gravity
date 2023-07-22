import sys

import pygame

from Source.ball import Ball
from Source.constans import SIZE, FPS, ANY_KEY, FONT, BACKGROUND_COLOR, BALL_COLOR, STAR_COLOR, LINE_COLOR, TEXT_COLOR


class Engine:
    def __init__(self):
        self._screen_ = pygame.display.set_mode(SIZE)
        self._clock_ = pygame.time.Clock()

        self._balls_ = [
            Ball(SIZE // 2, 25, (0, 0), 5E3, STAR_COLOR),
        ]

    def add_ball(self, coordinates: pygame.math.Vector2, velocity: pygame.math.Vector2, radius: int = 5,
                 mass: float = 15, color: tuple[int, int, int] = BALL_COLOR):
        self._balls_.append(Ball(coordinates, radius, velocity, mass, color))

    def draw_balls(self) -> None:
        for index, ball in enumerate(self._balls_):
            pygame.draw.circle(self._screen_, ball.get_color(), ball.get_coordinates(), ball.get_radius())
            text = FONT.render(f"Ball {index} Velocity: {round(ball.get_velocity(), 4)}", True, TEXT_COLOR)

            self._screen_.blit(text, (25, 25 + text.get_height() * 2 * index))

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self._screen_.fill(BACKGROUND_COLOR)

            for first in self._balls_:
                for second in self._balls_:
                    if first is second:
                        continue

                    first.update(second)

            self.draw_balls()

            self._clock_.tick(FPS)
            pygame.display.update()


class Menu(Engine):
    def __init__(self):
        super().__init__()

        self._start_ = pygame.math.Vector2()
        self._end_ = pygame.math.Vector2()
        self._draw_line_ = False
        self._balls_drawing_ = []

    def menu(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    self.run()

                if event.type == pygame.MOUSEBUTTONDOWN and not event.type == pygame.MOUSEBUTTONUP:
                    self._start_.update(pygame.mouse.get_pos())
                    self._draw_line_ = True
                    self._balls_drawing_.append(self._start_)

                if event.type == pygame.MOUSEBUTTONUP:
                    self._end_.update(pygame.mouse.get_pos())
                    self._draw_line_ = False
                    self.add_ball(self._start_, (self._end_ - self._start_) / 50)

            self._screen_.fill((20, 12, 46))
            self.draw_balls()

            for ball_drawing in self._balls_drawing_:
                pygame.draw.circle(self._screen_, BALL_COLOR, ball_drawing, 5)

            if self._draw_line_:
                pygame.draw.line(self._screen_, LINE_COLOR, self._start_, pygame.mouse.get_pos(), 3)

            self._screen_.blit(ANY_KEY, ((SIZE[0] - ANY_KEY.get_width()) / 2, SIZE[1] - 2 * ANY_KEY.get_height()))

            self._clock_.tick(FPS)
            pygame.display.update()
