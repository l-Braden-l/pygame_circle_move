import pygame
import sys
import config  # Ensure you have this config file with required constants

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events(x1, y1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, x1, y1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1 = -3
            elif event.key == pygame.K_RIGHT:
                x1 = 3
            elif event.key == pygame.K_UP:
                y1 = -3
            elif event.key == pygame.K_DOWN:
                y1 = 3

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x1 = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y1 = 0
    return True, x1, y1

def draw_circle(screen, color, center, radius, thickness):
    pygame.draw.circle(screen, color, center, radius, thickness)

def main():
    screen = init_game()
    clock = pygame.time.Clock()
    
    running = True
    x1, y1 = 0, 0
    x_cord, y_cord = config.WINDOW_WIDTH // 2, config.WINDOW_HEIGHT // 2

    while running:
        running, x1, y1 = handle_events(x1, y1)  # Pass x1, y1 to handle_events, and get them back
        x_cord += x1
        y_cord += y1

        screen.fill(config.WHITE)

        # Circle variables
        circle_center = (x_cord, y_cord)
        circle_radius = 80
        circle_color = config.BLUE
        circle_thick = 0

        draw_circle(screen, circle_color, circle_center, circle_radius, circle_thick)

        pygame.display.flip()

        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

    main()
