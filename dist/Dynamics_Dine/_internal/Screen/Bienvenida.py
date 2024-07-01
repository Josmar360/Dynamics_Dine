from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.uix.label import Label


class Bienvenida(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Usamos RelativeLayout para mayor flexibilidad en el posicionamiento
        layout = RelativeLayout()

        # Agregar imagen grande del logotipo
        logo = Image(source='Image/Logotipo.png',
                     size_hint=(None, None), size=(300, 300))
        layout.add_widget(logo)
        logo.pos_hint = {'center_x': 0.5, 'center_y': 0.7}

        # Agregar texto de bienvenida abajo del logotipo
        welcome_label = Label(
            text='Bienvenido a la Casa De Toño', font_size=60, halign='center')
        layout.add_widget(welcome_label)
        welcome_label.pos_hint = {'center_x': 0.5, 'center_y': 0.3}

        self.add_widget(layout)

    def on_touch_down(self, touch):
        super().on_touch_down(touch)
        # Redirigir al siguiente screen cuando se hace clic en cualquier lugar Menu_Alimentos.py
        if touch.is_mouse_scrolling or touch.is_double_tap:
            return False  # Permitir que el evento se propague
        else:
            self.manager.current = 'menu_alimentos'
