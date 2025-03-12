import pygame
import random

# Initialize Pygame
pygame.init()

# Game screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Player settings
player_width = 80
player_height = 20
player_x = (SCREEN_WIDTH - player_width) // 2
player_y = SCREEN_HEIGHT - player_height - 10
player_speed = 10

# Falling object settings
falling_object_width = 20
falling_object_height = 20
falling_object_speed = 5
falling_objects = []

# Score and font
score = 0
missed_objects = 0
font = pygame.font.SysFont(None, 36)
large_font = pygame.font.SysFont(None, 72)

# Game clock
clock = pygame.time.Clock()

def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, player_width, player_height))

def draw_falling_objects(objects):
    for obj in objects:
        pygame.draw.rect(screen, RED, obj)

def draw_score(score):
    score_text = font.render(f"Score: {score}", True, GREEN)
    screen.blit(score_text, (10, 10))

def draw_missed(missed):
    missed_text = font.render(f"Missed: {missed}", True, RED)
    screen.blit(missed_text, (SCREEN_WIDTH - 150, 10))

def draw_game_over():
    game_over_text = large_font.render("GAME OVER!", True, BLACK)
    screen.blit(game_over_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 3))

def main():
    global player_x, score, falling_objects, missed_objects, falling_object_speed

    # Game loop
    running = True
    while running:
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Key press handling
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
            player_x += player_speed
        
        # Create new falling object
        if random.randint(1, 60) == 1:  # Random chance to create a new object
            new_object = pygame.Rect(random.randint(0, SCREEN_WIDTH - falling_object_width), 0, falling_object_width, falling_object_height)
            falling_objects.append(new_object)
        
        # Move falling objects
        for obj in falling_objects:
            obj.y += falling_object_speed
            # Check for collision with player
            if obj.colliderect(pygame.Rect(player_x, player_y, player_width, player_height)):
                falling_objects.remove(obj)
                score += 1  # Increase score when the player catches an object
            # Check if object missed
            elif obj.y > SCREEN_HEIGHT:
                falling_objects.remove(obj)
                missed_objects += 1

        # Increase difficulty as the score goes up
        if score % 10 == 0 and score != 0:  # Every 10 points, increase speed
            falling_object_speed += 1
            score += 1  # Prevent infinite speed increase on exact multiples of 10
        
        # Check for game over
        if missed_objects >= 5:
            draw_game_over()
            pygame.display.update()
            pygame.time.wait(2000)  # Wait for 2 seconds before quitting
            running = False  # End the game
        
        # Drawing
        draw_player(player_x, player_y)
        draw_falling_objects(falling_objects)
        draw_score(score)
        draw_missed(missed_objects)

        # Update the display
        pygame.display.update()

        # Set FPS
        clock.tick(60)
    
    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
s
