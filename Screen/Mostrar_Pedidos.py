import pygame
import mysql.connector
from datetime import datetime

# Inicialización de Pygame
pygame.init()

# Cargar ícono personalizado
icono = pygame.image.load('Icon/Dynamics_Dine.png')
pygame.display.set_icon(icono)

# Dimensiones de la pantalla
info_pantalla = pygame.display.Info()
ANCHO, ALTO = info_pantalla.current_w, info_pantalla.current_h

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL_CLARO = (205, 242, 214)
VERDE_GRIS = (151, 196, 173)
GRIS = (253, 250, 235)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)

# Configuración de la ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pedidos en Cocina")

# Fuente para el texto
fuente_titulo = pygame.font.Font("Font/Lost_Signal_Regular.otf", 70)
fuente_horario = pygame.font.Font("Font/Lost_Signal_Regular.otf", 40)
fuente_texto = pygame.font.Font(None, 36)


def dibujar_texto(texto, fuente, color, surface, x, y):
    texto_objeto = fuente.render(texto, True, color)
    texto_rectangulo = texto_objeto.get_rect()
    texto_rectangulo.center = (x, y)
    surface.blit(texto_objeto, texto_rectangulo)


def actualizar_estatus_pedido(num_pedido, clave_platillo, configuracion):
    try:
        conn = mysql.connector.connect(**configuracion)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Detalles_Pedido DP SET ESTATUS = 1 WHERE DP.FK_PK_NUM_PEDIDO = %s AND DP.FK_PK_PLATILLO = %s;",
            (num_pedido, clave_platillo)
        )
        print(f"Actualizo num: {num_pedido}, platillo: {clave_platillo}")
        conn.commit()
    except mysql.connector.Error as notificacion:
        print(f"Error al conectar a la base de datos MySQL: {notificacion}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()


def obtener_pedidos(configuracion):
    try:
        conn = mysql.connector.connect(**configuracion)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT DP.FK_PK_Num_Pedido, P.Platillos, DP.Cantidad, DP.Estatus, DP.FK_PK_Platillo FROM Detalles_Pedido DP JOIN Platillos P ON DP.FK_PK_Platillo = P.FK_Platillo WHERE DP.FK_PK_Num_Pedido IN (SELECT FK_PK_Num_Pedido FROM Detalles_Pedido WHERE Estatus = 0)"
        )
        pedidos = cursor.fetchall()
        return pedidos
    except mysql.connector.Error as notificacion:
        print(f"Error al conectar a la base de datos MySQL: {notificacion}")
        return []
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()


def Mostrar_Pedidos(configuracion):
    ejecutando = True

    while ejecutando:
        pedidos = obtener_pedidos(configuracion)
        pantalla.fill(AZUL_CLARO)
        y_offset = 100

        dibujar_texto("Pedidos en Cocina", fuente_titulo,
                      NEGRO, pantalla, ANCHO // 2, 50)

        # Mostrar fecha y hora
        fecha_hora_actual = datetime.now()
        fecha_texto = fecha_hora_actual.strftime("%d/%m/%Y")
        hora_texto = fecha_hora_actual.strftime("%H:%M:%S")
        pygame.draw.rect(pantalla, VERDE_GRIS, (30, 40, 220, 50))
        dibujar_texto(fecha_texto, fuente_horario, NEGRO, pantalla,
                      140, 65)  # Fecha en la parte superior izquierda
        pygame.draw.rect(pantalla, VERDE_GRIS, (ANCHO - 178, 40, 152, 50))
        dibujar_texto(hora_texto, fuente_horario, NEGRO, pantalla,
                      ANCHO - 100, 65)  # Hora en la parte superior derecha

        # Cuadro para colocar objetos de los pedidos
        cuadro_altura = 600
        cuadro_y = y_offset + 25
        pygame.draw.rect(pantalla, VERDE_GRIS,
                         (250, cuadro_y, 925, cuadro_altura))
        y_offset += 50

        headers = ["N° Pedido", "Platillo", "Cantidad", "Estatus", "Entregar"]
        x_offset = [350, 550, 750, 950, 1100]

        for i, header in enumerate(headers):
            dibujar_texto(header, fuente_texto, NEGRO,
                          pantalla, x_offset[i], y_offset)

        y_offset += 50

        botones = []
        pedidos_dict = {}

        for pedido in pedidos:
            num_pedido = pedido[0]
            if num_pedido not in pedidos_dict:
                pedidos_dict[num_pedido] = []
            pedidos_dict[num_pedido].append(pedido)

        # Calcular el número máximo de filas que caben en el cuadro
        max_filas = cuadro_altura // 50

        fila_actual = 0
        for num_pedido, detalles in pedidos_dict.items():
            if fila_actual >= max_filas:
                break
            for detalle in detalles:
                if fila_actual >= max_filas:
                    break
                for i, item in enumerate(detalle[:4]):
                    if i == 3:  # Estatus
                        if item == 0:
                            item = "Pendiente"
                            color = ROJO
                        else:
                            item = "Terminado"
                            color = VERDE
                    else:
                        color = NEGRO
                    dibujar_texto(str(item), fuente_texto, color,
                                  pantalla, x_offset[i], y_offset)

                # Crear botón "Entregar"
                boton_rect = pygame.Rect(1045, y_offset - 15, 110, 30)
                pygame.draw.rect(pantalla, GRIS, boton_rect)
                dibujar_texto("Entregar", fuente_texto,
                              NEGRO, pantalla, 1100, y_offset)
                botones.append((boton_rect, detalle[0], detalle[4]))

                y_offset += 50
                fila_actual += 1

        # Crear botón "Salir"
        boton_salir_rect = pygame.Rect(30, ALTO - 70, 130, 30)
        pygame.draw.rect(pantalla, GRIS, boton_salir_rect)
        dibujar_texto("Salir", fuente_texto, NEGRO, pantalla, 95, ALTO - 55)

        # Crear botón "Regresar"
        boton_regresar_rect = pygame.Rect(ANCHO - 160, ALTO - 70, 130, 30)
        pygame.draw.rect(pantalla, GRIS, boton_regresar_rect)
        dibujar_texto("Regresar", fuente_texto, NEGRO,
                      pantalla, ANCHO - 95, ALTO - 55)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    ejecutando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                mouse_pos = evento.pos
                for boton_rect, num_pedido, clave_platillo in botones:
                    if boton_rect.collidepoint(mouse_pos):
                        actualizar_estatus_pedido(
                            num_pedido, clave_platillo, configuracion)
                        print("Entregar")
                if boton_salir_rect.collidepoint(mouse_pos):
                    ejecutando = False
                elif boton_regresar_rect.collidepoint(mouse_pos):
                    from Inicio import Inicio
                    Inicio()
                    ejecutando = False

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    Mostrar_Pedidos()
