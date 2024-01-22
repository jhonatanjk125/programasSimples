Algoritmo numeroInvertido
	Escribir 'Ingrese número: '
	Leer number
	inverted_number <- 0
	Mientras number>0 Hacer
		inverted_number <- inverted_number*10
		inverted_number <- inverted_number+number MOD 10
		number <- TRUNC(number/10)
	FinMientras
	Escribir inverted_number
FinAlgoritmo
