import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
FPS = 60
GRAVITY = 0.25
BIRD_JUMP = -5
PIPE_WIDTH = 50
PIPE_HEIGHT = 300
PIPE_GAP = 100

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class FlappyBird:
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.fps = FPS

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Flappy Bird")

        self.clock = pygame.time.Clock()

        self.bird = Bird()
        self.pipes = []

    def generate_pipe(self):
        pipe_height = random.randint(50, HEIGHT - PIPE_GAP - 50)
        pipe = Pipe(self.width, pipe_height, PIPE_WIDTH, PIPE_HEIGHT, PIPE_GAP)
        self.pipes.append(pipe)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.jump()

    def run(self):
        while True:
            self.handle_input()

            # Update
            self.bird.update()

            for pipe in self.pipes:
                pipe.update()
                if self.bird.collides(pipe):
                    self.game_over()

            # Generate pipes
            if len(self.pipes) == 0 or self.pipes[-1].x < self.width - 200:
                self.generate_pipe()

            # Remove off-screen pipes
            self.pipes = [pipe for pipe in self.pipes if pipe.x + pipe.width > 0]

            # Draw
            self.screen.fill(WHITE)
            self.bird.draw(self.screen)
            for pipe in self.pipes:
                pipe.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(self.fps)

    def game_over(self):
        pygame.quit()
        sys.exit()

class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.radius = 20
        self.velocity = 0

    def jump(self):
        self.velocity = BIRD_JUMP

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

        # Prevent bird from going off-screen
        if self.y < 0:
            self.y = 0
            self.velocity = 0
        elif self.y > HEIGHT:
            self.y = HEIGHT
            self.velocity = 0

    def draw(self, screen):
        pygame.draw.circle(screen, BLUE, (self.x, int(self.y)), self.radius)

    def collides(self, pipe):
        return (
            self.x + self.radius > pipe.x
            and self.x - self.radius < pipe.x + pipe.width
            and (self.y + self.radius > pipe.y + pipe.gap or self.y - self.radius < pipe.y)
        )

class Pipe:
    def __init__(self, x, gap_start, width, height, gap):
        self.x = x
        self.y = gap_start - height
        self.width = width
        self.height = height
        self.gap = gap

    def update(self):
        self.x -= 5

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, GREEN, (self.x, self.y + self.height + self.gap, self.width, HEIGHT - self.y - self.height - self.gap))

if __name__ == "__main__":
    FlappyBird().run()
