"""
File: fire.py
Name: Yutung
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: str, the file path of the original image
    :return: SimpleImage, the image with highlighted fires.
    """
    highlighted_fire = SimpleImage(filename)
    for x in range(highlighted_fire.width):
        for y in range(highlighted_fire.height):
            pixel = highlighted_fire.get_pixel(x,y)
            pixel_avg = (pixel.red+pixel.green+pixel.blue) /3
            if pixel.red > pixel_avg * HURDLE_FACTOR:
                pixel.red = 255
                pixel.green = 0
                pixel.blue = 0
            else:
                pixel.red = pixel_avg
                pixel.green = pixel_avg
                pixel.blue = pixel_avg
    return highlighted_fire


def main():
    """
    This program points out the fire in the greenland image.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
