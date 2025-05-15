import sys, os
sys.path.append(os.path.join(os.path.expanduser("~"), ".kivy", "garden", "garden.mapview"))
from mapview import MapView
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.factory import Factory


class HomeScreen(Screen):
    pass

class ExploreScreen(Screen):
    pass

class MapScreen(Screen):
    pass

class InfoScreen(Screen):
    pass

class DetailScreen(Screen):
    title = StringProperty()
    image = StringProperty()
    description = StringProperty()


class TouristCard(BoxLayout):
    title = StringProperty()
    image = StringProperty()
    short_description = StringProperty()
    full_description = StringProperty()

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            app = App.get_running_app()
            screen = app.root.get_screen('detail')
            screen.title = self.title
            screen.image = self.image
            screen.description = self.full_description
            app.root.current = 'detail'
        return super().on_touch_up(touch)


Factory.register('TouristCard', cls=TouristCard)

class TouristApp(App):
    def build(self):
        return Builder.load_file("interface.kv")

if __name__ == '__main__':
    TouristApp().run()
