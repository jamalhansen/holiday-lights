
from lights.patterns import rainbow_cycle, solid, alternate, candycane_cycle
from lights.config import Color

try:
  import board
  import neopixel
except ImportError:
    from mock_neopixel import board, neopixel
            
pixel_pin = board.D18
num_pixels = 200
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

try: 
  while True:
    candycane_cycle(pixels, num_pixels, 0.01)
    solid(pixels, Color.OFF.value, 1)
    rainbow_cycle(pixels, num_pixels, 0.01)
    solid(pixels, Color.OFF.value, 1)
    alternate(pixels, num_pixels, Color.RED.value, Color.GREEN.value, 4, 1)

except KeyboardInterrupt:
    print("\nStopping... Happy Holidays!")
    solid(pixels, Color.OFF.value, 0.5)
    print('\nGoodbye!')
