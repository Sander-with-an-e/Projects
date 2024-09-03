import pygame
import sys
import math
import time

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
explosion_image = pygame.image.load("ex4.gif")

# Scale images to 12% of their original size
scale_factor = 0.12
red_ship_original = pygame.transform.scale(red_ship_original, (int(red_ship_original.get_width() * scale_factor), int(red_ship_original.get_height() * scale_factor)))
blue_ship_original = pygame.transform.scale(blue_ship_original, (int(blue_ship_original.get_width() * scale_factor), int(blue_ship_original.get_height() * scale_factor)))
missile_original = pygame.transform.scale(missile_original, (int(missile_original.get_width() * scale_factor), int(missile_original.get_height() * scale_factor)))
explosion_image = pygame.transform.scale(explosion_image, (int(explosion_image.get_width() * scale_factor), int(explosion_image.get_height() * scale_factor)))

# Load explosion sound
explode = pygame.mixer.Sound("explosion.wav")

# Precompute rotated images
def precompute_rotations(image):
    rotated_images = []
    for angle in range(360):
        rotated_image = pygame.transform.rotate(image, angle)  
        rotated_images.append(rotated_image)
    return rotated_images

red_ship_images = precompute_rotations(red_ship_original)
blue_ship_images = precompute_rotations(blue_ship_original)
missile_images = precompute_rotations(missile_original)

# Initial positions and angles
red_pos = [screen_width / 2 - 100, screen_height / 2]
blue_pos = [screen_width / 2 + 100, screen_height / 2]
red_angle = 180
blue_angle = 0
speed = 200  # pixels per second
omega = 180 # degrees/s

# Missile variables
missile_speed = 1000  # pixels per second
missile_lifetime = 1.0  # seconds
red_missile_pos = [-1, -1]
blue_missile_pos = [-1, -1]
red_missile_angle = 0
blue_missile_angle = 0
tmisred = -1.0
tmisblue = -1.0

#variable time step
t0 = 0.001 * pygame.time.get_ticks()
maxdt = 0.5 # time step limit to avoid jumps

def distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

def reset_game():
    global red_pos, blue_pos, red_angle, blue_angle, tmisred, tmisblue
    red_pos = [screen_width / 2 - 100, screen_height / 2]
    blue_pos = [screen_width / 2 + 100, screen_height / 2]
    red_angle = 180
    blue_angle = 90
    tmisred = -1.0
    tmisblue = -1.0

# Game loop
running = True
while running:
    t = 0.001 * pygame.time.get_ticks()
    dt = min(t - t0, maxdt)   # set maximum limit to dt

    # Events for stopping the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Get the state of all keyboard buttons
    keys = pygame.key.get_pressed()

    # Control redship (A/D for left/right turns)
    if keys[pygame.K_a]:
        red_angle += omega * dt
    if keys[pygame.K_d]:
        red_angle -= omega * dt

    # Control blueship (K/; for left/right turns)
    if keys[pygame.K_k]:
        blue_angle += omega * dt
    if keys[pygame.K_SEMICOLON]:
        blue_angle -= omega * dt

    # Normalize angles to be within 0-359 degrees
    red_angle %= 360
    blue_angle %= 360

     # Fire red missile (S key)
    if keys[pygame.K_s] and tmisred <= 0:
        tmisred = missile_lifetime
        red_missile_pos = red_pos[:]
        red_missile_angle = red_angle

    # Fire blue missile (L key)
    if keys[pygame.K_l] and tmisblue <= 0:
        tmisblue = missile_lifetime
        blue_missile_pos = blue_pos[:]
        blue_missile_angle = blue_angle
    
    if dt>0.0:
        t0 = t
        
        # Equations of motion/kinematics
        red_pos[0] = (red_pos[0] + math.cos(math.radians(red_angle)) * speed * dt) % screen_width
        red_pos[1] = (red_pos[1] - math.sin(math.radians(red_angle)) * speed * dt) % screen_height
        blue_pos[0] = (blue_pos[0] + math.cos(math.radians(blue_angle)) * speed * dt) % screen_width
        blue_pos[1] = (blue_pos[1] - math.sin(math.radians(blue_angle)) * speed * dt) % screen_height

        # Equations of motion/kinematics for missiles
        if tmisred > 0:
            tmisred -= dt
            red_missile_pos[0] += math.cos(math.radians(red_missile_angle)) * missile_speed * dt
            red_missile_pos[1] -= math.sin(math.radians(red_missile_angle)) * missile_speed * dt
        if tmisblue > 0:
            tmisblue -= dt
            blue_missile_pos[0] += math.cos(math.radians(blue_missile_angle)) * missile_speed * dt
            blue_missile_pos[1] -= math.sin(math.radians(blue_missile_angle)) * missile_speed * dt
        
        # Check for collisions
        red_hit = tmisblue > 0 and distance(red_pos, blue_missile_pos) < 20  # Assume 20 pixels as the collision distance
        blue_hit = tmisred > 0 and distance(blue_pos, red_missile_pos) < 20  # Assume 20 pixels as the collision distance

        if red_hit or blue_hit:
            explode.play()
            if red_hit:
                explosion_pos = red_pos
                winner = "Blue"
            if blue_hit:
                explosion_pos = blue_pos
                winner = "Red"
            
            # Display explosion and wait
            screen.blit(explosion_image, (explosion_pos[0] - explosion_image.get_width() // 2, explosion_pos[1] - explosion_image.get_height() // 2))
            pygame.display.flip()
            pygame.time.wait(2000)
            
            # Print winner and reset the game
            print(f"{winner} wins!")
            reset_game()
        
        # Drawing
        screen.fill((0, 0, 0))  # Fill the screen with black
        screen.blit(red_ship_images[int(red_angle) % 360], (red_pos[0] - red_ship_images[int(red_angle) % 360].get_width() // 2, red_pos[1] - red_ship_images[int(red_angle) % 360].get_height() // 2))
        screen.blit(blue_ship_images[int(blue_angle) % 360], (blue_pos[0] - blue_ship_images[int(blue_angle) % 360].get_width() // 2, blue_pos[1] - blue_ship_images[int(blue_angle) % 360].get_height() // 2))

        # Draw missiles
        if tmisred > 0:
            screen.blit(missile_images[int(red_missile_angle)], (red_missile_pos[0] - missile_images[int(red_missile_angle)].get_width() // 2, red_missile_pos[1] - missile_images[int(red_missile_angle)].get_height() // 2))
        if tmisblue > 0:
            screen.blit(missile_images[int(blue_missile_angle)], (blue_missile_pos[0] - missile_images[int(blue_missile_angle)].get_width() // 2, blue_missile_pos[1] - missile_images[int(blue_missile_angle)].get_height() // 2))

        # Update the display
        pygame.display.flip()

# Quit PyGame
pygame.quit()
sys.exit()
