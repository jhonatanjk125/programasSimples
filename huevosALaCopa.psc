Algoritmo huevosALaCopa
	Escribir "Ingrese la masa en gramos del huevo: "
	Leer m
	Escribir "Ingrese la temperatura original del huevo: "
	Leer To
	t = ((m	^(2/3)*3.7*(1.038^(1/3)))/(0.0054*PI*PI*(4*PI/3)^(2/3)))*ln(0.76*((To-100)/(70-100)))
	Escribir "El tiempo requerido es: ", t, " s"
FinAlgoritmo
