from abc import ABC, abstractmethod
from datetime import date


# ---------------------------------------------------------
# Herencia: Persona (abstracta) <- Estudiante, Docente
# ---------------------------------------------------------
class Persona(ABC):
    def __init__(self, nombre, ci):
        self._nombre = nombre
        self._ci = ci

    @property
    def nombre(self):
        return self._nombre

    @property
    def ci(self):
        return self._ci

    @abstractmethod
    def __str__(self):
        ...


class Estudiante(Persona):
    def __init__(self, nombre, ci, codigo):
        super().__init__(nombre, ci)
        self._codigo = codigo
        # Asociación: el estudiante conoce sus inscripciones
        self._inscripciones = []

    @property
    def codigo(self):
        return self._codigo

    def inscribirse(self, materia):
        inscripcion = Inscripcion(self, materia, date.today())
        self._inscripciones.append(inscripcion)
        materia._registrar_inscripcion(inscripcion)
        return inscripcion

    @property
    def inscripciones(self):
        return tuple(self._inscripciones)

    def __str__(self):
        return f"Estudiante {self.nombre} (código {self._codigo})"


class Docente(Persona):
    def __init__(self, nombre, ci, especialidad):
        super().__init__(nombre, ci)
        self._especialidad = especialidad
        # Asociación: el docente conoce las materias que dicta
        self._materias = []

    def dictar(self, materia):
        self._materias.append(materia)
        materia._set_docente(self)

    # Dependencia: Acta se crea y se devuelve, pero NO se guarda como atributo
    def generar_acta(self, materia):
        return Acta(materia)

    @property
    def materias(self):
        return tuple(self._materias)

    def __str__(self):
        return f"Docente {self.nombre} ({self._especialidad})"


# ---------------------------------------------------------
# Composición: Universidad -> Carrera
# ---------------------------------------------------------
class Universidad:
    def __init__(self, nombre):
        self._nombre = nombre
        self._carreras = []

    # La Universidad CREA a las partes (carreras)
    def crear_carrera(self, nombre_carrera):
        carrera = Carrera(nombre_carrera)
        self._carreras.append(carrera)
        return carrera

    @property
    def nombre(self):
        return self._nombre

    @property
    def carreras(self):
        return tuple(self._carreras)


# ---------------------------------------------------------
# Agregación: Carrera -> Docente
# ---------------------------------------------------------
class Carrera:
    def __init__(self, nombre):
        self._nombre = nombre
        self._docentes = []

    # La Carrera AGREGA a las partes ya existentes
    def agregar_docente(self, docente):
        self._docentes.append(docente)

    @property
    def nombre(self):
        return self._nombre

    @property
    def docentes(self):
        return tuple(self._docentes)


# ---------------------------------------------------------
# Composición: Materia -> Horario
# ---------------------------------------------------------
class Materia:
    def __init__(self, codigo, creditos):
        self._codigo = codigo
        self._creditos = creditos
        self._docente = None
        self._horarios = []
        self._inscripciones = []

    def agregar_horario(self, fecha, aula):
        horario = Horario(fecha, aula)
        self._horarios.append(horario)
        return horario

    def _registrar_inscripcion(self, inscripcion):
        self._inscripciones.append(inscripcion)

    def _set_docente(self, docente):
        self._docente = docente

    @property
    def codigo(self):
        return self._codigo

    @property
    def creditos(self):
        return self._creditos

    @property
    def docente(self):
        return self._docente

    @property
    def horarios(self):
        return tuple(self._horarios)

    @property
    def inscripciones(self):
        return tuple(self._inscripciones)


class Horario:
    def __init__(self, fecha, aula):
        self._fecha = fecha
        self._aula = aula

    @property
    def fecha(self):
        return self._fecha

    @property
    def aula(self):
        return self._aula


# ---------------------------------------------------------
# Inscripcion implementa Calificable
# ---------------------------------------------------------
class Calificable(ABC):
    @abstractmethod
    def calcular_nota(self):
        ...


class Inscripcion(Calificable):
    def __init__(self, estudiante, materia, fecha):
        self._estudiante = estudiante
        self._materia = materia
        self._fecha = fecha
        self._nota = 0.0

    def registrar_nota(self, nota):
        if nota < 0 or nota > 100:
            raise ValueError("La nota debe estar entre 0 y 100")
        self._nota = float(nota)

    def calcular_nota(self):
        return self._nota

    @property
    def estudiante(self):
        return self._estudiante

    @property
    def materia(self):
        return self._materia

    @property
    def fecha(self):
        return self._fecha


# ---------------------------------------------------------
# Dependencia: Docente usa Acta de forma temporal
# ---------------------------------------------------------
class Acta:
    def __init__(self, materia):
        self._fecha = date.today()
        lineas = [f"ACTA {materia.codigo} - {self._fecha}"]
        for i in materia.inscripciones:
            lineas.append(f"  {i.estudiante.nombre}: {i.calcular_nota()}")
        self._contenido = "\n".join(lineas)

    def __str__(self):
        return self._contenido


def main():
    # Composición: la Universidad crea sus Carreras
    umsa = Universidad("UMSA")
    informatica = umsa.crear_carrera("Informática")

    # Agregación: los Docentes existen antes e independientemente
    docente = Docente("Ana Alba", "1234567", "Ingeniería de Software")
    informatica.agregar_docente(docente)

    # Asociación: el Docente dicta una Materia
    poo = Materia("INF-121", 6)
    docente.dictar(poo)

    # Composición: la Materia crea sus Horarios
    poo.agregar_horario(date(2026, 7, 2), "Aula 101")
    poo.agregar_horario(date(2026, 7, 9), "Aula 101")

    # Asociación entre Estudiante e Inscripcion
    e1 = Estudiante("Carlos Flores", "7654321", "E-001")
    e2 = Estudiante("Maria Salas", "7654322", "E-002")
    i1 = e1.inscribirse(poo)
    i2 = e2.inscribirse(poo)
    i1.registrar_nota(85)
    i2.registrar_nota(92)

    # Herencia + polimorfismo
    personas = [docente, e1, e2]
    for p in personas:
        print(p)

    # La inscripción se usa a través de la interfaz Calificable
    c = i1
    print(f"Nota de {e1.nombre}: {c.calcular_nota()}")

    # Dependencia: el Docente usa Acta solo dentro de un método
    acta = docente.generar_acta(poo)
    print(acta)


if __name__ == "__main__":
    main()
