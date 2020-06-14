from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.gridlayout import GridLayout

root = Builder.load_string('''

<MuscleTone>:
    rows : 2
    canvas.before:
        Color:
            rgba: .5, .5, .5, 1
        Line:
            width: 2
            rectangle: self.x, self.y, self.width, self.height
    Label:
        text: 'Мышечный тонус'    
    GridLayout:
        cols: 5
        ToggleButton:
            text: 'Отсутвует'
            group: 'muscle_tone'
            on_press: root.update_apgar('0'); 
            id: none-tone
        ToggleButton:
            text: 'Слабый'
            group: 'muscle_tone'
            on_press:  root.update_apgar('1'); 
            id:weak-tone
        ToggleButton:
            text: 'Норма' 
            group: 'muscle_tone'
            on_press: root.update_apgar('2'); 
            id:normal-tone


''')


class MuscleTone(GridLayout):
    apgar = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.apgar='0'

    def reset_data(self):
        #  values так как там dict с id {id: instance}
        for item in self.ids.values():
            item.state = 'normal'

    def update_apgar(self, apgar):
        self.apgar = apgar
        current_app = App.get_running_app()
        current_app.change_field = 'мышечный тонус'
        current_app.muscle_tone_apgar = apgar
        current_app.calc_apgar()
        current_app.update_log(apgar)
