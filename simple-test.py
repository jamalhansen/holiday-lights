## from https://docs.circuitpython.org/projects/neopixel/en/latest/examples.html

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time

try:
  import board
  import neopixel
except ImportError:
    # Mock the library for macOS development
    class board:
        D18 = "Mock Pin"

    class neopixel:
        GRB = "GRB"
        RGB = "RGB"

        class NeoPixel:
            def __init__(self, pin, num_pixels, *args, **kwargs):
                print(f"Mock NeoPixel: Initialized with pin {pin} and {num_pixels} pixels")
                self.num_pixels = num_pixels
                self.pixels = [(0, 0, 0)] * num_pixels
            def __setitem__(self, index, color):
                if 0 <= index < self.num_pixels:
                    self.pixels[index] = color
                    print(f"Mock NeoPixel: Set pixel {index} to {color}")
                else:
                    print(f"Mock NeoPixel: Index {index} out of range")
            def show(self):
                print(f"Mock NeoPixel: Current state: {self.pixels}")
            def fill(self, color):
                self.pixels = [color] * self.num_pixels
                print(f"Mock NeoPixel: All pixels set to {color}")
            


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 300

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


try: 
  while True:
      # Comment this line out if you have RGBW/GRBW NeoPixels
      pixels.fill((255, 0, 0))
      # Uncomment this line if you have RGBW/GRBW NeoPixels
      # pixels.fill((255, 0, 0, 0))
      pixels.show()
      time.sleep(1)

      # Comment this line out if you have RGBW/GRBW NeoPixels
      pixels.fill((0, 255, 0))
      # Uncomment this line if you have RGBW/GRBW NeoPixels
      # pixels.fill((0, 255, 0, 0))
      pixels.show()
      time.sleep(1)

      # Comment this line out if you have RGBW/GRBW NeoPixels
      pixels.fill((0, 0, 255))
      # Uncomment this line if you have RGBW/GRBW NeoPixels
      # pixels.fill((0, 0, 255, 0))
      pixels.show()
      time.sleep(1)

      rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step
except KeyboardInterrupt:
    print("\nStopping... Happy Holidays!")
    pixels.fill((0, 0, 0))
    pixels.show()
    print('Goodbye!')
