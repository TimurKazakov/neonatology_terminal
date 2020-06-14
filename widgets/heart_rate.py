from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.gridlayout import GridLayout

root = Builder.load_string('''

<HeartRate>:   
    rows : 3
    canvas.before:
        Color:
            rgba: .5, .5, .5, 1
        Line:
            width: 2
            rectangle: self.x, self.y, self.width, self.height
    Label:
        text: 'Частота сердечных сокращений'
        text_size: self.size
        halign: 'center'
        valign: 'middle'   
    GridLayout:
        cols: 3
        ToggleButton:
            text: 'меньше 60'
            group: 'breathe'
            id: button0
            on_press: root.update_heart_rate(0)
        ToggleButton:
            text: 'больше 60'
            on_press: root.update_heart_rate(60)
            group: 'breathe'         
            id: button60   
        ToggleButton:
            text: 'больше 100' 
            on_press: root.update_heart_rate(100)     
            group: 'breathe'
            id: button100


''')


class HeartRate(GridLayout):
    heart_rate = StringProperty()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.heart_apgar = '0'

    def reset_data(self):
        self.heart_rate = f''
        #  values так как там dict с id {id: instance}
        for item in self.ids.values():
            item.state = 'normal'

    def update_heart_rate(self, heart_apgar):

        self.heart_rate = f'{heart_apgar}'
        if heart_apgar == 0:
            self.heart_apgar = 0
        elif heart_apgar == 60:
            self.heart_apgar = 1
        else:
            self.heart_apgar = 2
        current_app = App.get_running_app()
        current_app.change_field = 'частота сердечных сокращений'
        current_app.heart_rate_apgar = self.heart_apgar
        current_app.calc_apgar()
        current_app.update_log(self.heart_apgar)


