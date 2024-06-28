from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from Screen.Bienvenida import Bienvenida
from Screen.Menu_Alimentos import Menu_Alimentos


class InicioApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        # Agregar las pantallas al ScreenManager
        self.screen_manager.add_widget(Bienvenida(name='bienvenida'))
        self.screen_manager.add_widget(Menu_Alimentos(name='menu_alimentos'))

        # Mostrar la pantalla de bienvenida al inicio
        self.screen_manager.current = 'bienvenida'

        return self.screen_manager


if __name__ == '__main__':
    InicioApp().run()
