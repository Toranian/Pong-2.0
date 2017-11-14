import time
import random
import pickle
import pygame
from settings import *

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
pygame.init()
clock = pygame.time.Clock()


# Display a message to the game_display variable
def message_to_screen(x, y, size, msg, colour):
    font = pygame.font.SysFont("arial", size)
    screen_text = font.render(msg, True, colour).get_rect()
    game_display.blit(screen_text, [x, y])


class Paddle:

    """The main paddle functions."""

    def __init__(self, paddle_x, paddle_y, paddle_size, speed):
        self.paddle_x = paddle_x
        self.paddle_y = paddle_y
        self.paddle_size = paddle_size
        self.speed = speed
        self.direction_y = speed
        self.paddle = pygame.Rect(self.paddle_x, self.paddle_y, self.paddle_size[0], self.paddle_size[1])

    def move(self, direction_y):

        if self.paddle_y + self.paddle_size[1] >= HEIGHT:
            self.paddle_y = HEIGHT - self.paddle_size[1]
        elif self.paddle_y < 0:
            self.paddle_y = 0

        self.paddle_y += self.direction_y
        pygame.draw.rect(game_display, WHITE, [self.paddle_x, self.paddle_y, self.paddle_size[0], self.paddle_size[1]])


class Ball:

    """The ball physics."""

    def __init__(self, speed):
        self.speed = speed
        self.ball_x_change = random.choice(-self.speed, self.speed)
        self.ball_y_change = random.choice(-self.speed, self.speed)
        self.ball_x = WIDTH / 2
        self.ball_y = HEIGHT / 2
        self.ball_size = 20
        self.ball = pygame.Rect(self.ball_x, self.ball_y, self.ball_size, self.ball_size)

    def move(self):

        if self.ball_x >= WIDTH:
            self.ball_x_change = -self.speed
        elif self.ball < 0:
            self.ball_x_change = self.speed
        if self.ball >= HEIGHT:
            self.ball_y_change = -self.speed
        elif self.ball < 0:
            self.ball_y_change = self.speed

speed = 4
ball = Ball()


def game_over():
    for i in range(7):
        random_colour = (random.randint(0, 255), random.randint(0, 255, ), random.randint(0, 255))
        ball = pygame.draw.rect(game_display, random_colour, [])
