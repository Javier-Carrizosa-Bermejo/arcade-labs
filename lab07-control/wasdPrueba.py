import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED_iz = 5
MOVEMENT_SPEED_de = 5
MOVEMENT_SPEED_up = 5
MOVEMENT_SPEED_down = 5


def tormentrper():
    lista = arcade.ShapeElementList()
    arcade.set_background_color(arcade.color.BLACK)
    # Figura principal
    lista.append(arcade.create_polygon([[100, 200], [150, 300], [650, 300], [700, 200], [500, 30], [300, 30]],
                                       arcade.color.WHITE_SMOKE))

    lista.append(arcade.create_polygon([[500, 400], [350, 300], [650, 300], [700, 200], [500, 30], [300, 30]],
                                       arcade.color.GREEN))

    lista.append(arcade.create_polygon([[230, 500], [50, 30], [65, 30], [70, 20], [50, 30], [30, 30]],
                                       arcade.color.YELLOW))

    return lista


class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        # Move the ball
        if self.position_x > 800:
            self.position_x = 800
        elif self.position_x < 0:
            self.position_x = 0
        if self.position_y > 600:
            self.position_y = 600
        elif self.position_y < 0:
            self.position_y = 0
        self.position_x += self.change_x
        print(self.position_x)
        self.position_y += self.change_y


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.

        # Create our ball
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.AUBURN)

    def seetup(self):
        self.fuck = tormentrper()

    def on_draw(self):
        arcade.start_render()
        self.fuck.draw()
        self.ball.draw()

    def update(self, delta_time):
        self.ball.update()


    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.A:
            self.ball.change_x = -5
            print("pulsando tecla")
        elif key == arcade.key.D:
            self.ball.change_x = MOVEMENT_SPEED_de
        elif key == arcade.key.W:
            self.ball.change_y = MOVEMENT_SPEED_down
        elif key == arcade.key.S:
            self.ball.change_y = -MOVEMENT_SPEED_up

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.A or key == arcade.key.D:
            self.ball.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.ball.change_y = 0


def main():
    window = MyGame()
    window.seetup()
    arcade.run()


main()
