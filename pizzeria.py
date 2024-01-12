import os.path
from typing import Dict
import csv
# Función para verificar si un usuario ya está registrado
def usuario_existente(correo):
    file_path = 'usuarios.csv'

    if not os.path.isfile(file_path):
        # If the file doesn't exist, create an empty file
        with open(file_path, 'w', newline=''):
            pass

    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[1] == correo:
                return True
    return False

# Función para registrar un nuevo usuario si no existe previamente
def registrar_usuario():
    while True:
        print("Creemos una cuenta para ti")
        nombre = input("Introduce tu nombre: ")
        correo = input("Introduce tu nombre de usuario: ")
        contraseña = input("Introduce una contraseña: ")

        if nombre.strip() != "" and correo.strip() != "" and contraseña.strip() != "":
            if not usuario_existente(correo):
                with open('usuarios.csv', mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([nombre, correo, contraseña])
                    print("Usuario registrado. Inicia sesión.")
                    break
            else:
                print("Ya existe un usuario con este correo. intentalo de nuevo.")
                break
        else:
            print("Falta información.")

# Función para verificar si el usuario existe en el archivo CSV
def verificar_usuario(correo, contraseña):
    with open('usuarios.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == correo and row[2] == contraseña:
                return True
    return False

# Interacción con el usuario
def iniciar_sesion_o_registrar():
    print("Pizzeria DELIZIOSO, que desea?")
    opcion = input("Esta registrado? (sí/no): ")

    if opcion.lower() == 'no':
        registrar_usuario()
        iniciar_sesion_o_registrar()
    elif opcion.lower() == 'sí':
        correo = input("Ingresar tu nombre de usuario: ")
        contraseña = input("Ingresa tu contraseña: ")
        if verificar_usuario(correo, contraseña):
            print("El incio de sesiónha sido todo un exito.")
            # Aquí podrías redirigir al usuario a la página principal de la pizzería
        else:
            print("Campos incorrectos. Inténtalo de nuevo.")
            iniciar_sesion_o_registrar()
    else:
        print("Respuestas válidas: 'sí' o 'no'.")
        iniciar_sesion_o_registrar()




