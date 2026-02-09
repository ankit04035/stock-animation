import pygame
import sys
import time

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Task Animation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (52, 152, 219)
GREEN = (46, 204, 113)
GRAY = (200, 200, 200)

# Font
font = pygame.font.SysFont("arial", 28)
small_font = pygame.font.SysFont("arial", 22)

# Progress bar settings
bar_x = 100
bar_y = 150
bar_width = 400
bar_height = 30
progress = 0

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw title
    title = font.render("Task Animation", True, BLACK)
    screen.blit(title, (200, 40))

    # Task text
    if progress < 100:
        task_text = small_font.render("Task Running...", True, BLACK)
    else:
        task_text = small_font.render("Task Completed ", True, GREEN)

    screen.blit(task_text, (220, 90))

    # Draw progress bar background
    pygame.draw.rect(screen, GRAY, (bar_x, bar_y, bar_width, bar_height))

    # Draw progress bar fill
    pygame.draw.rect(
        screen,
        BLUE,
        (bar_x, bar_y, bar_width * (progress / 100), bar_height)
    )

    # Percentage text
    percent_text = small_font.render(f"{progress}%", True, BLACK)
    screen.blit(percent_text, (270, 190))

    # Increase progress
    if progress < 100:
        progress += 1
        time.sleep(0.03)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()

