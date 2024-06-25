import pygame
import mysql.connector

# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
info_pantalla = pygame.display.Info()
ANCHO, ALTO = info_pantalla.current_w, info_pantalla.current_h

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (200, 200, 200)

# Configuración de la ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Iniciar sesión")

# Fuente para el texto
fuente_titulo = pygame.font.Font("Font/Pollinator.ttf", 50)

# Datos de conexión a la base de datos
configuracion = {
    'user': '',  # Inicialmente vacíos, se llenarán con la entrada del usuario
    'password': '',
    'host': 'localhost',
    'database': 'Dynamics_Dine',
    'raise_on_warnings': True
}


def dibujar_texto(texto, fuente, color, surface, x, y):
    texto_objeto = fuente.render(texto, True, color)
    texto_rectangulo = texto_objeto.get_rect()
    texto_rectangulo.center = (x, y)
    surface.blit(texto_objeto, texto_rectangulo)


def Inicio():
    ejecutando = True
    input_user = ''
    input_password = ''
    is_typing_user = True

    while ejecutando:
        pantalla.fill(BLANCO)

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
                                dibujar_texto(
                                    "Conexión establecida con éxito", fuente_titulo, NEGRO, pantalla, ANCHO // 2, ALTO // 2 + 50)
                        except mysql.connector.Error as notificacion:
                            print(f"Error al conectar a la base de datos MySQL: {
                                  notificacion}")
                            dibujar_texto(f"Error al conectar a la base de datos MySQL: {
                                          notificacion}", fuente_titulo, NEGRO, pantalla, ANCHO // 2, ALTO // 2 + 50)
                        finally:
                            if "conn" in locals() and conn.is_connected():
                                conn.close()
                                print("Conexión cerrada")
                        ejecutando = False
                    else:
                        input_password += evento.unicode

        pygame.draw.rect(pantalla, GRIS, (300, 150, 300, 30)
                         )  # Cuadro para usuario
        pygame.draw.rect(pantalla, GRIS, (300, 200, 300, 30)
                         )  # Cuadro para contraseña

        dibujar_texto("Usuario:", fuente_titulo, NEGRO, pantalla, 150, 135)
        dibujar_texto("Contraseña:", fuente_titulo, NEGRO, pantalla, 150, 185)
        dibujar_texto(input_user, fuente_titulo, NEGRO, pantalla, 450, 155)
        dibujar_texto("*" * len(input_password),
                      fuente_titulo, NEGRO, pantalla, 450, 205)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    Inicio()
