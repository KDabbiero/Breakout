"""
File: breakout.py
Original Author: Katelyn Dabbiero
This program implements a simplistic version of the
classic Breakout arcade game.
"""
import arcade
import random
from abc import abstractmethod

# These are Global constants to use throughout the game
SCREEN_WIDTH = 580
SCREEN_HEIGHT = 400
BALL_RADIUS = 5

PADDLE_WIDTH = 50
PADDLE_HEIGHT = 10
MOVE_AMOUNT = 10

SCORE_HIT = 1
SCORE_MISS = 5
#Point class is used to create the points for the center of the ball and the center of the pong
class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
#velocity determines how fast the ball will move
class Velocity:
    def __init__(self):
        self.dx = 0
        self.dy = 0

class Ball:
    def __init__(self):
        self.center = Point()
        self.center.x = 555
        self.center.y = random.uniform(5, 395)
        self.velocity = Velocity()
        self.velocity.dx = random.randint(-2, 2)
        self.velocity.dy = random.randint(-2, 2)

#draws the circle
    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, BALL_RADIUS, arcade.color.BLACK)

#moves the ball forward
    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

#enables the ball to change direction when it hits the sides
    def bounce_horizontal(self):
        self.velocity.dx *= -1

#same as above but for the y axis
    def bounce_vertical(self):
        if abs(self.velocity.dy) > 2:
            self.velocity.dy = -2
        else:
            self.velocity.dy *= -1.05

#restarts the game when the ball goes out of play
    def restart(self):
        self.center = Point()
        self.velocity = Velocity()
        self.velocity.dx = random.uniform(-2, 4)
        self.velocity.dy = random.uniform(-2, 4)

class Paddle:
    def __init__(self):
        self.center = Point()
        self.center.x = 595
        self.center.y = 10
#draw the paddle(black rectangle)
    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, PADDLE_WIDTH, PADDLE_HEIGHT, arcade.color.BLACK)
#moves the paddle up
    def move_left(self):
        if self.center.x <= PADDLE_WIDTH / 2:
            self.center.x = PADDLE_WIDTH / 2
        else:
            self.center.x -= 5
#moves the paddle down
    def move_right(self):
        if self.center.x >= SCREEN_WIDTH - PADDLE_WIDTH / 2:
            self.center.x = SCREEN_WIDTH - PADDLE_WIDTH / 2
        else:
            self.center.x += 5

class Bricks:
    def __init__(self):
        self.center = Point()
        self.center.x = 0
        self.center.y = 0

    #@abstractmethod
    #def hit(self):
        #pass

    @abstractmethod
    def draw(self):
        pass

class Filled(Bricks):
    def __init__(self):
        self.center = Point()
        self.center.x = 0
        self.center.y = 0
        self.alive = True
        self.hit1 = 2

    def draw(self, x, y):
        self.center.x = x
        self.center.y = y
        arcade.draw_rectangle_filled(self.center.x, self.center.y, PADDLE_WIDTH, PADDLE_HEIGHT, arcade.color.BLACK)

class Breakout(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Point
        Velocity
        Ball
        Paddle
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class,
    but should not have to if you don't want to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.ball = Ball()
        self.paddle = Paddle()
        self.score = 0

        self.filled1 = Filled()
        self.filled2 = Filled()
        self.filled3 = Filled()
        self.filled4 = Filled()
        self.filled5 = Filled()
        self.filled6 = Filled()
        self.filled7 = Filled()
        self.filled8 = Filled()
        self.filled9 = Filled()
        self.filled10 = Filled()
        self.filled11 = Filled()
        self.bricks = [self.filled1, self.filled2, self.filled3, self.filled4, self.filled5, self.filled6, self.filled7, self.filled8, self.filled9, self.filled10, self.filled11]

        self.filled1_2 = Filled()
        self.filled2_2 = Filled()
        self.filled3_2 = Filled()
        self.filled4_2 = Filled()
        self.filled5_2 = Filled()
        self.filled6_2 = Filled()
        self.filled7_2 = Filled()
        self.filled8_2 = Filled()
        self.filled9_2 = Filled()
        self.filled10_2 = Filled()
        self.filled11_2 = Filled()
        self.bricks_2 = [self.filled1_2, self.filled2_2, self.filled3_2, self.filled4_2, self.filled5_2, self.filled6_2, self.filled7_2, self.filled8_2, self.filled9_2, self.filled10_2, self.filled11_2]

        self.filled1_3 = Filled()
        self.filled2_3 = Filled()
        self.filled3_3 = Filled()
        self.filled4_3 = Filled()
        self.filled5_3 = Filled()
        self.filled6_3 = Filled()
        self.filled7_3 = Filled()
        self.filled8_3 = Filled()
        self.filled9_3 = Filled()
        self.filled10_3 = Filled()
        self.filled11_3 = Filled()
        self.bricks_3 = [self.filled1_3, self.filled2_3, self.filled3_3, self.filled4_3, self.filled5_3, self.filled6_3, self.filled7_3, self.filled8_3, self.filled9_3, self.filled10_3, self.filled11_3]

        # These are used to see if the user is
        # holding down the arrow keys
        self.holding_left = False
        self.holding_right = False

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsiblity of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # draw each object
        self.ball.draw()
        self.paddle.draw()
        
        self.create_brick()

        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.NAVY_BLUE)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """

        # Move the ball forward one element in time
        self.ball.advance()

        # Check to see if keys are being held, and then
        # take appropriate action
        self.check_keys()

        # check for ball at important places
        self.check_miss()
        self.check_hit_paddle()
        self.check_hit_brick() 
        self.check_bounce()
        self.create_brick()
        self.cleanup_zombies()

    def create_brick(self):

        # Drawws the first row from the top of the screen
        if self.filled1.alive:
            self.filled1.draw(25, 375)
        
        if self.filled2.alive:
            self.filled2.draw(78, 375)

        if self.filled3.alive:
            self.filled3.draw(131, 375)
        
        if self.filled4.alive:
            self.filled4.draw(184, 375)
        
        if self.filled5.alive:
            self.filled5.draw(237, 375)

        if self.filled6.alive:
            self.filled6.draw(290, 375)
        
        if self.filled7.alive:
            self.filled7.draw(343, 375)

        if self.filled8.alive:
            self.filled8.draw(396, 375)

        if self.filled9.alive:
            self.filled9.draw(449, 375)

        if self.filled10.alive:
            self.filled10.draw(502, 375)

        if self.filled11.alive:
            self.filled11.draw(555, 375)

        # Beginning of drawing the second row of bricks
        if self.filled1_2.alive:
            self.filled1_2.draw(25, 362)
        
        if self.filled2_2.alive:
            self.filled2_2.draw(78, 362)

        if self.filled3_2.alive:
            self.filled3_2.draw(131, 362)
        
        if self.filled4_2.alive:
            self.filled4_2.draw(184, 362)
        
        if self.filled5_2.alive:
            self.filled5_2.draw(237, 362)

        if self.filled6_2.alive:
            self.filled6_2.draw(290, 362)
        
        if self.filled7_2.alive:
            self.filled7_2.draw(343, 362)

        if self.filled8_2.alive:
            self.filled8_2.draw(396, 362)

        if self.filled9_2.alive:
            self.filled9_2.draw(449, 362)

        if self.filled10_2.alive:
            self.filled10_2.draw(502, 362)

        if self.filled11_2.alive:
            self.filled11_2.draw(555, 362)

        # Draws the third row
        if self.filled1_3.alive:
            self.filled1_3.draw(25, 349)
        
        if self.filled2_3.alive:
            self.filled2_3.draw(78, 349)

        if self.filled3_3.alive:
            self.filled3_3.draw(131, 349)
        
        if self.filled4_3.alive:
            self.filled4_3.draw(184, 349)
        
        if self.filled5_3.alive:
            self.filled5_3.draw(237, 349)

        if self.filled6_3.alive:
            self.filled6_3.draw(290, 349)
        
        if self.filled7_3.alive:
            self.filled7_3.draw(343, 349)

        if self.filled8_3.alive:
            self.filled8_3.draw(396, 349)

        if self.filled9_3.alive:
            self.filled9_3.draw(449, 349)

        if self.filled10_3.alive:
            self.filled10_3.draw(502, 349)

        if self.filled11_3.alive:
            self.filled11_3.draw(555, 349)


    def check_hit_paddle(self):
        """
        Checks to see if the ball has hit the paddle
        and if so, calls its bounce method.
        :return:
        """
        too_close_x = (PADDLE_WIDTH / 2) + BALL_RADIUS
        too_close_y = (PADDLE_HEIGHT / 2) + BALL_RADIUS

        if (abs(self.ball.center.x - self.paddle.center.x) < too_close_x and abs(self.ball.center.y - self.paddle.center.y) < too_close_y):
            # we are too close and moving right, this is a hit!
            self.ball.bounce_vertical()

    def check_hit_brick(self):
        too_close_x = (PADDLE_WIDTH / 2) + BALL_RADIUS
        too_close_y = (PADDLE_HEIGHT / 2) + BALL_RADIUS
        # Beginning of the first row
        if self.filled1.alive:
            if (abs(self.ball.center.x - self.filled1.center.x ) < too_close_x and abs(self.ball.center.y - self.filled1.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled1.alive = False

        if self.filled2.alive:
            if (abs(self.ball.center.x - self.filled2.center.x ) < too_close_x and abs(self.ball.center.y - self.filled2.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled2.alive = False

        if self.filled3.alive:
            if (abs(self.ball.center.x - self.filled3.center.x ) < too_close_x and abs(self.ball.center.y - self.filled3.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled3.alive = False

        if self.filled4.alive:
            if (abs(self.ball.center.x - self.filled4.center.x ) < too_close_x and abs(self.ball.center.y - self.filled4.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled4.alive = False

        if self.filled5.alive:
            if (abs(self.ball.center.x - self.filled5.center.x ) < too_close_x and abs(self.ball.center.y - self.filled5.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled5.alive = False

        if self.filled6.alive:
            if (abs(self.ball.center.x - self.filled6.center.x ) < too_close_x and abs(self.ball.center.y - self.filled6.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled6.alive = False

        if self.filled7.alive:
            if (abs(self.ball.center.x - self.filled7.center.x ) < too_close_x and abs(self.ball.center.y - self.filled7.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled7.alive = False

        if self.filled8.alive:
            if (abs(self.ball.center.x - self.filled8.center.x ) < too_close_x and abs(self.ball.center.y - self.filled8.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled8.alive = False

        if self.filled9.alive:
            if (abs(self.ball.center.x - self.filled9.center.x ) < too_close_x and abs(self.ball.center.y - self.filled9.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled9.alive = False

        if self.filled10.alive:
            if (abs(self.ball.center.x - self.filled10.center.x ) < too_close_x and abs(self.ball.center.y - self.filled10.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled10.alive = False

        # Last brick in the first row
        if self.filled11.alive:
            if (abs(self.ball.center.x - self.filled11.center.x ) < too_close_x and abs(self.ball.center.y - self.filled11.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled11.alive = False

        # First brick in the third row
        if self.filled1_2.alive:
            if (abs(self.ball.center.x - self.filled1_2.center.x ) < too_close_x and abs(self.ball.center.y - self.filled1_2.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled1_2.alive = False

        if self.filled2_2.alive:
            if (abs(self.ball.center.x - self.filled2_2.center.x ) < too_close_x and abs(self.ball.center.y - self.filled2_2.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled2_2.alive = False

        if self.filled3_2.alive:
            if (abs(self.ball.center.x - self.filled3_2.center.x ) < too_close_x and abs(self.ball.center.y - self.filled3_2.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled3_2.alive = False

        if self.filled4_2.alive:
            if (abs(self.ball.center.x - self.filled4_2.center.x ) < too_close_x and abs(self.ball.center.y - self.filled4_2.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled4_2.alive = False

        if self.filled5_2.alive:
            if (abs(self.ball.center.x - self.filled5_2.center.x ) < too_close_x and abs(self.ball.center.y - self.filled5_2.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled5_2.alive = False

        if self.filled6_2.alive:
            if (abs(self.ball.center.x - self.filled6_2.center.x ) < too_close_x and abs(self.ball.center.y - self.filled6_2.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled6_2.alive = False

        if self.filled7_2.alive:
            if (abs(self.ball.center.x - self.filled7_2.center.x ) < too_close_x and abs(self.ball.center.y - self.filled7_2.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled7_2.alive = False

        if self.filled8_2.alive:
            if (abs(self.ball.center.x - self.filled8_2.center.x ) < too_close_x and abs(self.ball.center.y - self.filled8_2.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled8_2.alive = False

        if self.filled9_2.alive:
            if (abs(self.ball.center.x - self.filled9_2.center.x ) < too_close_x and abs(self.ball.center.y - self.filled9_2.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled9_2.alive = False

        if self.filled10_2.alive:
            if (abs(self.ball.center.x - self.filled10_2.center.x ) < too_close_x and abs(self.ball.center.y - self.filled10_2.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled10_2.alive = False

        # Last brick in the second row
        if self.filled11_2.alive:
            if (abs(self.ball.center.x - self.filled11_2.center.x ) < too_close_x and abs(self.ball.center.y - self.filled11_2.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled11_2.alive = False

        # Beginning of the third row
        if self.filled1_3.alive:
            if (abs(self.ball.center.x - self.filled1_3.center.x ) < too_close_x and abs(self.ball.center.y - self.filled1_3.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled1_3.alive = False

        if self.filled2_3.alive:
            if (abs(self.ball.center.x - self.filled2_3.center.x ) < too_close_x and abs(self.ball.center.y - self.filled2_3.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled2_3.alive = False

        if self.filled3_3.alive:
            if (abs(self.ball.center.x - self.filled3_3.center.x ) < too_close_x and abs(self.ball.center.y - self.filled3_3.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled3_3.alive = False

        if self.filled4_3.alive:
            if (abs(self.ball.center.x - self.filled4_3.center.x ) < too_close_x and abs(self.ball.center.y - self.filled4_3.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled4_3.alive = False

        if self.filled5_3.alive:
            if (abs(self.ball.center.x - self.filled5_3.center.x ) < too_close_x and abs(self.ball.center.y - self.filled5_3.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled5_3.alive = False

        if self.filled6_3.alive:
            if (abs(self.ball.center.x - self.filled6_3.center.x ) < too_close_x and abs(self.ball.center.y - self.filled6_3.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled6_3.alive = False

        if self.filled7_3.alive:
            if (abs(self.ball.center.x - self.filled7_3.center.x ) < too_close_x and abs(self.ball.center.y - self.filled7_3.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled7_3.alive = False

        if self.filled8_3.alive:
            if (abs(self.ball.center.x - self.filled8_3.center.x ) < too_close_x and abs(self.ball.center.y - self.filled8_3.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled8_3.alive = False

        if self.filled9_3.alive:
            if (abs(self.ball.center.x - self.filled9_3.center.x ) < too_close_x and abs(self.ball.center.y - self.filled9_3.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled9_3.alive = False

        if self.filled10_3.alive:
            if (abs(self.ball.center.x - self.filled10_3.center.x ) < too_close_x and abs(self.ball.center.y - self.filled10_3.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled10_3.alive = False

        # Last brick in the second row
        if self.filled11_3.alive:
            if (abs(self.ball.center.x - self.filled11_3.center.x ) < too_close_x and abs(self.ball.center.y - self.filled11_3.center.y) < too_close_y):
                self.ball.bounce_vertical()
                self.score += 1
                self.filled11_3.alive = False

    def cleanup_zombies(self):
        for brick in self.bricks:
            if not brick.alive:
                self.bricks.remove(brick)
        row_one = len(self.bricks)

        for brick in self.bricks_2:
            if not brick.alive:
                self.bricks_2.remove(brick)

        row_two = len(self.bricks_2)

        for brick in self.bricks_3:
            if not brick.alive:
                self.bricks_3.remove(brick)

        row_three = len(self.bricks_3)

        total = row_one + row_two + row_three
        if total == 0:
            exit()

    def check_miss(self):
        """
        Checks to see if the ball went past the paddle
        and if so, restarts it.
        """
        if self.ball.center.y < 0:
            # We missed!
            self.ball.restart()

    def check_bounce(self):
        """
        Checks to see if the ball has hit the borders
        of the screen and if so, calls its bounce methods.
        """
        #Bounce off the left wall
        if self.ball.center.x < BALL_RADIUS and self.ball.velocity.dx < 0:
            self.ball.bounce_horizontal()

        #Bounce off the top
        if self.ball.center.y > SCREEN_HEIGHT - BALL_RADIUS and self.ball.velocity.dy > 0:
            self.ball.bounce_vertical()

        #Bounce off the right wall
        if self.ball.center.x > SCREEN_WIDTH - BALL_RADIUS and self.ball.velocity.dx > 0:
            self.ball.bounce_horizontal()

    def check_keys(self):
        """
        Checks to see if the user is holding down an
        arrow key, and if so, takes appropriate action.
        """
        if self.holding_left:
            self.paddle.move_left()

        if self.holding_right:
            self.paddle.move_right()

    def on_key_press(self, key, key_modifiers):
        """
        Called when a key is pressed. Sets the state of
        holding an arrow key.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key == arcade.key.LEFT or key == arcade.key.DOWN:
            self.holding_left = True

        if key == arcade.key.RIGHT or key == arcade.key.UP:
            self.holding_right = True

    def on_key_release(self, key, key_modifiers):
        """
        Called when a key is released. Sets the state of
        the arrow key as being not held anymore.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key == arcade.key.LEFT or key == arcade.key.DOWN:
            self.holding_left = False

        if key == arcade.key.RIGHT or key == arcade.key.UP:
            self.holding_right = False

# Creates the game and starts it going
window = Breakout(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()