"""Escriba un programa que pida al usuario un entero de tres dígitos,
y entregue el número con los dígitos en orden inverso:"""

number = int(input('Ingrese numero:'))
inverted_number = 0
while number>0:
    inverted_number *=10
    inverted_number += (number%10)
    number=number//10
print(inverted_number)