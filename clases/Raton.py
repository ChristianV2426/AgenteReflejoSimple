"""
    Inteligencia Artificial - 750022C Grupo 01
    Agente de Reflejo Simple - Clase Ratón

    Autor:
    Christian David Vargas Gutiérrez - 2179172
"""

class Raton:

    @staticmethod
    def encontrar_raton(matriz_entorno):
        for fila in range(len(matriz_entorno)):
            for columna in range(len(matriz_entorno[0])):
                if (matriz_entorno[fila][columna] == 2):
                    print(fila, columna)
                    return (fila, columna)
        return None


    def __init__(self, x_actual, y_actual):
        self.x_actual = x_actual
        self.y_actual = y_actual


    def actualizar_icono(self, icono):
        self.icono = icono

    
    def ajustar_posicion_actual(self, rectangulo_ancho, rectangulo_alto, offset_x, offset_y):
        self.x_actual = self.x_actual * rectangulo_alto + offset_x
        self.y_actual = self.y_actual * rectangulo_ancho + offset_y


    def actualizar(self, matriz_entorno, matriz_decisiones):
        pass
    

    def dibujar(self, ventana):
        ventana.blit(self.icono, (self.y_actual, self.x_actual))
