import pygame
import sys
import math

# Initialize PyGame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dogfight Game")

# Load and scale images
red_ship_original = pygame.image.load("redship.png")
blue_ship_original = pygame.image.load("blueship.png")
missile_original = pygame.image.load("missile.png")

# Scale images to 12% of their original size
scale_factor = 0.12
red_ship_original = pygame.transform.scale(red_ship_original, (int(red_ship_original.get_width() * scale_factor), int(red_ship_original.get_height() * scale_factor)))
blue_ship_original = pygame.transform.scale(blue_ship_original, (int(blue_ship_original.get_width() * scale_factor), int(blue_ship_original.get_height() * scale_factor)))
missile_original = pygame.transform.scale(missile_original, (int(missile_original.get_width() * scale_factor), int(missile_original.get_height() * scale_factor)))

# Precompute rotated images
def precompute_rotations(image):
    rotated_images = []
    for angle in range(360):
        rotated_image = pygame.transform.rotate(image, -angle)  # Note the negative sign for counterclockwise rotation
        rotated_images.append(rotated_image)
    return rotated_images

red_ship_images = precompute_rotations(red_ship_original)
blue_ship_images = precompute_rotations(blue_ship_original)
missile_images = precompute_rotations(missile_original)

# Initial positions and angles
red_pos = [screen_width / 2 - 100, screen_height / 2]
blue_pos = [screen_width / 2 + 100, screen_height / 2]
red_angle = 180
blue_angle = 90
speed = 200  # pixels per second

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    dt = clock.tick(60) / 1000.0  # Amount of seconds between each loop

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Equations of motion/kinematics
    red_pos[0] = (red_pos[0] + math.cos(math.radians(red_angle)) * speed * dt) % screen_width
    red_pos[1] = (red_pos[1] - math.sin(math.radians(red_angle)) * speed * dt) % screen_height
    blue_pos[0] = (blue_pos[0] + math.cos(math.radians(blue_angle)) * speed * dt) % screen_width
    blue_pos[1] = (blue_pos[1] - math.sin(math.radians(blue_angle)) * speed * dt) % screen_height

    # Drawing
    screen.fill((0, 0, 0))  # Fill the screen with black
    screen.blit(red_ship_images[int(red_angle) % 360], (red_pos[0] - red_ship_images[int(red_angle) % 360].get_width() // 2, red_pos[1] - red_ship_images[int(red_angle) % 360].get_height() // 2))
    screen.blit(blue_ship_images[int(blue_angle) % 360], (blue_pos[0] - blue_ship_images[int(blue_angle) % 360].get_width() // 2, blue_pos[1] - blue_ship_images[int(blue_angle) % 360].get_height() // 2))
    
    # Update the display
    pygame.display.flip()

# Quit PyGame
pygame.quit()
sys.exit()
