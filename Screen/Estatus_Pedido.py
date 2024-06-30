from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
import mysql.connector


class ProductCard(BoxLayout):
    def __init__(self, product_name, product_image, product_status, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.height = 300  # Ajustar altura para incluir el estatus

        # Imagen del producto
        self.image = Image(source=product_image, size_hint_y=None, height=200)
        self.add_widget(self.image)

        # Nombre del producto
        self.add_widget(Label(text=product_name, size_hint_y=None, height=30))

        # Estado del producto
        status_label = Label(text=product_status, size_hint_y=None, height=30)
        if "preparando" in product_status.lower():
            # Rojo para "Su comida se está preparando"
            status_label.color = (1, 0, 0, 1)
        elif "lista para recoger" in product_status.lower():
            # Verde para "Su comida está lista para recoger"
            status_label.color = (0, 1, 0, 1)
        else:
            # Blanco para cualquier otro caso
            status_label.color = (1, 1, 1, 1)
        self.add_widget(status_label)


class Estatus_Pedido(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=[
                           30, 20, 30, 30], spacing=10)  # Ajuste de spacing aquí

        # Título centrado
        titulo = Label(text='Estatus de pedido', halign='center',
                       valign='middle', size_hint=(1, None), height=60, font_size=50)
        layout.add_widget(titulo)

        # Contenedor para el número de pedido y número de mesa
        self.numero_pedido_label = Label(
            text='Número de pedido:', halign='center', valign='middle', size_hint=(1, None), height=30, font_size=30)
        layout.add_widget(self.numero_pedido_label)

        self.numero_mesa_label = Label(text='Número de mesa:', halign='center',
                                       valign='middle', size_hint=(1, None), height=30, font_size=30)
        layout.add_widget(self.numero_mesa_label)

        # Separador
        # Ajuste de height aquí
        layout.add_widget(BoxLayout(size_hint=(1, None), height=5))

        # ScrollView para las tarjetas de productos
        scroll_view = ScrollView(size_hint=(1, 1))
        self.estatus_layout = GridLayout(
            cols=3, spacing=10, size_hint_y=None)  # Ajuste de spacing aquí
        self.estatus_layout.bind(
            minimum_height=self.estatus_layout.setter('height'))
        scroll_view.add_widget(self.estatus_layout)
        layout.add_widget(scroll_view)

        # Espacio para el botón de actualizar
        # Ajuste de height aquí
        layout.add_widget(BoxLayout(size_hint_y=None, height=0))

        # Agregar los botones de Salir y Pagar
        button_layout = GridLayout(cols=3, size_hint=(1, None), height=50)
        menu_alimentos_button = Button(
            text='Menu Alimentos', size_hint=(0.5, 1))
        menu_alimentos_button.bind(on_press=self.go_to_menu_alimentos)
        actualizar_button = Button(text='Actualizar', size_hint=(0.5, 1))
        actualizar_button.bind(on_press=self.go_to_actualizar)
        recoger_button = Button(text='Recoger', size_hint=(0.5, 1))
        recoger_button.bind(on_press=self.go_to_recoger)

        button_layout.add_widget(menu_alimentos_button)
        button_layout.add_widget(actualizar_button)
        button_layout.add_widget(recoger_button)

        layout.add_widget(button_layout)

        self.add_widget(layout)

        # Consultar el estatus de los pedidos
        self.consultar_estatus_pedidos()

    def consultar_estatus_pedidos(self):
        try:
            # Conexión a la base de datos
            conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Sarinha_3',
                database='Dynamics_Dine'
            )

            cursor = conexion.cursor()

            # Realizar la consulta
            query = """
            SELECT PD.PK_Num_Pedido, P.Platillos, PD.Mesa, DP.Estatus, P.FK_Platillo
            FROM Pedidos PD
            JOIN Detalles_Pedido DP ON PD.PK_Num_Pedido = DP.FK_PK_Num_Pedido
            JOIN Platillos P ON DP.FK_PK_Platillo = P.FK_Platillo
            WHERE PD.Mesa = 4 AND DP.Entregado = 0;
            """
            cursor.execute(query)

            # Limpiar el layout actual
            self.estatus_layout.clear_widgets()

            # Mostrar los resultados
            for (pk_num_pedido, platillo, mesa, estatus, fk_platillo) in cursor:
                self.numero_pedido_label.text = f'Número de pedido: {
                    pk_num_pedido}'
                self.numero_mesa_label.text = f'Número de mesa: {mesa}'

                # Crear la tarjeta de producto
                card = ProductCard(product_name=platillo, product_image=f'Image/{
                                   fk_platillo}.jpg', product_status=self.get_status_text(estatus))
                self.estatus_layout.add_widget(card)

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            cursor.close()
            conexion.close()

    def get_status_text(self, estatus):
        if estatus == 0:
            return "Su comida se está preparando"
        elif estatus == 1:
            return "Su comida está lista para recoger"
        else:
            return f"Estatus: {estatus}"

    def go_to_menu_alimentos(self, instance):
        self.manager.current = 'menu_alimentos'

    def go_to_actualizar(self, instance):
        self.consultar_estatus_pedidos()

    def go_to_recoger(self, instance):
        try:
            # Conexión a la base de datos
            conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Sarinha_3',
                database='Dynamics_Dine'
            )

            cursor = conexion.cursor()

            # Query para actualizar el estado a 'Recogido'
            update_query = """
            UPDATE Detalles_Pedido AS DP
            JOIN Pedidos AS P ON DP.FK_PK_Num_Pedido = P.PK_Num_Pedido
            SET DP.Entregado = 1
            WHERE DP.Estatus = 1 AND P.Mesa = 4;
            """

            cursor.execute(update_query)
            conexion.commit()

            # Mostrar mensaje de éxito
            popup = Popup(title='Éxito',
                          content=Label(
                              text='Productos recogidos correctamente.'),
                          size_hint=(None, None), size=(400, 200))
            popup.open()

            # Actualizar la pantalla
            self.consultar_estatus_pedidos()

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            # Mostrar mensaje de error
            popup = Popup(title='Error',
                          content=Label(
                              text=f'Error al recoger productos: {err}'),
                          size_hint=(None, None), size=(400, 200))
            popup.open()

        finally:
            cursor.close()
            conexion.close()
