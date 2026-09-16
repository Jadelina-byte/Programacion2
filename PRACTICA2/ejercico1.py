import math


class MiPunto:

    # Constructor
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    # Getter de x
    def getX(self):
        return self.__x

    # Getter de y
    def getY(self):
        return self.__y

    # Distancia usando otro objeto MiPunto
    def distancia(self, *args):

        if len(args) == 1 and isinstance(args[0], MiPunto):
            p = args[0]

            dx = p.getX() - self.__x
            dy = p.getY() - self.__y

        # Distancia usando coordenadas x e y
        elif len(args) == 2:
            x = args[0]
            y = args[1]

            dx = x - self.__x
            dy = y - self.__y

        else:
            raise ValueError("Datos incorrectos")

        return math.sqrt(dx ** 2 + dy ** 2)


# Programa de prueba

p1 = MiPunto()
p2 = MiPunto(10, 30.5)

print("Punto 1:", p1.getX(), ",", p1.getY())
print("Punto 2:", p2.getX(), ",", p2.getY())

print("Distancia usando objeto:")
print(p1.distancia(p2))

print("Distancia usando coordenadas:")
print(p1.distancia(10, 30.5))