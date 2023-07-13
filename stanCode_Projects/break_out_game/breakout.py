"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
You have three lives. Your aim is to remove
all of the bricks. Keep the ball bouncing as
many times as you can by using your mouse to
manipulate the paddle. When you miss the ball,
you lose a life, and the game finishes when you
lose three lives.
"""
from campy import graphics
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 3  # Number of attempts
is_collision = False


def main():
    graphics = BreakoutGraphics()
    global is_collision
    lives = NUM_LIVES
    num_bricks = graphics.brick_rows * graphics.brick_cols
    run = 0
    while run < NUM_LIVES and num_bricks > 0:
        if graphics.have_clicked:
            graphics.ball.move(graphics.dx, graphics.dy)

            obj_upper_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
            obj_upper_right = graphics.window.get_object_at(graphics.ball.x + 2 * graphics.ball_radius, graphics.ball.y)
            obj_bottom_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + 2 * graphics.ball_radius)
            obj_bottom_right = graphics.window.get_object_at(graphics.ball.x + 2 * graphics.ball_radius
                                                             , graphics.ball.y + 2 * graphics.ball_radius)

            # Check collisions from the ball's upper left corner
            if obj_upper_left is not None:
                # Hit a brick
                if obj_upper_left.y < graphics.pad.y:
                    graphics.window.remove(obj_upper_left)
                    num_bricks -= 1
                graphics.dy = -graphics.dy
                continue
            # Check collisions from the ball's upper right corner
            if obj_upper_right is not None:
                if obj_upper_right.y < graphics.pad.y:
                    graphics.window.remove(obj_upper_right)
                    num_bricks -= 1
                graphics.dy = -graphics.dy
                continue
            # Check collisions from the ball's bottom left corner
            if obj_bottom_left is not None:
                if obj_bottom_left.y < graphics.pad.y:
                    graphics.window.remove(obj_bottom_left)
                    num_bricks -= 1
                graphics.dy = -graphics.dy
                continue
            # Check collisions from the ball's bottom right corner
            if obj_bottom_right is not None:
                if obj_bottom_right.y < graphics.pad.y:
                    graphics.window.remove(obj_bottom_right)
                    num_bricks -= 1
                graphics.dy = -graphics.dy
                continue

            # Check collisions for the four window edges
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                graphics.dx = -graphics.dx
            if graphics.ball.y <= 0:
                graphics.dy = -graphics.dy
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                run += 1
                graphics.have_clicked = False
                graphics.set_ball_position()
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
