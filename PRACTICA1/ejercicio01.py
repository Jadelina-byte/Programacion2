import time
import random

class Cronometro:
    
    def __init__(self):
        self.__inicia = time.time() * 1000
        self.__finaliza = None

    def getInicia(self):
        return self.__inicia

    def getFinaliza(self):
        return self.__finaliza

    def inicia(self):
        self.__inicia = time.time() * 1000

    def detener(self):
        self.__finaliza = time.time() * 1000

    def lapsoDeTiempo(self):
        return self.__finaliza - self.__inicia


def seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]


# PROGRAMA PRINCIPAL
numeros = [random.randint(1, 100000) for _ in range(100000)]

crono = Cronometro()
crono.inicia()

seleccion(numeros)

crono.detener()

print("Tiempo en milisegundos:", crono.lapsoDeTiempo())