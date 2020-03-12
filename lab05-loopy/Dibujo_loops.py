import arcade


def lineas():
    arcade.draw_line(0, 300, 1200, 300, arcade.color.BLACK, 1)
    arcade.draw_line(300, 0, 300, 600, arcade.color.BLACK, 1)
    arcade.draw_line(600, 0, 600, 600, arcade.color.BLACK, 1)
    arcade.draw_line(900, 0, 900, 600, arcade.color.BLACK, 1)


def draw_section_1():
    y = 5
    for row in range(30):
        x = 5
        for column in range(30):
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            x += 10

        y += 10


def draw_section_2():
    y = 5
    for row in range(30):
        x = 305
        for column in range(30):
            if column%2 != 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            x += 10

        y += 10


def draw3():
    y = 305
    for row in range(30):
        x = 5
        for column in range(30):
            if row % 2 != 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
            else:
                if column % 2 != 0:
                    arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
                else:
                    arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

            x += 10

        y += 10


def draw4():
    y = 305
    for row in range(30):
        x = 305
        for column in range(30):
            if row % 2 != 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            x += 10

        y += 10

def draw5():
    y = 5
    for row in range(30):
        x = 605
        rango = 30 - row
        for column in range(rango):
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            x += 10

        y += 10


def draw6():
    y = 5
    for row in range(30):
        x = 905 + 10 * row
        rango = 30 - row
        for column in range(rango):
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            x += 10

        y += 10


def draw7():
    y = 305
    for row in range(30):
        x = 600 + 5
        for column in range(row + 1):
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            x += 10

        y += 10


def draw8():
    y = 305
    for row in range(30):
        x = 895 + 10 * (30 - row)
        for column in range(row + 1):
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            x += 10

        y += 10


def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw3()
    draw4()
    draw5()
    draw6()
    draw7()
    draw8()

    # Draw the outlines for the sections
    lineas()

    arcade.finish_render()

    arcade.run()


main()
