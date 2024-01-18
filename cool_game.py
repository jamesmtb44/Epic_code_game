import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)

scorecounter = 0
score = 0
 
# Player variables
player_x = WIDTH // 2
player_y = HEIGHT - 120 #50
player_speed = 4 #5

# Obstacle variables
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5
obstacle_frequency = 25
obstacles = []

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hill Climb Racing")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Function to draw the player
def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, [x, y, 30, 70])


# Function to draw obstacles
def draw_obstacles(obstacles):
    for obstacle in obstacles:
        pygame.draw.rect(screen, "red" , obstacle)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #score
    scorecounter += 1  

    if scorecounter == 60:
        score +=1 
        scorecounter = 0    


    # Move the player with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 30:
        player_x += player_speed

    # Generate obstacles
    if random.randint(0, obstacle_frequency) == 0:
        obstacle_x = random.randint(0, WIDTH - obstacle_width)
        obstacle_y = -obstacle_height
        obstacles.append(pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    # Move obstacles
    for obstacle in obstacles:
        obstacle.y += obstacle_speed
        if obstacle.y > HEIGHT:
            obstacles.remove(obstacle)

    # Check for collisions with obstacles
    player_rect = pygame.Rect(player_x, player_y, 30, 50)
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            print("Game Over!")
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the player and obstacles
    draw_player(player_x, player_y)
    draw_obstacles(obstacles)
    wordfont=pygame.font.Font(None,50)#font type, font size
    text=wordfont.render(str(score),True,'Green')
    screen.blit(text, (670,20))
    # Update the display
    
    pygame.display.flip()
    

    # Set the frame rate
    clock.tick(FPS)
    #print(str(score))