Algoritmo queNotaNecesito
	Escribir "Ingrese la nota del examen 1: "
	Leer grade_1
	Escribir "Ingrese la nota del examen 2: "
	Leer grade_2
	Escribir "Ingrese la nota del laboratorio: "
	Leer grade_lab
	Nc = (10*60-3*grade_lab)/7
	C3 = 3*Nc-grade_1-grade_2
	Escribir "Necesita nota ", C3, " en el examen 3"
FinAlgoritmo
