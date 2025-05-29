# You need to install pygame to run this code

import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snakey snake game')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 25)

def draw_text(text, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (0, -1)

    def head_position(self):
        return self.positions[0]

    def turn(self, dir):
        opposite = (-self.direction[0], -self.direction[1])
        if dir != opposite:
            self.direction = dir

    def move(self):
        head_x, head_y = self.head_position()
        dx, dy = self.direction
        new_pos = ((head_x + dx) % GRID_WIDTH, (head_y + dy) % GRID_HEIGHT)

        if new_pos in self.positions[1:]:
            return False

        self.positions.insert(0, new_pos)
        self.positions.pop()
        return True

    def grow(self):
        tail = self.positions[-1]
        self.positions.append(tail)

    def draw(self, surface):
        for pos in self.positions:
            rect = pygame.Rect(pos[0]*CELL_SIZE, pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, GREEN, rect)

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def draw(self, surface):
        rect = pygame.Rect(self.position[0]*CELL_SIZE, self.position[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, RED, rect)

def main():
    snake = Snake()
    food = Food()
    score = 0

    running = True
    while running:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.turn((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.turn((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.turn((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.turn((1, 0))

        if not snake.move():
            running = False

        if snake.head_position() == food.position:
            snake.grow()
            score += 1
            food.randomize_position()

        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)
        draw_text(f"Score: {score}", WHITE, 10, 10)
        pygame.display.flip()

    screen.fill(BLACK)
    draw_text("Game Over!", RED, WIDTH//2 - 70, HEIGHT//2 - 20)
    draw_text(f"Final Score: {score}", WHITE, WIDTH//2 - 80, HEIGHT//2 + 20)
    pygame.display.flip()
    pygame.time.wait(3000)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
