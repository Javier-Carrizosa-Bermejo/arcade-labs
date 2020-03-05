import arcade
import random


# Para dibujar rectángulos, se marca por ejemplo, de 0 a 400 en el eje x y de 20 a 60 en el eje y Para dibujar

# circulos se marca el centro mediante coordenadas x-y, se marca el radio, color y para hacer figuras geometricas se
# pone número de segmentos/lados

# para parábolas, se marca el comienzo en el eje x, el comienzo en el eje y, el final del eje x, altura, color y ángulo
# en el caso de outline, igual pero marcas el grosos al final con un número

# Para dibujar polígonos, se marcan los puntos mediante coordenadas x-y en una tupla  y se marca el color


def estrellas():
    num_estrellas = random.randint(50, 100)

    for i in range(num_estrellas):
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        arcade.draw_circle_filled(x, y, 3, arcade.color.BLUE, 10)


def tormentrper():
    # Figura principal
    arcade.draw_polygon_filled([[100, 200], [150, 300], [650, 300], [700, 200], [500, 30], [300, 30]],
                               arcade.color.WHITE_SMOKE)

    # Bandana negra y casco
    arcade.draw_lrtb_rectangle_filled(150, 650, 350, 300, arcade.color.WHITE_SMOKE)
    arcade.draw_lrtb_rectangle_filled(150, 650, 340, 320, arcade.color.BLACK)

    # Ojos verdes
    arcade.draw_polygon_filled([[200, 250], [230, 290], [350, 270], [290, 250]], arcade.color.GREEN_YELLOW)
    arcade.draw_polygon_filled([[510, 250], [450, 270], [570, 290], [600, 250]], arcade.color.GREEN_YELLOW)

    # Boca negra
    arcade.draw_polygon_filled([[330, 30], [375, 90], [425, 90], [470, 30]], arcade.color.BLACK)

    # Círculo de la boca
    arcade.draw_circle_filled(300, 80, 30, arcade.color.BLACK, 8)
    arcade.draw_circle_filled(500, 80, 30, arcade.color.BLACK, 8)

    # Decorado del casco
    arcade.draw_polygon_filled([[120, 210], [180, 220], [250, 130], [190, 140]], arcade.color.BLACK)
    arcade.draw_polygon_filled([[680, 210], [620, 220], [550, 130], [610, 140]], arcade.color.BLACK)
    arcade.draw_polygon_filled([[360, 320], [440, 320], [420, 210], [380, 210]], arcade.color.BLACK)

    # Frente y cabeza
    arcade.draw_parabola_filled(150, -50, 650, 400, arcade.color.WHITE_SMOKE, 0)

    # Boca
    arcade.draw_parabola_outline(280, 0, 520, 120, arcade.color.BLACK, 40)


def nave(x):
    arcade.draw_circle_filled(x + 10, 400, 10, arcade.color.RED, 3)


def arte():
    nave(arte.contador)
    if arte.contador >= 785:
        arte.derecha = False
    elif arte.contador <= 25:
        arte.derecha = True

    if arte.derecha:
        arte.contador += 10
    else:
        arte.contador -= 10


arte.contador = 3
arte.derecha = True


def dibujo(delta_time):
    arcade.start_render()
    estrellas()
    tormentrper()
    arte()


juego = arcade.Window(799, 600, "Drawing Example")
arcade.set_background_color(arcade.color.BLACK)
arcade.schedule(dibujo, 1 / 30) #schedule runea x veces por segundo la función del primer argumento
arcade.run()
