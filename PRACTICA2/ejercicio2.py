import math


class AlgebraVectorial:

    # Sobrecarga de constructores
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    # Producto escalar
    def productoEscalar(self, b):
        return self.__x * b.getX() + self.__y * b.getY()

    # Longitud del vector
    def modulo(self):
        return math.sqrt(self.__x ** 2 + self.__y ** 2)

    # Sobrecarga para perpendicular
    def perpendicular(self, *args):

        if len(args) == 1 and isinstance(args[0], AlgebraVectorial):
            b = args[0]

            return self.productoEscalar(b) == 0

        elif len(args) == 2:
            b = AlgebraVectorial(args[0], args[1])

            return self.productoEscalar(b) == 0

        else:
            raise ValueError("Datos incorrectos")

    # Sobrecarga para paralela
    def paralela(self, *args):

        if len(args) == 1 and isinstance(args[0], AlgebraVectorial):
            b = args[0]

        elif len(args) == 2:
            b = AlgebraVectorial(args[0], args[1])

        else:
            raise ValueError("Datos incorrectos")

        determinante = self.__x * b.getY() - self.__y * b.getX()

        return determinante == 0

    # Proyección de a sobre b
    def proyeccion(self, b):

        modulo_b = b.modulo()

        if modulo_b == 0:
            raise ValueError("No se puede proyectar sobre el vector cero")

        producto = self.productoEscalar(b)

        factor = producto / (modulo_b ** 2)

        x = factor * b.getX()
        y = factor * b.getY()

        return AlgebraVectorial(x, y)

    # Componente de a en la dirección de b
    def componente(self, b):

        modulo_b = b.modulo()

        if modulo_b == 0:
            raise ValueError("El vector b no puede ser cero")

        return self.productoEscalar(b) / modulo_b

    def __str__(self):
        return "({}, {})".format(self.__x, self.__y)


# Programa principal

a = AlgebraVectorial(3, 4)
b = AlgebraVectorial(4, -3)

print("Vector a =", a)
print("Vector b =", b)

print("¿Son perpendiculares?", a.perpendicular(b))
print("¿Son paralelos?", a.paralela(b))

print("Producto escalar =", a.productoEscalar(b))

print("Proyección de a sobre b =", a.proyeccion(b))

print("Componente de a en b =", a.componente(b))