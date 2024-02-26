"""
    Inteligencia Artificial - 750022C Grupo 01
    Agente de Reflejo Simple - Clase Entorno

    Autor:
    Christian David Vargas Gutiérrez - 2179172
"""

import pygame
import os

ruta_actual = os.path.dirname(os.path.abspath(__file__))


class Entorno:
    def __init__(self, ancho, alto, titulo, matriz_entorno, matriz_decisiones, agentes):
        self.matriz_entorno = matriz_entorno
        self.filas = len(matriz_entorno)
        self.columnas = len(matriz_entorno[0])
        self.matriz_decisiones = matriz_decisiones
        self.percepciones = len(matriz_decisiones)
        self.sensores = len(matriz_decisiones[0])
        self.agentes = agentes

        self.rectangulo_ancho = ancho // self.columnas
        self.ancho = self.columnas * self.rectangulo_ancho
        self.rectangulo_alto = alto // self.filas
        self.alto = self.filas * self.rectangulo_alto
        self.titulo = titulo
        self.ventana = pygame.display.set_mode((self.ancho, self.alto))
        pygame.display.set_caption(self.titulo)

        self.icono_raton = pygame.image.load(os.path.join(ruta_actual, "imagenes/icono_raton.png"))
        self.icono_raton = pygame.transform.scale(self.icono_raton, (self.rectangulo_ancho*0.6, self.rectangulo_alto*0.6))
        self.icon_raton_offset_x = (self.rectangulo_ancho - self.icono_raton.get_width()) // 2
        self.icon_raton_offset_y = (self.rectangulo_alto - self.icono_raton.get_height()) // 2
        for agente in self.agentes:
            agente.actualizar_icono(self.icono_raton)
            agente.ajustar_posicion_actual(self.rectangulo_ancho, self.rectangulo_alto, self.icon_raton_offset_x, self.icon_raton_offset_y)

        self.icono_queso = pygame.image.load(os.path.join(ruta_actual, "imagenes/icono_queso.png"))
        self.icono_queso = pygame.transform.scale(self.icono_queso, (self.rectangulo_ancho*0.4, self.rectangulo_alto*0.4))
        self.icon_queso_offset_x = (self.rectangulo_ancho - self.icono_queso.get_width()) // 2
        self.icon_queso_offset_y = (self.rectangulo_alto - self.icono_queso.get_height()) // 2

        self.colores = [(192, 192, 192), (28, 68, 88),]


    def mostrar_entorno(self):
        while True:
            evento = pygame.event.poll()
            if evento.type == pygame.QUIT:
                break

            for fila in range(self.filas):
                for columna in range(self.columnas):
                    rectangulo = pygame.Rect(columna * self.rectangulo_ancho, fila * self.rectangulo_alto, self.rectangulo_ancho, self.rectangulo_alto)
                    
                    if (self.matriz_entorno[fila][columna] == 1): # Obstáculo
                        self.ventana.fill(self.colores[1], rectangulo)
                        pygame.draw.rect(self.ventana, (0, 0, 0), rectangulo, 1)

                    else:
                        self.ventana.fill(self.colores[0], rectangulo)
                        pygame.draw.rect(self.ventana, (0, 0, 0), rectangulo, 1)

                        if (self.matriz_entorno[fila][columna] == 3): # Queso
                            self.ventana.blit(self.icono_queso, (columna * self.rectangulo_ancho + self.icon_queso_offset_x, fila * self.rectangulo_alto + self.icon_queso_offset_y))

            for agente in self.agentes:
                agente.actualizar(self.matriz_entorno, self.matriz_decisiones)
                agente.dibujar(self.ventana)


            pygame.display.flip()

        pygame.quit()


