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
movement_speed = 0.05

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
    new_x = x_pos + step_x
    new_y = y_pos + step_y

    # Check if the sprite is still on screen, if not, wrap around
    if new_x > screen_width:
        new_x = 0
    elif new_x < 0:
        new_x = screen_width

    if new_y > screen_height:
        new_y = 0
    elif new_y < 0:
        new_y = screen_height

    # Create a new rect for the updated sprite position
    sprite_rect = pygame.Rect(new_x, new_y, image.get_width() - 10, image.get_height() - 15)

    # Check for collision along the y-axis
    if sprite_rect.colliderect(platform):
        # Collision occurred
        # Check if the sprite is coming from above the platform
        if step_y > 0 and sprite_rect.top < platform.top:
            # Adjust the y position to sit on the platform
            new_y = platform.top - image.get_height()
        elif step_y < 0 and sprite_rect.bottom > platform.bottom:
            # Adjust the y position to sit below the platform
            new_y = platform.bottom

    # Check for collision along the x-axis (horizontal)
    if sprite_rect.colliderect(platform):
        # Collision occurred along the x-axis
        # Adjust the x position to prevent passing through the platform
        if step_x > 0:
            new_x = platform.left - image.get_width()
        elif step_x < 0:
            new_x = platform.right

    # Update the position of the sprite
    x_pos = new_x
    y_pos = new_y

    # Clear the screen
    screen.fill((0, 0, 0))

    # Blit the image onto the screen at the updated position
    screen.blit(image, (x_pos, y_pos))

    # Draw the red rectangle platform
    pygame.draw.rect(screen, (255, 0, 0), platform)

    # Update the display
    pygame.display.flip()

pygame.quit()
sys.exit()
