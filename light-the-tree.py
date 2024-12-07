
from lights.patterns import rainbow_cycle, solid, alternate, candycane_cycle

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
 
RED = (255, 0, 0)
GREEN = (0, 255, 0)
OFF = (0, 0, 0)

try: 
  while True:
    candycane_cycle(pixels, num_pixels, 0.01)
    solid(pixels, OFF, 1)
    rainbow_cycle(pixels, num_pixels, 0.01)
    solid(pixels, OFF, 1)
    alternate(pixels, num_pixels, RED, GREEN, 4, 1)

except KeyboardInterrupt:
    print("\nStopping... Happy Holidays!")
    solid(pixels, OFF, 0.5)
    print('Goodbye!')
