#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("=" * 50)
print("FORMULARIO DE DATOS PERSONALES")
print("=" * 50)
print()

# Solicitar datos personales
nombre = input("¿Cuál es tu nombre? ")
apellido = input("¿Cuál es tu apellido? ")
edad = input("¿Cuántos años tienes? ")
pais = input("¿Cuál es tu país? ")
ciudad = input("¿Cuál es tu ciudad? ")
telefono = input("¿Cuál es tu teléfono? ")
email = input("¿Cuál es tu email? ")

# Mostrar información
print()
print("=" * 50)
print("INFORMACIÓN REGISTRADA")
print("=" * 50)
print(f"Nombre: {nombre}")
print(f"Apellido: {apellido}")
print(f"Edad: {edad} años")
print(f"País: {pais}")
print(f"Ciudad: {ciudad}")
print(f"Teléfono: {telefono}")
print(f"Email: {email}")
print("=" * 50)
