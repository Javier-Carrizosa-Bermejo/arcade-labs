import arcade
import random


class Prota:  # clase de Rombo persecutor
    pos_inicial_x = 200  # se hacen clases para poder hacer objetos y poder acceder a sus atributos (coordenadas)
    pos_inicial_y = 300  # siempre que se requiera


nave = Prota()


class Enemigo:  # clase de Rombo a perseguir
    pos_principio_x = 300
    pos_principio_y = 200


perse = Enemigo()


def circulo():  # D ibuja rombo persecutor
    arcade.draw_circle_filled(nave.pos_inicial_x, nave.pos_inicial_y, 10, arcade.color.GREEN, 4)


def cuadrao():  # Dibuja rombo perseguido
    arcade.draw_circle_filled(perse.pos_principio_x, perse.pos_principio_y, 10, arcade.color.RED, 4)


def inteligencia(delta_time):
    arcade.start_render()
    cuadrao()  # Se dibuja primero el rombo perseguido
    if nave.pos_inicial_x > perse.pos_principio_x:  # if que declara la posición en x
        nave.pos_inicial_x -= 10

    elif nave.pos_inicial_x < perse.pos_principio_x:
        nave.pos_inicial_x += 10

    elif nave.pos_inicial_x == perse.pos_principio_x:
        None

    if nave.pos_inicial_y > perse.pos_principio_y:  # if que declara la posición en el eje y
        nave.pos_inicial_y -= 10

    elif nave.pos_inicial_y < perse.pos_principio_y:
        nave.pos_inicial_y += 10
    elif nave.pos_inicial_y == perse.pos_principio_y:
        None

    circulo()  # Se dibuja el persecutor tras declarar sus cordenadas x-y, de esta forma se intenta dar la sensación
    # de movimiento diagonal

    if nave.pos_inicial_y == perse.pos_principio_y and nave.pos_inicial_x == perse.pos_principio_x:
        perse.pos_principio_x = (random.randint(10, 790) // 10) * 10
        perse.pos_principio_y = (random.randint(10, 590) // 10) * 10
        # momento en el que coinciden, las coordenadas de nuestro perseguido son reescritas. Siempre multiplos de 10
        # ya que nuestro persecutor se mueve de 10 en 10


juego = arcade.Window(800, 600, "Funciona")
arcade.set_background_color(arcade.color.GRAY)
arcade.schedule(inteligencia, 1 / 60)  # 10 fps, si se ponen más altos va demasiado rápido y no se aprecia
arcade.run()
