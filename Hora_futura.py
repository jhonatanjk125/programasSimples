current_time = int(input('Hora actual: '))
hours = int(input('Cantidad de horas: '))
print(f'En {hours} horas, el reloj marcará las {(current_time+hours)%24}')