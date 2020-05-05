#Veremos como insertar datos a un diccionario
diccionario = {}
nombre = raw_input("Ingresa su nombre: ")
diccionario["Nombre"] = nombre

apellido = raw_input("Ingrese su apellido: ")
diccionario["Apellido"] = apellido

edad = int(input("Que edad tienes: "))
diccionario["Edad"] = edad

numero_telefono = int(input("Ingrese su numero de telefono: "))
diccionario["Telefono"] = numero_telefono

estado_civil = raw_input("Casado o soltero: ")
diccionario["Estado civil"] = estado_civil
