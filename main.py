import pygame
import sys

pygame.init()

# Set the display dimensions
screen_width = 500
screen_height = 350

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Movement with Keyboard Input")

# Load an image
image = pygame.image.load("bb.png")

# Initial position of the sprite
x_pos = 50
y_pos = 50

# Initial step values
step_x = 0
step_y = 0

# Movement speed
movement_speed = .075

# Define the red rectangle platform
platform = pygame.Rect(200, 250, 100, 20)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the state of the keys
    keys = pygame.key.get_pressed()

    # Check arrow key presses to move the sprite
    if keys[pygame.K_LEFT]:
        step_x = -movement_speed
    elif keys[pygame.K_RIGHT]:
        step_x = movement_speed
    else:
        step_x = 0

    if keys[pygame.K_UP]:
        step_y = -movement_speed
    elif keys[pygame.K_DOWN]:
        step_y = movement_speed
    else:
        step_y = 0

    # Update the position of the sprite
    x_pos += step_x
    y_pos += step_y

    # Check if the sprite is still on screen, if not, wrap around
    if x_pos > screen_width:
        x_pos = 0
    elif x_pos < 0:
        x_pos = screen_width

    if y_pos > screen_height:
        y_pos = 0
    elif y_pos < 0:
        y_pos = screen_height

    # Check for collision - the "-5" is to prevent premature collision
    if platform.colliderect(pygame.Rect(x_pos, y_pos, image.get_width()-5, image.get_height()-5)):
        # Collision occurred
        print("Collision!")

    # Clear the screen
    screen.fill((0, 0, 0))

    # Blit the image onto the screen at the updated position
    screen.blit(image, (x_pos, y_pos))
    platform = pygame.draw.rect(screen, (255,0,0), (200, 250, 100, 20))

    # Update the display
    pygame.display.flip()

pygame.quit()
sys.exit()
