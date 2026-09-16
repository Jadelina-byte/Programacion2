import random
import time


class Cronometro:
    def __init__(self):
        self.__inicia = time.time()
        self.__finaliza = None

    def getInicia(self):
        return self.__inicia

    def getFinaliza(self):
        return self.__finaliza

    def inicia(self):
        self.__inicia = time.time()
        self.__finaliza = None

    def detener(self):
        self.__finaliza = time.time()

    def lapsoDeTiempo(self):
        if self.__finaliza is None:
            raise ValueError("Primero debe detener el cronómetro.")
        return (self.__finaliza - self.__inicia) * 1000


def seleccion(lista):
    n = len(lista)
    for i in range(n):
        indice_min = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_min]:
                indice_min = j
        lista[i], lista[indice_min] = lista[indice_min], lista[i]


# PROGRAMA PRINCIPAL
numeros = [random.randint(1, 100000) for _ in range(100000)]

crono = Cronometro()
crono.inicia()
seleccion(numeros)
crono.detener()

print(f"Tiempo de ejecución: {crono.lapsoDeTiempo():.3f} ms")