"""
File: sierpinski.py
Name: Yutung
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6            # Controls the order of Sierpinski Triangle
LENGTH = 600         # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100   # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950   # The width of the GWindow
WINDOW_HEIGHT = 700  # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
    """
    This program uses a recursive function to carry out the
    Sierpinski triangle method. It draws the required triangle
    in the order indicated by the user.
    """
    sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)
    pause(1000)  # Pause for 1 second to see the drawn triangle


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
    """
    :param order: int
    :param length: float
    :param upper_left_x: int
    :param upper_left_y: int
    :return: int
    """
    # Base case
    if order == 0:
        return 1
    else:
        # Start with a large triangle
        line_upper = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
        window.add(line_upper)
        line_left = GLine(upper_left_x, upper_left_y, upper_left_x + 0.5 * length, upper_left_y + 0.866 * length)
        window.add(line_left)
        line_right = GLine(upper_left_x + length, upper_left_y, upper_left_x + 0.5 * length,
                           upper_left_y + 0.866 * length)
        window.add(line_right)

        # Initialize a variable to track the number of smaller triangles cut out
        count = 0

        # Recursively call the sierpinski_triangle function for each sub-triangle
        count += sierpinski_triangle(order - 1, length / 2, upper_left_x, upper_left_y)
        count += sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 2, upper_left_y)
        count += sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 4,
                                     upper_left_y + 0.866 * length / 2)

        return count


if __name__ == '__main__':
    main()
