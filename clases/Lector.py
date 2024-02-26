"""
    Inteligencia Artificial - 750022C Grupo 01
    Agente de Reflejo Simple - Clase Lector

    Autor:
    Christian David Vargas Gutiérrez - 2179172
"""

class Lector:
    def __init__(self):
        pass

    def leer_archivo_entorno(self, archivo):
        matriz_entorno = []

        with open(archivo, "r") as file:
            for line in file:
                matriz_entorno.append(list(map(int, line.split())))

        return matriz_entorno
    
    
    def intentar_bool(self,s):
        try:
            int(s)
            return bool(s)
        
        except ValueError:
            return s

    
    def leer_archivo_decisiones(self, archivo):
        matriz_decisiones = []

        with open(archivo, "r") as file:
            next(file) # Saltar la primera línea, que es de información para el usuario
            for line in file:
                matriz_decisiones.append(list(map(self.intentar_bool, line.split())))
                
        return matriz_decisiones

            
