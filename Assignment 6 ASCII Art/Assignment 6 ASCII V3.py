import numpy as np
import pygame
## Pre-calculated values:

# Dimensions of a single, fixed-width character:
# (determined for Courier New: cour.ttf)
char_width = 12
char_height = 20
char_hw_ratio = char_height / char_width

# A list of characters that you can use in your ASCII art...
characters = ['M', 'W', 'Q', 'B', 'E', 'R', 'N', '@', 'H', 'q', 'p', 'g', 'K', 'A', '#', 'm', 'b', '8', '0', 'd', 'X', 'D', 'G', 'F', 'P', 'e', 'h', 'U', '9', '6', 'k', 'Z', '%', 'S', '4', 'O', 'x', 'y', 'T', '5', 'w', 'f', 'a', 'V', 's',
                '2', 'L', '$', 'Y', '&', 'n', '3', 'C', 'J', 'u', 'o', 'z', 'I', 'j', 'v', 'c', 'r', 't', 'l', 'i', '1', '=', '?', '7', '>', '<', ']', '[', '(', ')', '+', '*', ';', '}', '{', ':', '/', '\\', '!', '|', '_', ',', '^', '-', '~', '.', ' ']
n_characters = len(characters)

# ... and the corresponding grayscale values
grayscale_values = np.array([217.56944444, 218.82291667, 219.89236111, 220.19444444,
                      222.14583333, 222.94097222, 223.0625, 223.17361111,
                      223.22222222, 223.23958333, 223.45486111, 223.60416667,
                      224.05208333, 224.09722222, 224.33333333, 225.25,
                      225.59722222, 225.62152778, 225.91666667, 225.96180556,
                      226.10763889, 226.74305556, 226.80208333, 227.04861111,
                      227.42361111, 228.45833333, 228.61458333, 228.73958333,
                      228.76736111, 228.80555556, 228.8125, 228.90625,
                      228.98611111, 229.06597222, 229.28472222, 229.61805556,
                      229.96527778, 230.07291667, 230.17361111, 230.21875,
                      230.60416667, 230.62847222, 230.84375, 231.03472222,
                      231.05555556, 231.46875, 231.55555556, 231.9375,
                      232.04861111, 232.07291667, 232.64583333, 232.68055556,
                      233.16319444, 233.53472222, 233.70138889, 234.20833333,
                      234.40625, 234.76388889, 234.93055556, 235.30208333,
                      235.36805556, 235.44791667, 235.5, 236.53472222,
                      237.32986111, 237.67361111, 237.70138889, 238.61458333,
                      238.61805556, 238.78125, 238.78472222, 238.79166667,
                      238.98611111, 239.07638889, 239.08680556, 239.97569444,
                      240.32291667, 240.78125, 241.50694444, 241.57291667,
                      242.25694444, 243.13194444, 243.18055556, 243.31944444,
                      244.30208333, 244.61805556, 245.03819444, 246.62847222,
                      247.58333333, 247.60763889, 248.62847222, 255.0])

# Start writing your code here!

pygame.init()

def convert_to_grayscale(image):

    # Get the colour components of the image
    red = pygame.surfarray.pixels_red(image)
    green = pygame.surfarray.pixels_green(image)
    blue = pygame.surfarray.pixels_blue(image)
    
    # Convert the image to grayscale using weighted average
    grayscale = 0.299 * red + 0.587 * green + 0.114 * blue

    return grayscale

def get_char_for_value(avg_value, min_val, max_val, characters, grayscale_values):

    # Normalize the value to the range of the grayscale array
    normalized_val = (avg_value - min_val) / (max_val - min_val) * (grayscale_values[-1] - grayscale_values[0]) + grayscale_values[0]

    # Create a new array of the values of the difference between the grayscale values and normalized values
    normalized_val_grayscale_array = np.abs(grayscale_values - normalized_val)

    # Find the index of the smallest value in the new array
    index = np.argmin(normalized_val_grayscale_array)

    # Return the corresponding character
    return characters[index]

def generate_ascii_art(grayscale_image, patch_width, patch_height):

    rows, cols = grayscale_image.shape
    ascii_art = []

    # Determine min and max grayscale values of the image
    min_val = np.min(grayscale_image)
    max_val = np.max(grayscale_image)

    for y in range(0, rows, patch_height):
        line = ""
        for x in range(0, cols, patch_width):
            patch = grayscale_image[y:y + patch_height, x:x + patch_width]
            avg_value = np.mean(patch)
            ascii_char = get_char_for_value(avg_value, min_val, max_val, characters, grayscale_values)
            line += ascii_char
        ascii_art.append(line)

    return ascii_art

def render_ascii_image(ascii_art, font_path, font_size, bg_colour, text_colour):

    font = pygame.font.Font(font_path, font_size)
    char_width, char_height = font.size('A')  

    
    # Calculate the width and height of the rendered ASCII image
    img_width = char_width * len(ascii_art[0])
    img_height = char_height * len(ascii_art)

    # Create a surface for the ASCII art with the calculated width and height
    image = pygame.Surface((img_width, img_height))

    # Fill entire surface with background colour
    image.fill(bg_colour)

    # Iterate over each character in the ascii_art list and render it using the specified font and foreground color
    for y, line in enumerate(ascii_art):
        for x, char in enumerate(line):
            char_surface = font.render(char, True, text_colour)
            image.blit(char_surface, (x * char_width, y * char_height))

    return image

def main(image):

    # Convert the image to grayscale
    grayscale_image = convert_to_grayscale(image)

    # Calculate patch dimensions based on character dimensions and aspect ratio
    patch_width = 5  # Example patch width
    patch_height = int(patch_width * char_hw_ratio)

    # Generate ASCII art from the grayscale image
    ascii_art = generate_ascii_art(grayscale_image, patch_width, patch_height)

    # Render ASCII art as an image
    font_path = pygame.font.match_font('courier new')  
    font_size = 12
    bg_colour = (0, 0, 0)
    text_colour = (255, 255, 255)
    ascii_image = render_ascii_image(ascii_art, font_path, font_size, bg_colour, text_colour)

    # Rotate the image 90 degrees to the right
    rotated_image = pygame.transform.rotate(ascii_image, -90)

    # Mirror the image from left to right
    mirrored_image = pygame.transform.flip(rotated_image, True, False)

    # Display the ASCII art image
    screen = pygame.display.set_mode((mirrored_image.get_width(), mirrored_image.get_height()))
    pygame.display.set_caption("ASCII Art")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(mirrored_image, (0, 0))
        pygame.display.flip()

    pygame.quit()


# Choose the image name
image = pygame.image.load("python.jpg")

# Start the main def with the image
main(image)
