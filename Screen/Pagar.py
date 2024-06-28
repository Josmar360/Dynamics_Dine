from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from Screen.Menu_Alimentos import selected_products


class Pagar(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update_screen()

    def update_screen(self):
        # Clear previous widgets
        self.clear_widgets()

        # Scroll view for the product list
        scrollview = ScrollView(size_hint=(
            1, None), size=(Window.width, Window.height))

        # Layout to display selected products
        layout = GridLayout(cols=2, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        total = 0.0

        # Loop through selected_products to display each product
        for product in selected_products.values():
            if product['quantity'] > 0:
                subtotal = product['quantity'] * product['price']
                total += subtotal

                product_layout = GridLayout(
                    cols=1, padding=10, spacing=10, size_hint_y=None, height=300)

                product_layout.add_widget(
                    Image(source=product['image'], size_hint=(1, 0.8)))
                product_layout.add_widget(
                    Label(text=product['name'], size_hint=(1, 0.1)))
                product_layout.add_widget(
                    Label(text=f"Precio: ${product['price']:.2f}", size_hint=(1, 0.1)))
                product_layout.add_widget(
                    Label(text=f"Cantidad: {product['quantity']}", size_hint=(1, 0.1)))
                product_layout.add_widget(
                    Label(text=f"Subtotal: ${subtotal:.2f}", size_hint=(1, 0.1)))

                layout.add_widget(product_layout)

        layout.add_widget(Label(text=f"Total a Pagar: ${
                          total:.2f}", font_size='24sp', size_hint_y=20, height=40))

        scrollview.add_widget(layout)

        # Back button
        back_button = Button(text='Regresar', size_hint=(1, None), height=50)
        back_button.bind(on_press=self.go_back)

        # Adding widgets to the screen
        self.add_widget(scrollview)
        self.add_widget(back_button)

    def go_back(self, instance):
        self.manager.current = 'menu_alimentos'

    def on_pre_enter(self):
        self.update_screen()
