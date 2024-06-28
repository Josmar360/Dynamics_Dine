# Procesar_Pago.py

from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image


class Procesar_Pago(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Layout principal
        layout = GridLayout(cols=2, spacing=10, padding=[50, 100])

        # Título grande centrado
        titulo_grande = Label(text='Ingresar datos bancarios', halign='center',
                              valign='middle', size_hint=(1, None), height=100, font_size=28)
        layout.add_widget(titulo_grande)

        # Imagen grande centrada
        image = Image(source='bank_icon.png', size_hint=(
            None, None), size=(200, 200), pos_hint={'center_x': 0.5})
        layout.add_widget(image)

        # Cuadros de texto y etiquetas
        cuadros_layout = GridLayout(
            cols=2, spacing=10, size_hint_y=None, height=200)

        self.num_tarjeta_input = TextInput(multiline=False, input_type='number',
                                           hint_text='Número de tarjeta', size_hint_x=None, width=300, font_size=20)
        self.cvv_input = TextInput(multiline=False, input_type='number',
                                   hint_text='CVV', size_hint_x=None, width=200, font_size=20)
        self.mes_venc_input = TextInput(
            multiline=False, hint_text='MM', size_hint_x=None, width=100, font_size=20)
        self.anno_venc_input = TextInput(
            multiline=False, hint_text='AA', size_hint_x=None, width=100, font_size=20)

        cuadros_layout.add_widget(Label(
            text='Número de tarjeta:', halign='right', size_hint_x=None, width=300, font_size=20))
        cuadros_layout.add_widget(self.num_tarjeta_input)
        cuadros_layout.add_widget(
            Label(text='CVV:', halign='right', size_hint_x=None, width=200, font_size=20))
        cuadros_layout.add_widget(self.cvv_input)
        cuadros_layout.add_widget(Label(
            text='Fecha de vencimiento:', halign='right', size_hint_x=None, width=200, font_size=20))
        cuadros_layout.add_widget(self.mes_venc_input)
        cuadros_layout.add_widget(self.anno_venc_input)

        layout.add_widget(cuadros_layout)

        # Botón Pagar (inicialmente deshabilitado)
        self.pagar_button = Button(text='Pagar', disabled=True, size_hint=(
            None, None), width=200, height=50, font_size=20)
        self.pagar_button.bind(on_press=self.realizar_pago)
        layout.add_widget(self.pagar_button)

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
        mes_valid = len(self.mes_venc_input.text) == 2
        anno_valid = len(self.anno_venc_input.text) == 2

        if num_tarjeta_valid and cvv_valid and mes_valid and anno_valid:
            self.pagar_button.disabled = False
        else:
            self.pagar_button.disabled = True

    def realizar_pago(self, instance):
        # Implementar la lógica para procesar el pago aquí
        numero_tarjeta = self.num_tarjeta_input.text
        cvv = self.cvv_input.text
        fecha_vencimiento = f"{
            self.mes_venc_input.text}/{self.anno_venc_input.text}"

        # Ejemplo: solo imprimimos los datos ingresados
        print(f"Número de tarjeta: {numero_tarjeta}")
        print(f"CVV: {cvv}")
        print(f"Fecha de vencimiento: {fecha_vencimiento}")
