"""
File: stanCodoshop.py
Name: Yutung
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""
import math
import os
import sys

from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """

    color_dist = math.sqrt((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)
    return color_dist


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    # Initialize variables to track total rgb values
    total_r = 0
    total_g = 0
    total_b = 0

    # Iterate over the pixels to sum up their rgb values
    for pixel in pixels:
        total_r += pixel.red
        total_g += pixel.green
        total_b += pixel.blue

    avg_red = int(total_r / len(pixels))
    avg_green = int(total_g / len(pixels))
    avg_blue = int(total_b / len(pixels))

    return [avg_red, avg_green, avg_blue]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    # Calculate the average color
    avg_red = sum(pixel.red for pixel in pixels) / len(pixels)
    avg_green = sum(pixel.green for pixel in pixels) / len(pixels)
    avg_blue = sum(pixel.blue for pixel in pixels) / len(pixels)

    # Initialize variables to track the best pixel and its color distance
    best_pixel = None
    min_color_dist = float('inf')

    # Iterate over the pixels and find the one with the smallest color distance
    for pixel in pixels:
        color_dist = math.sqrt(
            (avg_red - pixel.red) ** 2 + (avg_green - pixel.green) ** 2 + (avg_blue - pixel.blue) ** 2)
        if color_dist < min_color_dist:
            min_color_dist = color_dist
            best_pixel = pixel

    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    print("Displaying image!")

    # Iterate over each pixel position
    for x in range(width):
        for y in range(height):
            pixels = []
            # Iterate over each image and retrieve the pixel at that position
            for image in images:
                pixel = image.get_pixel(x, y)
                pixels.append(pixel)

            best_pixel = get_best_pixel(pixels)

            # Set pixels in the result image
            result.set_pixel(x, y, best_pixel)

    # Display or save the Ghost solution image
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
