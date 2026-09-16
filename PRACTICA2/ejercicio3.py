import math


class Vector3D:

    # Constructor
    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z

    # Getters
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getZ(self):
        return self.__z

    # Sobrecarga del operador +
    def __add__(self, b):
        return Vector3D(
            self.__x + b.getX(),
            self.__y + b.getY(),
            self.__z + b.getZ()
        )

    # Sobrecarga del operador *
    def __mul__(self, r):

        if isinstance(r, (int, float)):
            return Vector3D(
                r * self.__x,
                r * self.__y,
                r * self.__z
            )

        raise ValueError("Solo se puede multiplicar por un escalar")

    # Permite escalar * vector
    def __rmul__(self, r):
        return self.__mul__(r)

    # Longitud del vector
    def longitud(self):
        return math.sqrt(
            self.__x ** 2 +
            self.__y ** 2 +
            self.__z ** 2
        )

    # Normal del vector
    def normal(self):

        longitud = self.longitud()

        if longitud == 0:
            raise ValueError("El vector cero no tiene normal")

        return Vector3D(
            self.__x / longitud,
            self.__y / longitud,
            self.__z / longitud
        )

    # Sobrecarga de @ para producto escalar
    def __matmul__(self, b):

        return (
            self.__x * b.getX() +
            self.__y * b.getY() +
            self.__z * b.getZ()
        )

    # Sobrecarga de ^ para producto vectorial
    def __xor__(self, b):

        x = self.__y * b.getZ() - self.__z * b.getY()

        y = self.__z * b.getX() - self.__x * b.getZ()

        z = self.__x * b.getY() - self.__y * b.getX()

        return Vector3D(x, y, z)

    def __str__(self):

        return "({}, {}, {})".format(
            self.__x,
            self.__y,
            self.__z
        )


# Programa de prueba

a = Vector3D(1, 2, 3)
b = Vector3D(4, 5, 6)

print("Vector a =", a)
print("Vector b =", b)

# Suma
print("a + b =", a + b)

# Multiplicación por escalar
print("2 * a =", 2 * a)

# Longitud
print("|a| =", a.longitud())

# Normal
print("Normal de a =", a.normal())

# Producto escalar
print("a . b =", a @ b)

# Producto vectorial
print("a x b =", a ^ b)