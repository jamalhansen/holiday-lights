def char_light(rgb: tuple[int, int, int], char: str = "█") -> str:
    """
    Converts an RGB tuple into a terminal character with that color.
    
    Args:
        rgb (tuple[int, int, int]): The RGB color values (0-255).
        char (str): The character to display (default is a block).
    
    Returns:
        str: A string with the character in the specified color.
    """
    r, g, b = rgb
    return f"\033[38;2;{r};{g};{b}m{char}"


class board:
    D18 = "Mock Pin"


class neopixel:
    GRB = "GRB"
    RGB = "RGB"

    class NeoPixel:
        def __init__(self, pin, num_pixels, *args, **kwargs):
            print(f"Holiday light simulator initialized with {num_pixels} pixels")
            print(f"Press CTRL + C to stop")
            self.num_pixels = num_pixels
            self.pixels = [(0, 0, 0)] * num_pixels

        def __setitem__(self, index, color):
            if 0 <= index < self.num_pixels:
                self.pixels[index] = color

        def show(self):
            # Print all pixels on the same line
            print('\r' + ''.join([char_light(color) for color in self.pixels]), end="")
            print("\033[0m", end="")  # Reset color without new line

        def fill(self, color):
            self.pixels = [color] * self.num_pixels