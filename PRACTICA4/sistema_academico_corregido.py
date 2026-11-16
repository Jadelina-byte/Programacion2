from abc import ABC, abstractmethod
from datetime import date

# Llave que solo conocen los "Todos" (en un proyecto real vive en su propio módulo)
_LLAVE = object()


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
        for i in self._inscripciones:
            if i.materia is materia:
                raise ValueError(
                    f"{self.nombre} ya está inscrito en {materia.codigo}")
        inscripcion = Inscripcion(self, materia, date.today())
        self._inscripciones.append(inscripcion)
        materia._registrar_inscripcion(inscripcion)
        return inscripcion

    @property
    def inscripciones(self):
        return tuple(self._inscripciones)

    def __str__(self):
        return f"Estudiante {self.nombre} (código {self._codigo})"


class Ayudante(Estudiante):
    """Herencia: un ayudante ES un estudiante. Asociación: colabora con un docente."""

    def __init__(self, nombre, ci, codigo):
        super().__init__(nombre, ci, codigo)
        self._docente = None

    def colaborar_con(self, docente):
        if self._docente is not None:
            raise ValueError(f"{self.nombre} ya colabora con un docente")
        self._docente = docente
        docente._agregar_ayudante(self)

    @property
    def docente(self):
        return self._docente

    def __str__(self):
        return f"Ayudante {self.nombre} (código {self.codigo})"


class Docente(Persona):
    def __init__(self, nombre, ci, especialidad):
        super().__init__(nombre, ci)
        self._especialidad = especialidad
        # Asociación: el docente conoce las materias que dicta
        self._materias = []
        self._carrera = None
        self._ayudantes = []

    def dictar(self, materia):
        if materia.docente is not None:
            raise ValueError(f"La materia {materia.codigo} ya tiene docente")
        self._materias.append(materia)
        materia._set_docente(self)

    @property
    def carrera(self):
        return self._carrera

    def _set_carrera(self, carrera):
        self._carrera = carrera

    def _agregar_ayudante(self, ayudante):
        self._ayudantes.append(ayudante)

    @property
    def ayudantes(self):
        return tuple(self._ayudantes)

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
        carrera = Carrera(nombre_carrera, _LLAVE)
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
    def __init__(self, nombre, _llave=None):
        if _llave is not _LLAVE:
            raise TypeError("Una Carrera solo la crea una Universidad")
        self._nombre = nombre
        self._docentes = []

    # La Carrera AGREGA a las partes ya existentes
    def agregar_docente(self, docente):
        if docente.carrera is not None:
            raise ValueError(
                f"{docente.nombre} ya pertenece a {docente.carrera.nombre}")
        self._docentes.append(docente)
        docente._set_carrera(self)

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
        horario = Horario(fecha, aula, _LLAVE)
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
    def __init__(self, fecha, aula, _llave=None):
        if _llave is not _LLAVE:
            raise TypeError("Un Horario solo lo crea una Materia")
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
        self._nota = None   # None = aún sin calificar

    def registrar_nota(self, nota):
        if nota < 0 or nota > 100:
            raise ValueError("La nota debe estar entre 0 y 100")
        self._nota = float(nota)

    def esta_calificada(self):
        return self._nota is not None

    def calcular_nota(self):
        if self._nota is None:
            raise ValueError("La inscripción aún no tiene nota")
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
            nota = i.calcular_nota() if i.esta_calificada() else "SIN NOTA"
            lineas.append(f"  {i.estudiante.nombre}: {nota}")
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

    # Ayudante: es un Estudiante (herencia) y colabora con un Docente (asociación)
    ay = Ayudante("Pedro Quispe", "7654323", "E-003")
    ay.colaborar_con(docente)
    ay.inscribirse(poo)
    print(ay, "-> colabora con", ay.docente.nombre)
    print("Ayudantes de", docente.nombre, ":", [a.nombre for a in docente.ayudantes])


if __name__ == "__main__":
    main()
