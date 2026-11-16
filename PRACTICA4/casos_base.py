from datetime import date
from sistema_academico import *

umsa = Universidad("UMSA")
informatica = umsa.crear_carrera("Informática")
sistemas = umsa.crear_carrera("Sistemas")
docente = Docente("Ana Alba", "1234567", "Ingeniería de Software")
d2 = Docente("Luis Rojas", "999", "Redes")

print("--- Caso 1: doble inscripción")
poo = Materia("INF-121", 6)
e1 = Estudiante("Carlos Flores", "7654321", "E-001")
e1.inscribirse(poo)
e1.inscribirse(poo)
print(docente.generar_acta(poo))

print("--- Caso 2: dos docentes en un curso")
poo = Materia("INF-121", 6)
docente.dictar(poo)
d2.dictar(poo)
print("poo.docente           =", poo.docente.nombre)
print("docente.materias tiene poo:", poo in docente.materias)
print("d2.materias tiene poo     :", poo in d2.materias)

print("--- Caso 3: nota sin registrar")
poo = Materia("INF-121", 6)
i = e1.inscribirse(poo)
print("calcular_nota() =", i.calcular_nota())

print("--- Caso 4: docente en dos carreras")
informatica.agregar_docente(docente)
sistemas.agregar_docente(docente)
informatica.agregar_docente(docente)
print("Informática:", [d.nombre for d in informatica.docentes])
print("Sistemas   :", [d.nombre for d in sistemas.docentes])

print("--- Caso 5: composición no estricta")
h = Horario(date(2026, 7, 16), "Aula 5")
falsa = Carrera("Falsa")
print("Horario suelto creado:", h.aula, "| Carrera suelta:", falsa.nombre)
print("Carreras de UMSA:", [c.nombre for c in umsa.carreras])
