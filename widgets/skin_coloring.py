from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.gridlayout import GridLayout

root = Builder.load_string('''

<SkinColoring>:
    rows : 2
    canvas.before:
        Color:
            rgba: .5, .5, .5, 1
        Line:
            width: 2
            rectangle: self.x, self.y, self.width, self.height
    Label:
        text: 'Окраска кожи'    
    GridLayout:
        cols: 3
        ToggleButton:
            text: 'Цианоз'
            group: 'skin_coloring'
            on_press: root.update_apgar('0');
            id: none-color
        ToggleButton:
            text: 'Акроцианоз'
            group: 'skin_coloring'
            on_press: root.update_apgar('1');
            id: weak-color
        ToggleButton:
            text: 'Норма' 
            group: 'skin_coloring'
            on_press:root.update_apgar('2');
            id: strong-color



''')


class SkinColoring(GridLayout):
    apgar = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.apgar = '0'

    def reset_data(self):
        #  values так как там dict с id {id: instance}
        for item in self.ids.values():
            item.state = 'normal'

    def update_apgar(self, apgar):
        self.apgar = apgar
        current_app = App.get_running_app()
        current_app.change_field = 'цвет кожных покровов'
        current_app.skin_coloring_apgar = apgar
        current_app.calc_apgar()
        current_app.update_log(apgar)
