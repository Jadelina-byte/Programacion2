import random


class Juego:
    def __init__(self, vidas):
        self.vidasIniciales = vidas
        self.numeroDeVidas = vidas
        self.record = 0

    def reiniciaPartida(self):
        self.numeroDeVidas = self.vidasIniciales

    def actualizaRecord(self):
        intentos = self.vidasIniciales - self.numeroDeVidas

        if self.record == 0 or intentos < self.record:
            self.record = intentos

        print("Record:", self.record, "intentos fallidos")

    def quitaVida(self):
        self.numeroDeVidas -= 1
        print("Vidas restantes:", self.numeroDeVidas)
        return self.numeroDeVidas > 0


class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAAdivinar = 0

    def validaNumero(self, numero):
        return 0 <= numero <= 10

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)

        while self.numeroDeVidas > 0:
            try:
                numero = int(input("Adivina un numero entre 0 y 10: "))
            except ValueError:
                print("Ingresa un numero entero.")
                continue

            if not self.validaNumero(numero):
                print("Numero fuera del intervalo 0-10.")
                continue

            if numero == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                return

            if not self.quitaVida():
                print("Perdiste. El numero era:", self.numeroAAdivinar)
                return

            if numero < self.numeroAAdivinar:
                print("El numero secreto es mayor.")
            else:
                print("El numero secreto es menor.")


class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if not 0 <= numero <= 10:
            print("Error: el numero debe estar entre 0 y 10.")
            return False

        if numero % 2 != 0:
            print("Error: debes ingresar un numero par.")
            return False

        return True


class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if not 0 <= numero <= 10:
            print("Error: el numero debe estar entre 0 y 10.")
            return False

        if numero % 2 == 0:
            print("Error: debes ingresar un numero impar.")
            return False

        return True


class Aplicacion:
    @staticmethod
    def main():
        juego1 = JuegoAdivinaNumero(3)
        juego2 = JuegoAdivinaPar(3)
        juego3 = JuegoAdivinaImpar(3)

        print("\n--- JUEGO DE NUMERO ---")
        juego1.juega()

        print("\n--- JUEGO DE NUMERO PAR ---")
        juego2.juega()

        print("\n--- JUEGO DE NUMERO IMPAR ---")
        juego3.juega()


if __name__ == "__main__":
    Aplicacion.main()
