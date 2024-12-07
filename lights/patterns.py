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
    if pos < 0 or pos > 255:
        return Color.OFF.value
    elif pos < 63:
        return Color.RED.value
    elif pos < 126:
        pos -= 63
        return (255, int(pos * 4), int(pos * 4))
    elif pos < 192:
        return Color.WHITE.value
    else:
        pos -= 192
        return (255, 255 - int(pos * 4), 255 - int(pos * 4))

def rainbow_cycle(pix: "NeoPixel", pixel_count: int, wait: float): 
    cycle(pix, pixel_count, wait, wheel)

def candycane_cycle(pix: "NeoPixel", pixel_count: int, wait: float): 
    cycle(pix, pixel_count, wait, candycane)

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
