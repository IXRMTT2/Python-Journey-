# You need to install pygame to run this code

import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 20
BALL_SPEED_X, BALL_SPEED_Y = 7, 7
PADDLE_SPEED = 7
AI_SPEED = 6

font = pygame.font.SysFont('Arial', 30)

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = 0

    def move(self):
        self.rect.y += self.speed
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

    def move_ai(self, ball):
        if self.rect.centery < ball.rect.centery:
            self.rect.y += AI_SPEED
        elif self.rect.centery > ball.rect.centery:
            self.rect.y -= AI_SPEED
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1

    def draw(self):
        pygame.draw.ellipse(screen, WHITE, self.rect)

    def reset(self):
        self.rect.center = (WIDTH//2, HEIGHT//2)
        self.speed_x *= -1
        self.speed_y *= 1

def main():
    clock = pygame.time.Clock()

    left_paddle = Paddle(20, HEIGHT//2 - PADDLE_HEIGHT//2)
    right_paddle = Paddle(WIDTH - 30, HEIGHT//2 - PADDLE_HEIGHT//2)

    ball = Ball()

    left_score = 0
    right_score = 0

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    left_paddle.speed = -PADDLE_SPEED
                elif event.key == pygame.K_s:
                    left_paddle.speed = PADDLE_SPEED

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    left_paddle.speed = 0

        left_paddle.move()
        right_paddle.move_ai(ball)
        ball.move()

        if ball.rect.colliderect(left_paddle.rect) and ball.speed_x < 0:
            ball.speed_x *= -1
        if ball.rect.colliderect(right_paddle.rect) and ball.speed_x > 0:
            ball.speed_x *= -1

        if ball.rect.left <= 0:
            right_score += 1
            ball.reset()
        elif ball.rect.right >= WIDTH:
            left_score += 1
            ball.reset()

        screen.fill(BLACK)

        left_paddle.draw()
        right_paddle.draw()
        ball.draw()

        left_text = font.render(f"{left_score}", True, WHITE)
        right_text = font.render(f"{right_score}", True, WHITE)
        screen.blit(left_text, (WIDTH//4, 20))
        screen.blit(right_text, (WIDTH*3//4, 20))

        pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
