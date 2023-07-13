"""
File: my_drawing.py
Name: Yutung
----------------------
This program uses campy.graphics to generate geometry,
which is then assembled into an image.
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Abo_Radish
    This figure is created by my dear friend. It was promoted
    on Instagram via her account. To see some more radishes,
    follow abo.934 :)
    """
    window = GWindow(width=800, height=600, title='abo.934')
    hair = GRect(35, 100, x=375, y=110)
    hair.filled = True
    hair.fill_color = 'yellow green'
    hair2 = GRect(40, 132, x=410, y=80)
    hair2.filled = True
    hair2.fill_color = 'yellow green'
    hair3 = GRect(40, 134, x=450, y=85)
    hair3.filled = True
    hair3.fill_color = 'yellow green'
    hair4 = GRect(35, 127, x=490, y=100)
    hair4.filled = True
    hair4.fill_color = 'yellow green'
    body = GArc(600, 850, 0, 180, 95, 210)
    # GArc(width, height, start, sweep, x, y)
    l_eye = GOval(13, 13, x=405, y=315)
    l_eye.filled = True
    l_eye.fill_color = 'dark grey'
    r_eye = GOval(13, 13, x=460, y=315)
    r_eye.filled = True
    r_eye.fill_color = 'dark grey'
    mouth = GLine(375, 380, 465, 375)
    l_blush = GOval(84, 84, x=235, y=315)
    l_blush.filled = True
    l_blush.fill_color = 'chocolate'
    r_blush = GOval(85, 85, x=535, y=300)
    r_blush.filled = True
    r_blush.fill_color = 'chocolate'

    window.add(hair)
    window.add(hair2)
    window.add(hair3)
    window.add(hair4)
    window.add(body)
    window.add(l_eye)
    window.add(r_eye)
    window.add(mouth)
    window.add(r_blush)
    window.add(l_blush)


if __name__ == '__main__':
    main()
