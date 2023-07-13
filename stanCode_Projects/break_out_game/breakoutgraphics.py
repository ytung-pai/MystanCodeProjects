"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
This is the breakout game's starting file.
This file use class as an object constructor,
creating instances along with its methods and
properties.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved, onmousedragged
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        self.have_clicked = False
        self.brick_rows = BRICK_ROWS
        self.brick_cols = BRICK_COLS
        self.ball_radius = BALL_RADIUS
        self.brick_height = BRICK_HEIGHT
        self.brick_spacing = BRICK_SPACING
        self.brick_offset = BRICK_OFFSET
        self.brick_width = BRICK_WIDTH

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle_offset = PADDLE_OFFSET
        self.pad = GRect(paddle_width, paddle_height)
        self.pad.filled = True
        self.pad.fill_color = 'black'
        self.window.add(self.pad, x=self.window_width/2-paddle_width/2, y=self.window_height-paddle_offset-paddle_height)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, x=self.window_width/2 - ball_radius, y=self.window_height/2 - ball_radius)

        # Default initial velocity for the ball
        self.dx = 0
        self.dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.reset_paddle)
        onmouseclicked(self.handle_click)

        # Draw bricks
        color_row = self.brick_rows
        if color_row > 0:
            for i in range(2):
                for j in range(self.brick_cols):
                    brick = GRect(self.brick_width, self.brick_height)
                    brick.filled = True
                    brick.color = 'red'
                    brick.fill_color = 'red'
                    self.window.add(brick, x=j * (self.brick_width + self.brick_spacing),
                                    y=self.brick_offset + i * (self.brick_height + self.brick_spacing))
                color_row -= 1
                if color_row == 0:
                    break
        if color_row > 0:
            for i in range(2):
                for j in range(self.brick_cols):
                    brick = GRect(self.brick_width, self.brick_height)
                    brick.filled = True
                    brick.color = 'orange'
                    brick.fill_color = 'orange'
                    self.window.add(brick, x=j * (self.brick_width + self.brick_spacing),
                                    y=self.brick_offset + + (i+2) * (self.brick_height + self.brick_spacing))
                color_row -= 1
                if color_row == 0:
                    break
        if color_row > 0:
            for i in range(2):
                for j in range(self.brick_cols):
                    brick = GRect(self.brick_width, self.brick_height)
                    brick.filled = True
                    brick.color = 'yellow'
                    brick.fill_color = 'yellow'
                    self.window.add(brick, x=j * (self.brick_width + self.brick_spacing),
                                    y=self.brick_offset + + (i+4) * (self.brick_height + self.brick_spacing))
                color_row -= 1
                if color_row == 0:
                    break
        if color_row > 0:
            for i in range(2):
                for j in range(self.brick_cols):
                    brick = GRect(self.brick_width, self.brick_height)
                    brick.filled = True
                    brick.color = 'green'
                    brick.fill_color = 'green'
                    self.window.add(brick, x=j * (self.brick_width + self.brick_spacing),
                                    y=self.brick_offset + + (i+6) * (self.brick_height + self.brick_spacing))
                color_row -= 1
                if color_row == 0:
                    break
        if color_row > 0:
            for i in range(2):
                for j in range(self.brick_cols):
                    brick = GRect(self.brick_width, self.brick_height)
                    brick.filled = True
                    brick.color = 'blue'
                    brick.fill_color = 'blue'
                    self.window.add(brick, x=j * (self.brick_width + self.brick_spacing),
                                    y=self.brick_offset + + (i+8) * (self.brick_height + self.brick_spacing))
                color_row -= 1
                if color_row == 0:
                    break
        if color_row > 0:
            for i in range(self.brick_rows - 10):
                for j in range(self.brick_cols):
                    brick = GRect(self.brick_width, self.brick_height)
                    brick.filled = True
                    brick.color = 'purple'
                    brick.fill_color = 'purple'
                    self.window.add(brick, x=j * (self.brick_width + self.brick_spacing),
                                    y=self.brick_offset + + (i+10) * (self.brick_height + self.brick_spacing))
                color_row -= 1
                if color_row == 0:
                    break

    def handle_click(self, event):
        self.have_clicked = True
        if self.dx == 0 and self.dy == 0:
            self.dx = random.randint(1, MAX_X_SPEED)
            self.dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.dx = -self.dx

    def reset_paddle(self, mouse):
        if self.pad.width / 2 <= mouse.x < self.window.width - self.pad.width / 2:
            self.pad.x = mouse.x - self.pad.width / 2
            self.pad.y = self.window_height - self.paddle_offset - self.pad.height
        elif mouse < self.pad.width / 2:
            self.pad.x = 0
            self.pad.y = self.window_height - self.paddle_offset - self.pad.height
        else:
            self.pad.x = self.window.width - self.pad.width
            self.pad.y = self.window_height - self.paddle_offset - self.pad.height

    def set_ball_position(self):
        self.ball.x = self.window_width/2 - self.ball_radius
        self.ball.y = self.window_height/2 - self.ball_radius
        self.dx = 0
        self.dy = 0

    def get_dx(self):
        return self.dx

    def get_dy(self):
        return self.dy

