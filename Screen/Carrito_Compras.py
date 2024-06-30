from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from Screen.Menu_Alimentos import selected_products

# Variable global para almacenar el total a pagar
total_a_pagar = 0.0


class Carrito_Compras(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update_screen()

    def update_screen(self):
        # Limpiar widgets previos
        self.clear_widgets()

        # Scroll view para la lista de productos
        scrollview = ScrollView(size_hint=(1, None), size=(
            Window.width, Window.height - 20))

        # Diseño para mostrar los productos seleccionados
        layout = GridLayout(cols=3, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        # Reiniciar el total
        global total_a_pagar
        total_a_pagar = 0.0

        # Recorrer selected_products para mostrar cada producto en la pantalla
        for product in selected_products.values():
            if product['quantity'] > 0:
                subtotal = product['quantity'] * product['price']
                total_a_pagar += subtotal

                product_layout = GridLayout(
                    cols=1, padding=10, spacing=10, size_hint_y=None, height=300)

                product_layout.add_widget(
                    Image(source=product['image'], size_hint=(1, 0.6)))
                product_layout.add_widget(
                    Label(text=product['name'], size_hint=(1, 0.1)))
                product_layout.add_widget(
                    Label(text=f"Precio: ${product['price']:.2f}", size_hint=(1, 0.1)))
                product_layout.add_widget(
                    Label(text=f"Cantidad: {product['quantity']}", size_hint=(1, 0.1)))
                product_layout.add_widget(
                    Label(text=f"Subtotal: ${subtotal:.2f}", size_hint=(1, 0.1)))

                layout.add_widget(product_layout)

        scrollview.add_widget(layout)

        # Etiqueta de Total a pagar
        total_label = Label(text=f"Total a Pagar: ${
                            total_a_pagar:.2f}", font_size='24sp', size_hint_y=None, height=50, halign='center', valign='middle')
        total_label.bind(size=total_label.setter(
            'text_size'))  # Asegurar que el texto esté centrado
        # Diseño para la etiqueta de total
        bottom_layout = GridLayout(cols=1, size_hint_y=None, height=100)
        bottom_layout.add_widget(total_label)

        # Agregar widgets a la pantalla
        self.add_widget(scrollview)
        self.add_widget(bottom_layout)

        # Agregar los botones de Regresar y Pagar
        button_layout = GridLayout(cols=2, size_hint=(1, None), height=50)
        regresar_button = Button(text='Regresar', size_hint=(0.5, 1))
        regresar_button.bind(on_press=self.go_to_menu_alimentos)
        pagar_button = Button(text='Pagar', size_hint=(0.5, 1))
        pagar_button.bind(on_press=self.go_to_pagar)

        button_layout.add_widget(regresar_button)
        button_layout.add_widget(pagar_button)

        self.add_widget(button_layout)

    # Función para ir a la pantalla de pago y actualizar el precio total en el pedido realizado 
    def go_to_pagar(self, instance):
        self.manager.current = 'realizar_pedido'
        self.manager.get_screen('realizar_pedido').actualizar_precio_total(total_a_pagar)


        self.manager.current = 'pagar'
    
    # Función para regresar el menu de alimentos
    def go_to_menu_alimentos(self, instance):
        self.manager.current = 'menu_alimentos'

    # Actualizar la pantalla
    def on_pre_enter(self):
        self.update_screen()
