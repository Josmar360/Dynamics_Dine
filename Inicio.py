import pygame
import mysql.connector
from Screen.Mostrar_Pedidos import Mostrar_Pedidos

# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
info_pantalla = pygame.display.Info()
ANCHO, ALTO = info_pantalla.current_w, info_pantalla.current_h

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (253, 250, 235)
AZUL_CLARO = (205, 242, 214)
VERDE_GRIS = (151, 196, 173)
AMARILLO_VERDOSO = (230, 252, 217)

# Imágenes
logotipo = pygame.image.load("Image/Logotipo.png")

# Configuración de la ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Iniciar sesión")

# Fuentes para el texto
fuente_titulo = pygame.font.Font("Font/Lost_Signal_Regular.otf", 45)
fuente_boton = pygame.font.Font("Font/Lost_Signal_Regular.otf", 27)
fuente_input = pygame.font.Font("Font/Delmon_Delicate.ttf", 30)
fuente_texto = pygame.font.Font(None, 36)

# Datos de conexión a la base de datos
configuracion = {
    'user': '',  # Inicialmente vacíos, se llenarán con la entrada del usuario
    'password': '',
    'host': 'localhost',
    'database': 'Dynamics_Dine',
    'raise_on_warnings': True
}

MAX_CARACTERES_USUARIO = 18  # Límite de caracteres para el usuario
MAX_CARACTERES_PASSWORD = 20  # Límite de caracteres para la contraseña


def dibujar_texto(texto, fuente, color, surface, x, y):
    texto_objeto = fuente.render(texto, True, color)
    texto_rectangulo = texto_objeto.get_rect()
    texto_rectangulo.center = (x, y)
    surface.blit(texto_objeto, texto_rectangulo)


def mostrar_mensaje_error(mensaje):
    pantalla.fill(AZUL_CLARO)
    dibujar_texto(mensaje, fuente_titulo, NEGRO,
                  pantalla, ANCHO // 2, ALTO // 2)
    pygame.display.flip()
    pygame.time.wait(1500)  # Espera 1.5 segundos antes de continuar


def Inicio():
    ejecutando = True
    input_user = ''
    input_password = ''
    is_typing_user = True
    boton_iniciar_sesion = pygame.Rect(ANCHO // 2.25, ALTO // 1.31, 150, 30)
    boton_salir_rect = pygame.Rect(30, ALTO - 70, 130, 30)

    while ejecutando:
        pantalla.fill(AZUL_CLARO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                if is_typing_user:
                    if evento.key == pygame.K_BACKSPACE:
                        input_user = input_user[:-1]
                    elif evento.key == pygame.K_RETURN:
                        is_typing_user = False
                    elif evento.key == pygame.K_ESCAPE:
                        ejecutando = False
                    else:
                        if len(input_user) < MAX_CARACTERES_USUARIO:
                            input_user += evento.unicode
                else:
                    if evento.key == pygame.K_BACKSPACE:
                        input_password = input_password[:-1]
                    elif evento.key == pygame.K_RETURN:
                        configuracion['user'] = input_user
                        configuracion['password'] = input_password

                        try:
                            conn = mysql.connector.connect(**configuracion)
                            if conn.is_connected():
                                print("Conexión establecida con éxito")
                                Mostrar_Pedidos(configuracion)
                        except mysql.connector.Error as notificacion:
                            print(f"Error al conectar a la base de datos MySQL: {
                                  notificacion}")
                            mostrar_mensaje_error(
                                "Usuario y/o contraseña son incorrectos")
                            input_user = ''
                            input_password = ''
                        finally:
                            if "conn" in locals() and conn.is_connected():
                                conn.close()
                                print("Conexión cerrada")
                                ejecutando = False
                    else:
                        if len(input_password) < MAX_CARACTERES_PASSWORD:
                            input_password += evento.unicode
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = evento.pos
                if ANCHO // 2.5 <= mouse_x <= ANCHO // 2.5 + 300 and ALTO // 1.9 <= mouse_y <= ALTO // 1.9 + 30:
                    is_typing_user = True
                elif ANCHO // 2.5 <= mouse_x <= ANCHO // 2.5 + 300 and ALTO // 1.5 <= mouse_y <= ALTO // 1.5 + 30:
                    is_typing_user = False
                elif boton_iniciar_sesion.collidepoint(mouse_x, mouse_y):
                    if input_user and input_password:
                        configuracion['user'] = input_user
                        configuracion['password'] = input_password
                        try:
                            conn = mysql.connector.connect(**configuracion)
                            if conn.is_connected():
                                print("Conexión establecida con éxito")
                                Mostrar_Pedidos()
                        except mysql.connector.Error as notificacion:
                            print(f"Error al conectar a la base de datos MySQL: {
                                  notificacion}")
                            mostrar_mensaje_error(
                                "Usuario y/o contraseña son incorrectos")
                            input_user = ''
                            input_password = ''
                        finally:
                            if "conn" in locals() and conn.is_connected():
                                conn.close()
                                print("Conexión cerrada")
                                ejecutando = False
                elif boton_salir_rect.collidepoint(mouse_x, mouse_y):
                    ejecutando = False

        # Cuadro para colocar objetos del login
        pygame.draw.rect(pantalla, VERDE_GRIS,
                         (ANCHO // 2.82, ALTO // 3.5, 400, 500))
        # Cuadro para usuario
        pygame.draw.rect(pantalla, AMARILLO_VERDOSO,
                         (ANCHO // 2.55, ALTO // 1.9, 300, 30))
        # Cuadro para contraseña
        pygame.draw.rect(pantalla, AMARILLO_VERDOSO,
                         (ANCHO // 2.55, ALTO // 1.5, 300, 30))
        # Botón de Iniciar sesión
        pygame.draw.rect(pantalla, GRIS, boton_iniciar_sesion)
        dibujar_texto("Iniciar sesión", fuente_boton, NEGRO,
                      pantalla, ANCHO // 2, ALTO // 1.28)

        # Círculo de logotipo
        pantalla.blit(logotipo, (ANCHO // 2.0 - logotipo.get_width() //
                      2, ALTO // 3.8 - logotipo.get_height() // 2))

        dibujar_texto("Usuario:", fuente_titulo, NEGRO,
                      pantalla, ANCHO // 2, ALTO // 2.05)
        dibujar_texto("Contraseña:", fuente_titulo, NEGRO,
                      pantalla, ANCHO // 2, ALTO // 1.59)
        dibujar_texto(input_user, fuente_input, NEGRO,
                      pantalla, ANCHO // 2, ALTO // 1.85)
        dibujar_texto("*" * len(input_password), fuente_input,
                      NEGRO, pantalla, ANCHO // 2, ALTO // 1.44)

        # Crear botón "Salir"
        boton_salir_rect = pygame.Rect(30, ALTO - 70, 130, 30)
        pygame.draw.rect(pantalla, GRIS, boton_salir_rect)
        dibujar_texto("Salir", fuente_texto, NEGRO, pantalla, 95, ALTO - 55)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    Inicio()
