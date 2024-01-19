"""Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario."""

number = float(input('Ingrese un numero: '))
decimal_part = number - number//1
print(f'{decimal_part}')