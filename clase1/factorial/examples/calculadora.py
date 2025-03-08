from factorial import operacion

resultado=operacion.multiplicar(1,2)
print("el resultado es de la multiplicacion:",resultado)

resultado=operacion.factorial(5)
print("el resultado es del factorial:",resultado)

my_vector = [1, 2,2, 3, 4, 5]
valor_posicional = [1, 2,2, 3, 4, 5]
resultado=operacion.promedio(my_vector)
print("el promedio de la lista es:",resultado)

resultado=operacion.mediana(my_vector)
print("la mediana de la lista es:",resultado)

resultado=operacion.moda(my_vector)
print("la moda de la lista es:",resultado)

resultado=operacion.varianza(my_vector)
print("la varianza de la lista es:",resultado)

resultado=operacion.desviacion(my_vector)
print("la desviacion de la lista es:",resultado)

resultado=operacion.pesoposicional(my_vector,valor_posicional)
print("el valor posicional de la lista es:",resultado)