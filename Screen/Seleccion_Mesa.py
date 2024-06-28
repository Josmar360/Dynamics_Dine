from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

selected_table = {}


class Seleccion_Mesa(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Configuración del layout principal
        layout = GridLayout(cols=1, spacing=10,
                            size_hint=(None, None), padding=[50])
        layout.bind(minimum_height=layout.setter('height'))

        # Título "Selecciona la mesa"
        title_label = Label(text="Selecciona la mesa", size_hint=(
            1, None), height=100, font_size=36, halign='center')
        layout.add_widget(title_label)

        # Scroll view para los botones de las mesas
        scrollview = ScrollView(size_hint=(None, None), size=(
            Window.width, Window.height - 200))
        scrollview.add_widget(self.create_table_buttons())
        layout.add_widget(scrollview)

        self.add_widget(layout)

    def create_table_buttons(self):
        # Layout para los botones de las mesas
        button_layout = GridLayout(
            cols=4, spacing=10, size_hint_y=None, padding=[50, 10])
        button_layout.bind(minimum_height=button_layout.setter('height'))

        # Botones para seleccionar mesas (asumo diez mesas)
        for mesa_num in range(1, 13):
            mesa_button = Button(text=f'Mesa {mesa_num}', size_hint=(
                None, None), size=(200, 200))
            mesa_button.bind(on_press=lambda instance,
                             mesa=mesa_num: self.select_table(mesa))
            button_layout.add_widget(mesa_button)

        return button_layout

    def select_table(self, mesa_num):
        # Almacenar la selección de mesa en la variable global 'selected_table'
        global selected_table
        selected_table = mesa_num

        # Cambiar a la siguiente pantalla después de seleccionar la mesa
        # Cambia 'bienvenida' al nombre de tu siguiente pantalla
        self.manager.current = 'bienvenida'
