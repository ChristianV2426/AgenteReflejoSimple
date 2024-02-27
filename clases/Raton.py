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
                    return (fila, columna)
        return None


    def __init__(self, y, x):
        # Las posiciones x, y guardan la posición en términos de los índices de la matriz de entorno
        self.y = y # Filas
        self.x = x # Columnas

        # Las posiciones estáticas, dinámicas y objetivo guardan la posición en términos de píxeles de la ventana
        self.y_estatico = y
        self.x_estatico = x

        self.y_dinamico = y
        self.x_dinamico = x

        self.y_objetivo = y
        self.x_objetivo = x

        # Tamaño de cada rectangulo en la cuadrícula, para efectos de ajustar la posición del ratón en la ventana
        self.rectangulo_ancho = 0
        self.rectangulo_alto = 0


    def actualizar_icono(self, icono):
        self.icono = icono

    
    def ajustar_posicion_actual(self, rectangulo_ancho, rectangulo_alto, offset_x, offset_y):
        self.rectangulo_ancho = rectangulo_ancho
        self.rectangulo_alto = rectangulo_alto

        # Ajustar la posición actual del ratón en términos de píxeles de la ventana
        self.y_estatico = self.y_estatico * rectangulo_alto + offset_y
        self.x_estatico = self.x_estatico * rectangulo_ancho + offset_x

        self.y_dinamico = self.y_dinamico * rectangulo_alto + offset_y
        self.x_dinamico = self.x_dinamico * rectangulo_ancho + offset_x


    def percibir_entorno(self, matriz_entorno):
        filas = len(matriz_entorno)
        columnas = len(matriz_entorno[0])
        
        if (self.x == 0):
            izquierda = False
        else:
            izquierda = matriz_entorno[self.y][self.x - 1] != 1
        
        if (self.y == 0):
            arriba = False
        else:
            arriba = matriz_entorno[self.y - 1][self.x] != 1
        
        if (self.x == filas - 1):
            derecha = False
        else:
            derecha = matriz_entorno[self.y][self.x + 1] != 1
        
        if (self.y == columnas - 1):
            abajo = False
        else:
            abajo = matriz_entorno[self.y + 1][self.x] != 1
        
        return (izquierda, arriba, derecha, abajo)
    
    
    def tomar_decision(self, matriz_entorno, matriz_decisiones):
        (izquierda, arriba, derecha, abajo) = self.percibir_entorno(matriz_entorno)
        percepciones = len(matriz_decisiones)

        for i in range(percepciones):
            if (izquierda == matriz_decisiones[i][0] and
                arriba == matriz_decisiones[i][1] and
                derecha == matriz_decisiones[i][2] and
                abajo == matriz_decisiones[i][3]):
                return matriz_decisiones[i][5]
    

    def mover_raton(self, accion):
        if (accion == "izquierda"):
            self.x_objetivo = self.x_estatico - self.rectangulo_ancho
            self.y_objetivo = self.y_estatico
            self.x_dinamico -= self.velocidad_x
        
        elif (accion == "arriba"):
            self.x_objetivo = self.x_estatico
            self.y_objetivo = self.y_estatico - self.rectangulo_alto
            self.y_dinamico -= self.velocidad_y

        elif (accion == "derecha"):
            self.x_objetivo = self.x_estatico + self.rectangulo_ancho
            self.y_objetivo = self.y_estatico
            self.x_dinamico += self.velocidad_x

        elif (accion == "abajo"):
            self.x_objetivo = self.x_estatico
            self.y_objetivo = self.y_estatico + self.rectangulo_alto
            self.y_dinamico += self.velocidad_y


    def actualizar(self, matriz_entorno, matriz_decisiones):
        ha_ganado = False
        self.velocidad_x = 2
        self.velocidad_y = 2

        accion = self.tomar_decision(matriz_entorno, matriz_decisiones)

        self.mover_raton(accion)

        if (self.x_dinamico == self.x_objetivo and self.y_dinamico == self.y_objetivo):
            self.x_estatico = self.x_objetivo
            self.y_estatico = self.y_objetivo

            matriz_entorno[self.y][self.x] = 0
            
            if(accion == "izquierda"):
                if (matriz_entorno[self.y][self.x - 1] == 3):
                    ha_ganado = True
                self.x -= 1

            elif(accion == "arriba"):
                if (matriz_entorno[self.y - 1][self.x] == 3):
                    ha_ganado = True
                self.y -= 1

            elif(accion == "derecha"):
                if (matriz_entorno[self.y][self.x + 1] == 3):
                    ha_ganado = True
                self.x += 1

            elif(accion == "abajo"):
                if (matriz_entorno[self.y + 1][self.x] == 3):
                    ha_ganado = True
                self.y += 1

            matriz_entorno[self.y][self.x] = 2

        return ha_ganado      


    def dibujar(self, ventana):
        ventana.blit(self.icono, (self.x_dinamico, self.y_dinamico))
