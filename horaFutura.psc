Algoritmo horaFutura
	Escribir 'Hora Actual'
	Leer current_time
	Escribir 'Cantidad de horas'
	Leer hours
	future_time <- (current_time+hours) MOD 24
	Escribir 'En ', hours, ' horas, el reloj marcar� las ', future_time
FinAlgoritmo
