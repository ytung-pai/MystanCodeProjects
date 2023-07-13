"""
File: blur.py
Name: Yutung
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:
    :return:
    """
    new_img = SimpleImage.blank(img.width, img.height)

    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            
            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image.
                pixel = img.get_pixel(x,y)
                pixel1 = img.get_pixel(x+1,y)
                pixel2 = img.get_pixel(x + 1, y + 1)
                pixel3 = img.get_pixel(x, y + 1)
                new_pixel = new_img.get_pixel(x,y)

                new_r = (pixel.red + pixel1.red + pixel2.red + pixel3.red)//4
                new_g = (pixel.red + pixel1.red + pixel2.red + pixel3.red)//4
                new_b = (pixel.red + pixel1.red + pixel2.red + pixel3.red)//4
                new_pixel.red = new_r
                new_pixel.green = new_g
                new_pixel.blue = new_b


            elif x == img.width-1 and y == 0:
                # Get pixel at the top-right corner of the image.
                pixel = img.get_pixel(x, y)
                p3 = img.get_pixel(x, y + 1)
                p4 = img.get_pixel(x - 1, y + 1)
                p5 = img.get_pixel(x - 1, y)
                new_pixel = new_img.get_pixel(x, y)

                new_r = (pixel.red + p3.red + p4.red + p5.red) // 4
                new_g = (pixel.green + p3.green + p4.green + p5.green) // 4
                new_b = (pixel.blue + p3.red + p4.blue + p5.blue ) // 4
                new_pixel.red = new_r
                new_pixel.green = new_g
                new_pixel.blue = new_b

            elif x == 0 and y == img.height-1:
                # Get pixel at the bottom-left corner of the image
                pixel = img.get_pixel(x, y)
                p1 = img.get_pixel(x + 1, y)
                p7 = img.get_pixel(x, y - 1)
                p8 = img.get_pixel(x + 1, y - 1)
                new_pixel = new_img.get_pixel(x, y)

                new_r = (pixel.red + p1.red + p7.red + p8.red) // 4
                new_g = (pixel.green + p1.green + p7.green + p8.green) // 4
                new_b = (pixel.blue + p1.blue + p7.blue + p8.blue) // 4
                new_pixel.red = new_r
                new_pixel.green = new_g
                new_pixel.blue = new_b

            elif x == img.width-1 and y == img.height-1:
                # Get pixel at the bottom-right corner of the image
                pixel = img.get_pixel(x, y)
                p5 = img.get_pixel(x - 1, y)
                p6 = img.get_pixel(x - 1, y - 1)
                p7 = img.get_pixel(x, y - 1)
                new_pixel = new_img.get_pixel(x, y)

                new_r = (pixel.red + p5.red + p6.red + p7.red) // 4
                new_g = (pixel.green + p5.green + p6.green + p7.green) // 4
                new_b = (pixel.blue + p5.blue + p6.blue + p7.blue) // 4
                new_pixel.red = new_r
                new_pixel.green = new_g
                new_pixel.blue = new_b
 
            elif 0 < x < img.width-1 and y == 0:
                # Get top edge's pixels (without two corners)
                pixel = img.get_pixel(x, y)
                p1 = img.get_pixel(x + 1, y)
                p2 = img.get_pixel(x + 1, y + 1)
                p3 = img.get_pixel(x, y + 1)
                p4 = img.get_pixel(x - 1, y + 1)
                p5 = img.get_pixel(x - 1, y)
                new_pixel = new_img.get_pixel(x, y)

                new_r = (pixel.red + p1.red + p2.red + p3.red + p4.red + p5.red) // 6
                new_g = (pixel.green + p1.green + p2.green + p3.green + p4.green + p5.green) // 6
                new_b = (pixel.blue + p1.blue + p2.blue + p3.red + p4.blue + p5.blue) // 6
                new_pixel.red = new_r
                new_pixel.green = new_g
                new_pixel.blue = new_b

            elif 0 < x < img.width-1 and y == img.height-1:
                # Get bottom edge's pixels (without two corners)
                pixel = img.get_pixel(x, y)
                p1 = img.get_pixel(x + 1, y)
                p5 = img.get_pixel(x - 1, y)
                p6 = img.get_pixel(x - 1, y - 1)
                p7 = img.get_pixel(x, y - 1)
                p8 = img.get_pixel(x + 1, y - 1)
                new_pixel = new_img.get_pixel(x, y)

                new_r = (pixel.red + p1.red + p5.red + p6.red + p7.red + p8.red) // 6
                new_g = (pixel.green + p1.green + p5.green + p6.green + p7.green + p8.green) // 6
                new_b = (pixel.blue + p1.blue + p5.blue + p6.blue + p7.blue + p8.blue) // 6
                new_pixel.red = new_r
                new_pixel.green = new_g
                new_pixel.blue = new_b

            elif x == 0 and 0 < y < img.height-1:
                # Get left edge's pixels (without two corners)
                pixel = img.get_pixel(x, y)
                p1 = img.get_pixel(x + 1, y)
                p2 = img.get_pixel(x + 1, y + 1)
                p3 = img.get_pixel(x, y + 1)
                p7 = img.get_pixel(x, y - 1)
                p8 = img.get_pixel(x + 1, y - 1)
                new_pixel = new_img.get_pixel(x, y)

                new_r = (pixel.red + p1.red + p2.red + p3.red + p7.red + p8.red) // 6
                new_g = (pixel.green + p1.green + p2.green + p3.green + p7.green + p8.green) // 6
                new_b = (pixel.blue + p1.blue + p2.blue + p3.red + p7.blue + p8.blue) // 6
                new_pixel.red = new_r
                new_pixel.green = new_g
                new_pixel.blue = new_b

            elif x == img.width-1 and 0 < y < img.height-1:
                # Get right edge's pixels (without two corners)
                pixel = img.get_pixel(x, y)
                p3 = img.get_pixel(x, y + 1)
                p4 = img.get_pixel(x - 1, y + 1)
                p5 = img.get_pixel(x - 1, y)
                p6 = img.get_pixel(x - 1, y - 1)
                p7 = img.get_pixel(x, y - 1)
                new_pixel = new_img.get_pixel(x, y)

                new_r = (pixel.red + p3.red + p4.red + p5.red + p6.red + p7.red) // 6
                new_g = (pixel.green + p3.green + p4.green + p5.green + p6.green + p7.green) // 6
                new_b = (pixel.blue + p3.red + p4.blue + p5.blue + p6.blue + p7.blue) // 6
                new_pixel.red = new_r
                new_pixel.green = new_g
                new_pixel.blue = new_b

            else:
                # Inner pixels.
                pixel = img.get_pixel(x, y)
                p1 = img.get_pixel(x + 1, y)
                p2 = img.get_pixel(x + 1, y + 1)
                p3 = img.get_pixel(x, y + 1)
                p4 = img.get_pixel(x - 1 , y + 1)
                p5 = img.get_pixel(x - 1, y)
                p6 = img.get_pixel(x - 1, y - 1)
                p7 = img.get_pixel(x, y - 1)
                p8 = img.get_pixel(x + 1, y - 1)
                new_pixel = new_img.get_pixel(x, y)

                new_r = (pixel.red + p1.red + p2.red + p3.red+p4.red+p5.red+p6.red+p7.red+p8.red) // 9
                new_g = (pixel.green + p1.green + p2.green + p3.green+p4.green+p5.green+p6.green+p7.green+p8.green) // 9
                new_b = (pixel.blue + p1.blue + p2.blue + p3.red+p4.blue+p5.blue+p6.blue+p7.blue+p8.blue) // 9
                new_pixel.red = new_r
                new_pixel.green = new_g
                new_pixel.blue = new_b

    return new_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
