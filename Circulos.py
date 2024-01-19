"""Escriba un programa que reciba como entrada el radio de un círculo
y entregue como salida su perímetro y su área:"""

from math import pi
radius = float(input('Ingrese el radio: '))
P=2*pi*radius
A=pi*radius**2
print(f'Perimetro: {P}')
print(f'Área: {A}')