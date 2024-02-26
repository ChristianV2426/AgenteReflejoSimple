"""
    Inteligencia Artificial - 750022C Grupo 01
    Agente de Reflejo Simple - Clase main

    Autor:
    Christian David Vargas Gutiérrez - 2179172
"""

from clases import *


if __name__ == "__main__":
    matriz_entorno = Lector().leer_archivo_entorno("entorno.txt")
    matriz_decisiones = Lector().leer_archivo_decisiones("decisiones.txt")

    (x_raton, y_raton) = Raton.encontrar_raton(matriz_entorno)
    raton = Raton(x_raton, y_raton)

    agentes = []
    agentes.append(raton)

    entorno = Entorno(600, 600, "Agente de Reflejo Simple", matriz_entorno, matriz_decisiones, agentes)
    entorno.mostrar_entorno()
