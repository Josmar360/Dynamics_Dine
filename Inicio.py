from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from Screen.Seleccion_Mesa import Seleccion_Mesa
from Screen.Bienvenida import Bienvenida
from Screen.Menu_Alimentos import Menu_Alimentos
from Screen.Carrito_Compras import Carrito_Compras
from Screen.Procesar_Pago import Procesar_Pago
from Screen.Realizar_Pedido import Realizar_Pedido
from Screen.Estatus_Pedido import Estatus_Pedido


class InicioApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        # Agregar las pantallas al ScreenManager
        self.screen_manager.add_widget(Seleccion_Mesa(name='mesa'))
        self.screen_manager.add_widget(Bienvenida(name='bienvenida'))
        self.screen_manager.add_widget(Menu_Alimentos(name='menu_alimentos'))
        self.screen_manager.add_widget(Carrito_Compras(name='carrito'))
        self.screen_manager.add_widget(Procesar_Pago(name='pagar'))
        self.screen_manager.add_widget(Realizar_Pedido(name='realizar_pedido'))
        self.screen_manager.add_widget(Estatus_Pedido(name='estatus'))

        # Mostrar la pantalla de seleccion de mesa al inicio
        self.screen_manager.current = 'mesa'

        return self.screen_manager


if __name__ == '__main__':
    InicioApp().run()
