"""
Escriba un programa que reciba como entrada la temperatura original del huevo y 
muestre como salida el tiempo en segundos que le toma alcanzar la temperatura máxima para prepararlo a la copa.
"""
from math import pi,log

m = float(input('Inserte la masa en gramos del huevo: '))
To = float(input('Inserte la temperatura original del huevo: '))

t = ((m**(2/3)*3.7*(1.038**(1/3)))/(0.0054*pi*pi*(4*pi/3)**(2/3)))*log(0.76*((To-100)/(70-100)))

print(f'El tiempo requerido es: {t} s')
