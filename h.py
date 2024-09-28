import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set title
pygame.display.set_caption("Bird Animation")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)

# Bird class
class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 30
        self.color = (255, 255, 0) # Yellow
        self.velocity = 0
        self.gravity = 0.5
        self.jump_height = 10

    def draw(self):
        pygame.draw.ellipse(screen, self.color, (self.x, self.y, self.width, self.height))

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

        # Check for collisions with the ground
        if self.y + self.height >= screen_height:
            self.y = screen_height - self.height
            self.velocity = 0

    def jump(self):
        self.velocity = -self.jump_height

# Create a bird object
bird = Bird(screen_width // 2, screen_height // 2)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()

    # Update the bird
    bird.update()

    # Clear the screen
    screen.fill(blue)

    # Draw the bird
    bird.draw()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
