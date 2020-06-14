from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.gridlayout import GridLayout

root = Builder.load_string('''

<Results>:
    rows : 3
    canvas.before:
        Color:
            rgba: .5, .5, .5, 1
        Line:
            width: 2
            rectangle: self.x, self.y, self.width, self.height
    BoxLayout:
        Label:
            text: 'Апгар 1 минуты' 
        Label:
            text: root.apgar_1
    BoxLayout:
        Label:
            text: 'Апгар 5 минуты' 
        Label:
            text: root.apgar_5
               
    BoxLayout
        Label:            
            text: root.actions



''')


class Results(GridLayout):
    actions = StringProperty()
    apgar_1 = StringProperty()
    apgar_5= StringProperty()
    price = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.actions = 'Исход положительный'
        self.actions = 'Состояние тяжелое'
        self.apgar_1 = f'0'
        self.apgar_5 = f'5'

    def update(self):
        self.apgar_1 = str(App.get_running_app().apgar_1)
        self.apgar_5 = str(App.get_running_app().apgar_5)
