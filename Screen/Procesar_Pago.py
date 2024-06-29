from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget


class Procesar_Pago(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=[
                           30, 80, 30, 30], spacing=20)

        # Título grande centrado
        titulo_grande = Label(text='Ingresar datos bancarios', halign='center',
                              valign='middle', size_hint=(1, None), height=40, font_size=50)
        layout.add_widget(titulo_grande)

        # Imagen grande centrada
        image_layout = BoxLayout(size_hint=(1, None), height=166)
        image = Image(source='Image/Formas_Pago.png',
                      size_hint=(None, None), size=(503, 166))
        # Añadir un widget vacío antes de la imagen
        image_layout.add_widget(Widget())
        image_layout.add_widget(image)
        # Añadir un widget vacío después de la imagen
        image_layout.add_widget(Widget())
        layout.add_widget(image_layout)

        # Cuadros de texto y etiquetas
        cuadros_layout = GridLayout(
            cols=2, spacing=10, size_hint_y=None, height=120)

        self.num_tarjeta_input = TextInput(multiline=False, input_type='number',
                                           hint_text='Número de tarjeta', size_hint_x=None, width=300, font_size=20)
        self.cvv_input = TextInput(multiline=False, input_type='number',
                                   hint_text='CVV', size_hint_x=None, width=300, font_size=20)

        # Layout para MM y AA
        vencimiento_layout = BoxLayout(
            orientation='horizontal', spacing=10, size_hint_x=None, width=210)
        self.mes_venc_input = TextInput(
            multiline=False, hint_text='MM', size_hint_x=None, width=145, font_size=20)
        self.anno_venc_input = TextInput(
            multiline=False, hint_text='AA', size_hint_x=None, width=145, font_size=20)
        vencimiento_layout.add_widget(self.mes_venc_input)
        vencimiento_layout.add_widget(self.anno_venc_input)

        cuadros_layout.add_widget(Label(
            text='Número de tarjeta:', halign='right', size_hint_x=None, width=300, font_size=20))
        cuadros_layout.add_widget(self.num_tarjeta_input)
        cuadros_layout.add_widget(
            Label(text='CVV:', halign='right', size_hint_x=None, width=300, font_size=20))
        cuadros_layout.add_widget(self.cvv_input)
        cuadros_layout.add_widget(Label(
            text='Fecha de vencimiento:', halign='right', size_hint_x=None, width=300, font_size=20))
        cuadros_layout.add_widget(vencimiento_layout)
        layout.add_widget(cuadros_layout)

        # Agregar los botones de Regresar y Pagar
        button_layout = GridLayout(cols=2, size_hint=(1, None), height=50)
        self.pagar_button = Button(
            text='Pagar', disabled=True, size_hint=(0.5, 1))
        self.pagar_button.bind(on_press=self.realizar_pago)
        regresar_button = Button(text='Regresar', size_hint=(0.5, 1))
        regresar_button.bind(on_press=self.go_to_carrito)

        button_layout.add_widget(regresar_button)
        button_layout.add_widget(self.pagar_button)

        # Se añade un espacio vacío para mantener los botones en la misma posición
        layout.add_widget(BoxLayout(size_hint_y=None, height=100))
        layout.add_widget(button_layout)

        self.add_widget(layout)

        # Vincular eventos de cambio de texto
        self.num_tarjeta_input.bind(text=self.on_text_input)
        self.cvv_input.bind(text=self.on_text_input)
        self.mes_venc_input.bind(text=self.on_text_input)
        self.anno_venc_input.bind(text=self.on_text_input)

    def on_text_input(self, instance, value):
        # Verificar si todos los campos están completos y tienen la longitud adecuada para habilitar el botón Pagar
        num_tarjeta_valid = len(self.num_tarjeta_input.text) == 16
        cvv_valid = len(self.cvv_input.text) == 3
        try:
            mes = int(self.mes_venc_input.text)
            mes_valid = 1 <= mes <= 12
        except ValueError:
            mes_valid = False

        try:
            anno = int(self.anno_venc_input.text)
            anno_valid = anno >= 24
        except ValueError:
            anno_valid = False

        if num_tarjeta_valid and cvv_valid and mes_valid and anno_valid:
            self.pagar_button.disabled = False
        else:
            self.pagar_button.disabled = True

    def go_to_carrito(self, instance):
        self.manager.current = 'carrito'

    def realizar_pago(self, instance):
        self.manager.current = 'Pedido'
