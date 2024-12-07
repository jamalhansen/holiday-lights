import time 
from lights.config import Color
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from neopixel import NeoPixel 

def wheel(pos):
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
    return (r, g, b)

def candycane(pos):
    return stripe(pos, Color.RED.value, Color.WHITE.value)

def redgreen(pos):
    return stripe(pos, Color.RED.value, Color.GREEN.value)
    
def stripe(pos, color1, color2):
    if pos < 0 or pos > 255:
        return Color.OFF.value 
    elif pos < 128:
        # Smooth transition from color1 to color2
        factor = pos / 127
        r = int(color1[0] * (1 - factor) + color2[0] * factor)
        g = int(color1[1] * (1 - factor) + color2[1] * factor)
        b = int(color1[2] * (1 - factor) + color2[2] * factor)
        return (r, g, b)
    else:
        # Smooth transition from color2 back to color1
        factor = (pos - 128) / 127
        r = int(color2[0] * (1 - factor) + color1[0] * factor)
        g = int(color2[1] * (1 - factor) + color1[1] * factor)
        b = int(color2[2] * (1 - factor) + color1[2] * factor)
        return (r, g, b)

def rainbow_cycle(pix: "NeoPixel", pixel_count: int, wait: float): 
    cycle(pix, pixel_count, wait, wheel)

def candycane_cycle(pix: "NeoPixel", pixel_count: int, wait: float): 
    cycle(pix, pixel_count, wait, candycane)

def redgreen_cycle(pix: "NeoPixel", pixel_count: int, wait: float): 
    cycle(pix, pixel_count, wait, redgreen)

def cycle(pix: "NeoPixel", pixel_count: int, wait: float, pattern: callable): 
    for j in range(255):
        for i in range(pixel_count):
            pixel_index = (i * 256 // pixel_count) + j
            pix[i] = pattern(pixel_index & 255)
        pix.show()
        time.sleep(wait)

def solid(pix: "NeoPixel", color: tuple, wait: float): 
    pix.fill(color)
    pix.show()
    time.sleep(wait)

def alternate(pix: "NeoPixel", pixel_count: int, color_one: tuple, color_two: tuple, times: int, wait: float): 
    for j in range(times):
        for i in range(pixel_count):
            anchor = j % 2
            color = color_one if i % 2 == anchor else color_two
            pix[i] = color
        pix.show()
        time.sleep(wait)
