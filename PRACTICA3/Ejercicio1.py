import random
class Juego:
    def __init__(self, vidas):
        self.numeroDeVidas = vidas
        self.record = 0

    def reiniciaPartida(self):
        self.numeroDeVidas = self.vidasIniciales

    def actualizaRecord(self):
        vidasUsadas = self.vidasIniciales - self.numeroDeVidas

        if self.record == 0 or vidasUsadas < self.record:
            self.record = vidasUsadas

        print("Record actualizado:", self.record, "intentos")

    def quitaVida(self):
        self.numeroDeVidas -= 1
        print("Vidas restantes:", self.numeroDeVidas)
        return self.numeroDeVidas > 0

class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.vidasIniciales = vidas
        self.numeroAAdivinar = 0

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)

        while self.numeroDeVidas > 0:
            try:
                numero = int(input("Adivina un numero entre 0 y 10: "))
            except ValueError:
                print("Debes ingresar un numero entero.")
                continue

            if numero < 0 or numero > 10:
                print("El numero debe estar entre 0 y 10.")
                continue

            if numero == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                return

            if not self.quitaVida():
                print("Te quedaste sin vidas.")
                print("El numero era:", self.numeroAAdivinar)
                return

            if numero < self.numeroAAdivinar:
                print("El numero a adivinar es mayor.")
            else:
                print("El numero a adivinar es menor.")

class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(3)
        juego.juega()

if __name__ == "__main__":
    Aplicacion.main()
