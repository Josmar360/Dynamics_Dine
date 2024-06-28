from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
import mysql.connector

# Configuración de la base de datos
configuracion = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Sarinha_3',
    'database': 'Dynamics_Dine'
}


class ProductCard(BoxLayout):
    def __init__(self, product_name, product_image, product_price, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        self.size_hint_y = None
        self.height = 300

        self.product_name = product_name
        self.product_image = product_image
        self.product_price = product_price
        self.quantity = 0

        # Ajustar el tamaño de la imagen
        self.image = Image(source=product_image, size_hint=(1, 0.8))
        self.add_widget(self.image)

        self.add_widget(Label(text=product_name, size_hint=(1, 0.1)))
        self.add_widget(
            Label(text=f"Precio: ${product_price:.2f}", size_hint=(1, 0.1)))

        control_layout = BoxLayout(size_hint=(1, 0.2), spacing=10)

        self.quantity_label = Label(
            text=str(self.quantity), size_hint=(0.2, 1))
        self.add_button = Button(text='+', size_hint=(0.4, 1))
        self.add_button.bind(on_press=self.increment_quantity)
        self.subtract_button = Button(text='-', size_hint=(0.4, 1))
        self.subtract_button.bind(on_press=self.decrement_quantity)

        control_layout.add_widget(self.subtract_button)
        control_layout.add_widget(self.quantity_label)
        control_layout.add_widget(self.add_button)

        self.add_widget(control_layout)

    def increment_quantity(self, instance):
        self.quantity += 1
        self.quantity_label.text = str(self.quantity)

    def decrement_quantity(self, instance):
        if self.quantity > 0:
            self.quantity -= 1
            self.quantity_label.text = str(self.quantity)


class RestaurantMenuApp(App):
    def build(self):
        tab_panel = TabbedPanel(size_hint=(1, 1))

        # Conectar a la base de datos
        conn = mysql.connector.connect(**configuracion)
        cursor = conn.cursor(dictionary=True)

        # Consulta para obtener los datos
        cursor.execute("""
            SELECT P.FK_Platillo, P.Platillos, P.Precios, TP.Tipo_Platillo
            FROM Platillos P
            JOIN Tipo_Platillo TP ON P.FK_Tipo_Platillo = TP.PK_Tipo_Platillo
        """)

        results = cursor.fetchall()
        conn.close()

        # Organizar los datos en categorías
        categories = {
            'Platillo': [],
            'Bebida': [],
            'Extra': [],
            'Postres': []
        }

        for row in results:
            product = {
                'name': row['Platillos'],
                'image': f"Image/{row['FK_Platillo']}.jpg",
                'price': row['Precios']
            }
            categories[row['Tipo_Platillo']].append(product)

        for category, products in categories.items():
            tab = TabbedPanelItem(text=category)
            scrollview = ScrollView(size_hint=(
                1, None), size=(Window.width, Window.height))
            layout = GridLayout(cols=2, spacing=10, size_hint_y=None)
            layout.bind(minimum_height=layout.setter('height'))
            for product in products:
                layout.add_widget(ProductCard(
                    product_name=product['name'], product_image=product['image'], product_price=product['price']))
            scrollview.add_widget(layout)
            tab.add_widget(scrollview)
            tab_panel.add_widget(tab)

        return tab_panel


if __name__ == '__main__':
    RestaurantMenuApp().run()
