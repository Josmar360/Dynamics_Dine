# Realizar_Pedido.py
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import mysql.connector

# Importar la variable global total_a_pagar desde Carrito_Compras.py
from Screen.Carrito_Compras import total_a_pagar


class Realizar_Pedido(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mesa_seleccionada = None  # Inicializar mesa_seleccionada en None
        self.custom_selected = {}

        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=[
                           30, 80, 30, 30], spacing=20)

        # Título centrado
        titulo = Label(text='Pedido realizado', halign='center',
                       valign='middle', size_hint=(1, None), height=40, font_size=50)
        layout.add_widget(titulo)

        # Mostrar el número de mesa seleccionada
        self.mesa_label = Label(text='Mesa seleccionada: ',
                                halign='center', size_hint=(1, None), height=40, font_size=24)
        layout.add_widget(self.mesa_label)

        # Mostrar el total a pagar
        self.total_label = Label(text=f'Total a Pagar: ${total_a_pagar:.2f}',
                                 halign='center', size_hint=(1, None), height=40, font_size=24)
        layout.add_widget(self.total_label)

        # Espacio para el botón de actualizar
        layout.add_widget(BoxLayout(size_hint_y=None, height=100))

        # Agregar botón de actualizar
        button_layout = GridLayout(cols=2, size_hint=(1, None), height=50)
        actualizar_button = Button(
            text='Actualizar', size_hint=(1, None), height=50)
        actualizar_button.bind(on_press=self.actualizar_pedido)
        button_layout.add_widget(actualizar_button)

        layout.add_widget(button_layout)

        self.add_widget(layout)

    def update_selected_table(self, mesa_seleccionada):
        self.mesa_seleccionada = mesa_seleccionada
        self.mesa_label.text = f'Mesa seleccionada: {self.mesa_seleccionada}'

    def actualizar_pedido(self, instance):
        if self.mesa_seleccionada is not None:
            print("Actualizando pedido para mesa número:", self.mesa_seleccionada)
            # Aquí deberías insertar en la base de datos usando el número de mesa seleccionada
            self.insertar_pedido(self.mesa_seleccionada,
                                 total_a_pagar, self.custom_selected)
        else:
            print("No se ha seleccionado ninguna mesa.")

    # Método para mostrar los valores de custom_selected
    def mostrar_custom_selected(self, custom_selected):
        self.custom_selected = custom_selected
        print("\nProductos personalizados desde Menu_Alimentos:")
        for fk_platillo, quantity in custom_selected.items():
            print(f"FK_Platillo: {fk_platillo}, Cantidad: {quantity}")

    # Método para actualizar el precio total
    def actualizar_precio_total(self, total):
        self.total_label.text = f'Total a Pagar: ${total:.2f}'
        print(f"Total a pagar es: {total}")

    # Método para insertar el pedido en la base de datos
    def insertar_pedido(self, mesa, total, custom_selected):
        try:
            # Conexión a la base de datos
            conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Sarinha_3',
                database='Dynamics_Dine'
            )

            cursor = conexion.cursor()

            # Comenzar una transacción
            cursor.execute("START TRANSACTION;")

            # Insertar datos en la tabla Pedidos y obtener el ID generado
            insert_pedido_query = "INSERT INTO Pedidos (Mesa, Total) VALUES (%s, %s);"
            cursor.execute(insert_pedido_query, (mesa, total))
            conexion.commit()  # Guardamos los cambios para obtener el LAST_INSERT_ID

            # Obtener el ID generado en Pedidos
            cursor.execute("SELECT LAST_INSERT_ID();")
            id_pedido = cursor.fetchone()[0]

            # Insertar en Detalles_Pedido usando el ID generado de Pedidos
            for fk_platillo, quantity in custom_selected.items():
                insert_detalle_query = "INSERT INTO Detalles_Pedido (FK_PK_Num_Pedido, FK_PK_Platillo, Cantidad, Estatus) VALUES (%s, %s, %s, %s);"
                cursor.execute(insert_detalle_query,
                               (id_pedido, fk_platillo, quantity, 0))

            # Confirmar la transacción
            conexion.commit()
            print("Pedido insertado exitosamente.")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            conexion.rollback()

        finally:
            cursor.close()
            conexion.close()
