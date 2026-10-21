
class Sensor:
    tipo = "Genérico"

    def __init__(self, id):
        self.id = id
        self.encendido = False

    def activar(self):
        self.encendido = True
        print(self.tipo, self.id, "activado")

    def desactivar(self):
        self.encendido = False
        print(self.tipo, self.id, "desactivado")


class Camara(Sensor):
    tipo = "Cámara"

    def __init__(self, id, resolucion):
        Sensor.__init__(self, id)
        self.resolucion = resolucion


class SensorLuzLaser(Sensor):
    tipo = "Luz Laser"

    def __init__(self, id, alcance):
        Sensor.__init__(self, id)
        self.alcance = alcance


class VehiculoAutonomo(Camara, SensorLuzLaser):
    tipo = "Vehículo Autónomo"

    def __init__(self, id, resolucion, alcance):
        Sensor.__init__(self, id)
        self.resolucion = resolucion
        self.alcance = alcance

    def mostrarDatos(self):
        print("\n--- DATOS DEL VEHICULO AUTONOMO ---")
        print("Tipo:", self.tipo)
        print("ID:", self.id)
        print("Resolucion de camara:", self.resolucion)
        print("Alcance del sensor laser:", self.alcance)
        print("Encendido:", self.encendido)


class Aplicacion:
    @staticmethod
    def main():
        vehiculo = VehiculoAutonomo("VA001", "1920x1080", 100)

        vehiculo.mostrarDatos()

        print("\n--- ACTIVACION ---")
        vehiculo.activar()
        vehiculo.mostrarDatos()

        print("\n--- DESACTIVACION ---")
        vehiculo.desactivar()
        vehiculo.mostrarDatos()


if __name__ == "__main__":
    Aplicacion.main()
