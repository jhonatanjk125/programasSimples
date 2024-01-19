"""Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:"""
sum=0
n=4
for i in range(n):
    current_grade=float(input(f'Por favor ingrese la nota {i+1}:'))
    sum+=current_grade
print(f'El promedio es: {sum/n}')