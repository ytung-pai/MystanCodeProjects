"""
File: bouncing_ball.py
Name: Yutung
-------------------------
This program should replicate bouncing ball motion three
times (runs) once the user clicks. Even if you attempt clicking,
your software should stop after three runs.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
have_clicked = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global have_clicked
    vx = VX
    vy = 0
    ball = set_up_ball()
    run = 0
    while run < 3:
        onmouseclicked(move)
        if have_clicked:
            ball.move(vx, vy)
            vy += GRAVITY
            if ball.y+SIZE >= window.height:
                vy = -vy*REDUCE
        if ball.x+SIZE >= window.width:
            run += 1
            have_clicked = False
            ball.x = START_X
            ball.y = START_Y
            vy = 0
        pause(DELAY)


def set_up_ball():
    ball = GOval(SIZE, SIZE)
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, x=START_X, y=START_Y)
    return ball


def move(mouse):
    global have_clicked
    have_clicked = True


if __name__ == "__main__":
    main()
