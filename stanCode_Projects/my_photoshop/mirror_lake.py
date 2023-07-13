"""
File: mirror_lake.py
Name:
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the file name of the original image
    :return:
    """
    original = SimpleImage(filename)
    reflected = SimpleImage.blank(original.width, original.height*2)
    for x in range(original.width):
        for y in range(original.height):
            colored_pixel = original.get_pixel(x,y)
            blank_pixel = reflected.get_pixel(x,y)
            blank_pixel.red = colored_pixel.red
            blank_pixel.green = colored_pixel.green
            blank_pixel.blue = colored_pixel.blue

            blank_pixel2 = reflected.get_pixel(x, reflected.height-y-1)
            blank_pixel2.red = colored_pixel.red
            blank_pixel2.green = colored_pixel.green
            blank_pixel2.blue = colored_pixel.blue

    return reflected


def main():
    """
    This program shows the image of mirror lake which was reflected
    by the original_mt image.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
