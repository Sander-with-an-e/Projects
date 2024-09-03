import pygame
import numpy as np

# Dimensions of a single, fixed-width character (Courier New: cour.ttf)
char_width = 12
char_height = 20
char_hw_ratio = char_height / char_width

# List of characters to use in ASCII art
characters = ['M', 'W', 'Q', 'B', 'E', 'R', 'N', '@', 'H', 'q', 'p', 'g', 'K', 'A', '#', 'm', 'b', '8', '0', 'd', 'X', 'D', 'G', 'F', 'P', 'e', 'h', 'U', '9', '6', 'k', 'Z', '%', 'S', '4', 'O', 'x', 'y', 'T', '5', 'w', 'f', 'a', 'V', 's',
              '2', 'L', '$', 'Y', '&', 'n', '3', 'C', 'J', 'u', 'o', 'z', 'I', 'j', 'v', 'c', 'r', 't', 'l', 'i', '1', '=', '?', '7', '>', '<', ']', '[', '(', ')', '+', '*', ';', '}', '{', ':', '/', '\\', '!', '|', '_', ',', '^', '-', '~', '.', ' ']
n_characters = len(characters)

# Corresponding grayscale values
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

def load_image(image_path):
    # Initialize Pygame
    pygame.init()
    # Load the image
    image = pygame.image.load(image_path)
    return image

def convert_to_grayscale(image):
    # Get the color components of the image
    red = pygame.surfarray.pixels_red(image)
    green = pygame.surfarray.pixels_green(image)
    blue = pygame.surfarray.pixels_blue(image)
    
    # Convert the image to grayscale using weighted average
    grayscale = 0.2989 * red + 0.5870 * green + 0.1140 * blue
    return grayscale

def average_grayscale_value(patch):
    return np.mean(patch)

def get_char_for_value(val, min_val, max_val, char_list, char_grayscale):
    # Normalize the value to the range of the grayscale array
    normalized_val = (val - min_val) / (max_val - min_val) * (char_grayscale[-1] - char_grayscale[0]) + char_grayscale[0]
    # Find the closest grayscale value and corresponding character
    index = np.argmin(np.abs(char_grayscale - normalized_val))
    return char_list[index]

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
            avg_value = average_grayscale_value(patch)
            ascii_char = get_char_for_value(avg_value, min_val, max_val, characters, grayscale_values)
            line += ascii_char
        ascii_art.append(line)

    return "\n".join(ascii_art)

def main(image_path):
    # Load and convert the image to grayscale
    image = load_image(image_path)
    grayscale_image = convert_to_grayscale(image)

    # Calculate patch dimensions based on character dimensions and aspect ratio
    patch_width = int(5)  # Example patch width
    patch_height = int(patch_width * char_hw_ratio)

    # Generate ASCII art from the grayscale image
    ascii_art = generate_ascii_art(grayscale_image, patch_width, patch_height)
    
    # Print the ASCII art
    print(ascii_art)

if __name__ == "__main__":
    image_path = "python.jpg"  # Change this to your image path
    main(image_path)
