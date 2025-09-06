
def say_hello():
	print("Hello world!")

#Marcar doble "Enter" para indicar el termino de la función

#Ejecutar/llamar la función

say_hello()

______________________________________________

#FUNCIONES SIMPLES

#SUMA 
# num1 parámetro abierto

def add_two(num1):
	result = num1 + 2
	return result

print(add_two(3))
#5


#ELEVAR AL CUADRADO
#num parámetro abierto

def square_number(num):
	return num * num

print(square_number(4))
#16


#MULTIPLO DE 2 NUMEROS 
# num1 y num2 parámetros abiertos

def multiple_two_numbers(num1, num2):
	return num1 + num2

print(multiple_two_numbers(2,3))
#5


#FUNCIONES COMPUESTAS
#Sustitución valor de x

def add_tree(x):
	return x + 3

print(add_tree(1))
#4


#Función reciprocal y compuesta
# parametros f y x

def reciprocal(f):
	return 1/f

def composite_function(x):
	return reciprocal(add_tree(x))

composite_function(1)
#0.25

#Verificar manualmente

result = 1/(1+3)

print(result)
#0.25



#EJERCISIO. Exercises: Create composite functions that evaluate the absolute value of a number



#Función compuesta (cuadrada y suma)

def square_number(num):
	return num * num

def add_five(x):
	return x + 5

def composite_function(x):
	return square_number(add_five(x))

composite_function(7)
#144

_________________________________________
#Función compuesta (cuadrada y suma)
 
def multiple_two_numbers(num1, num2):
	return num1 * num2


def substract_four(x):
	return x - 4

def composite_function(x,y):
	return multiple_two_numbers(substract_four(x),y)

composite_function(10,3)
#18

_______________________
# Valor absoluto

def absolute_value(x):
	if x < 0: 
		return -x
	else:
		return x

print(absolute_value(-5))
#5
print(absolute_value(5))
#5





