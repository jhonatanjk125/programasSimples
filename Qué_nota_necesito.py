grade_1 = float(input('Ingrese nota del examen 1:'))
grade_2 = float(input('Ingrese nota del examen 2:'))
grade_lab = float(input('Ingrese nota del laboratorio:'))

Nc = (10*60-3*grade_lab)/7
C3 = 3*Nc-grade_1-grade_2

print(f'Necesita nota {C3} en el examen 3')