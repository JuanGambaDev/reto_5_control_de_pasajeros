""" 
Reto 5
#Juan Sebastian Gamba Jacomussi
Mayo 06-2021 
"""

"""
Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones: 

1	Agregar pasajeros a la lista de viajeros.
2	Agregar ciudades a la lista de ciudades.
3	Dado el DNI (cédula) de un pasajero, ver a que ciudad viaja.
4	Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
5	Dado el DNI (cédula) de un pasajero, ver a que país viaja.
6	Dado un país, mostrar cuántos pasajeros viajan a esa ciudad.
7	Salir del programa.

""" 

#importamos libreria os
import os

#definimos variables
nombre = ""
dni = ""
destino = ""
pais_consultado = ""
ciudad = ""
#creamos listas vacias
pasajeros = []
ciudades = []

#creamos las funciones del menu
#funcion opcion 1 
def agregar_pasajeros(pasajeros):
  nombre = input("Ingrese su nombre(para salir digite 0): ")
  while nombre != "0":
    dni = int(input("ingrese su DNI: "))
    destino = input("ingrese su ciudad de destino: ")
    pasajeros.append((nombre,dni,destino))
    nombre = input("Ingrese su nombre(para salir digite 0): ")
  return pasajeros

#funcion opcion 2
def agregar_ciudades(ciudades):
  ciudad = ""
  pais = ""
  ciudad = input("Ingrese ciudad (para salir digite 0): ")
  while ciudad != "0" : 
    pais = input("ingrese pais: ")
    ciudades.append((ciudad,pais))
    ciudad = input("Ingrese ciudad (para salir digite 0): ")
  return ciudades

#función opcion 3
def consultar_destino(dni):
  dni = int(input("digite numero de cedula:"))
  while dni != 0:
    encontrado = True
    for pasajero in pasajeros:
      nombre, cedula, destino = pasajero
      if dni == cedula:
        print("nombre: ", nombre)
        print("destino:", destino)
        print("")
      break 
    if encontrado == False:
      print("Número de cedula no registrado.")
      dni = int(input("digite numero de cedula:"))
    else:
      dni = int(input("digite numero de cedula:"))

#funcion opcion 4
def consultar_personasporciudad(ciudad):
  numero = 0
  ciudad = input("ingrese ciudad (digite 0 pasa salir): ")
  while ciudad != "0":
    for pasajero in pasajeros:
      nombre, cedula, destino = pasajero
      if ciudad == pasajero[2]:
        numero = numero + 1
    print("cantidad de pasajeros: ",numero)
    numero = 0
    ciudad = input("ingrese ciudad (digite 0 pasa salir): ")

#función opción 5
def consultar_pais_pasajero(dni):
  dni = int(input("Cedula (Para salir ingrese 0) : "))
  while dni != 0:
    encontrado = False
    for pasajero in pasajeros:
      nombre, cedula, destino = pasajero
      if dni == cedula:
        encontrado = True
        for ciudad_pasajero in ciudades:
          ciudad, pais = ciudad_pasajero
          if ciudad == destino:
            print("Nombre: ", nombre)
            print("País Destino:", pais)
            print("")
          break
      break
    if encontrado==False:
      print("Número de cedula no registrado.")
      print("")
      dni = int(input("Cedula (Para salir ingrese 0) : "))
    else:
      dni = int(input("Cedula (Para salir ingrese 0) : "))

#Función opción 6
#Opcion 6
def cantidad_pasajeros_pais(pais_consultado): 
  pais_consultado = input("Pais (Para salir ingrese 0) : ")
  while pais_consultado != "0":
    cantidad_pasajeros = 0
    for tupla_ciudades in ciudades:
      ciudad, pais = tupla_ciudades
      if pais == pais_consultado:
        for tupla_pasajeros in pasajeros:     
          if ciudad == tupla_pasajeros[2] :
            cantidad_pasajeros = cantidad_pasajeros + 1
    print("Cantidad Pasajeros: ", cantidad_pasajeros)
    print("")
    pais_consultado=input("Pais (Para salir ingrese 0) : ")
    
#menu principal
def mostrar_menu():
  os.system('clear')
  print("1.- Agregar pasajeros")
  print("2.- Agregar ciudades")
  print("3.- Buscar ciudad de destino mediante DNI")
  print("4.- Cantidad de pasajeros que viajan a una ciudad")
  print("5.- Buscar pais destino mediante DNI")
  print("6.- Cantidad de pasajeros que viajan a un pais")
  print("7.- Salir")

  opc = int(input("Accion a ejecutar: "))

  if opc==1:
    # Agregar Pasajeros
    print("--> Registro de Pasajeros.")
    print("")
    agregar_pasajeros(pasajeros)
    print("")
    mostrar_menu()

  elif opc==2:
    # Agregar ciudades
    print("--> Registro de Ciudades.")
    print("")
    agregar_ciudades(ciudades)
    print("")
    mostrar_menu()

  elif opc==3:
    # Consultar Ciudad destino del pasajero por medio del número de cedula
    print("--> Consulta de Ciudad Destino.")
    print("")
    consultar_destino(dni)
    print("")
    mostrar_menu()
    
  elif opc==4:
    # Consultar cantidad de pasajeros por ciudad  
    print("--> Cantidad de Pasajeros.")
    print("")
    consultar_personasporciudad(ciudad)
    print("")
    mostrar_menu()

  elif opc==5:
    #Consultar país de destino.
    print("--> Consulta de País Destino")
    print("")
    consultar_pais_pasajero(dni)
    print("")
    mostrar_menu()

  elif opc==6:
    #Consultar cantidad de pasajeros por país.
    print("--> Cantidad de Pasajeros País.")
    print("")
    cantidad_pasajeros_pais(pais_consultado)
    print("")
    mostrar_menu()
 
  elif opc==7:
    print("--> Fin")
    print("")
    # Salir de la aplicación
    exit()

# Iniciamos el programa
def init():
    mostrar_menu()

if __name__ == "__main__":
    init()