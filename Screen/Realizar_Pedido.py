# Realizar_Pedido.py
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class Realizar_Pedido(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mesa_seleccionada = None  # Inicializar mesa_seleccionada en None

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
        else:
            print("No se ha seleccionado ninguna mesa.")
