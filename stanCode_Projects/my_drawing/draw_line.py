"""
File: draw_line.py
Name: Yutung
-------------------------
This program should draw a line between two dots entered
by the user. Your program should not stop creating new lines
while also removing old lines through user click.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the circle size of a pin.
SIZE = 10

window = GWindow()
is_even = False
oval = GOval(SIZE, SIZE)
pre_x = 0
pre_y = 0
end_x = 0
end_y = 0
line = GLine(pre_x, pre_y, end_x, end_y)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    global is_even
    pin = oval
    global line
    line_object = line
    if not is_even:
        window.add(pin, x=mouse.x, y=mouse.y)
        is_even = True
        global pre_x
        global pre_y
        pre_x = mouse.x
        pre_y = mouse.y
    else:
        window.remove(pin)
        window.remove(line_object)
        line = GLine(pre_x, pre_y, mouse.x, mouse.y)
        global end_x
        global end_y
        end_x = mouse.x
        end_y = mouse.y
        window.add(line)
        is_even = False


if __name__ == "__main__":
    main()
