from datetime import date
from sistema_academico_corregido import *

def intentar(titulo, f):
    try:
        f()
        print(f"{titulo}: SIN ERROR (inconsistente)")
    except Exception as ex:
        print(f"{titulo}: {type(ex).__name__}: {ex}")

umsa = Universidad("UMSA")
informatica = umsa.crear_carrera("Informática")
sistemas = umsa.crear_carrera("Sistemas")
docente = Docente("Ana Alba", "1234567", "Ingeniería de Software")
d2 = Docente("Luis Rojas", "999", "Redes")
e1 = Estudiante("Carlos Flores", "7654321", "E-001")
poo = Materia("INF-121", 6)

e1.inscribirse(poo)
intentar("Caso 1 doble inscripción ", lambda: e1.inscribirse(poo))

docente.dictar(poo)
intentar("Caso 2 dos docentes      ", lambda: d2.dictar(poo))

i = e1.inscripciones[0]
intentar("Caso 3 nota sin registrar", lambda: i.calcular_nota())
print(docente.generar_acta(poo))

informatica.agregar_docente(docente)
intentar("Caso 4 docente 2 carreras", lambda: sistemas.agregar_docente(docente))

intentar("Caso 5a Horario suelto   ", lambda: Horario(date(2026, 7, 16), "Aula 5"))
intentar("Caso 5b Carrera suelta   ", lambda: Carrera("Falsa"))
