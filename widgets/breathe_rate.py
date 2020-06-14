from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.gridlayout import GridLayout

root = Builder.load_string('''

<BreatheRate>:   
    rows : 3
    canvas.before:
        Color:
            rgba: .5, .5, .5, 1
        Line:
            width: 2
            rectangle: self.x, self.y, self.width, self.height
    Label:
        text: 'Частота дыхания' 
        text_size: self.size
        halign: 'center'
        valign: 'middle'  
    GridLayout:
        cols: 3
        ToggleButton:
            text: 'меньше 20'
            group: 'breathe'
            id: button20
            on_press: root.update_breathe_rate(20)
        ToggleButton:
            text: 'меньше 40'
            on_press: root.update_breathe_rate(40)
            group: 'breathe'         
            id: button40   
        ToggleButton:
            text: 'больше 40' 
            on_press: root.update_breathe_rate(60)     
            group: 'breathe'
            id: button60


''')


class BreatheRate(GridLayout):
    breathe_rate = StringProperty()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.breathe_apgar = '0'

    def reset_data(self):
        self.breathe_rate = f''
        #  values так как там dict с id {id: instance}
        for item in self.ids.values():
            item.state = 'normal'

    def update_breathe_rate(self, breath_rate):

        self.breathe_rate = f'{breath_rate}'
        if breath_rate <= 20:
            self.breathe_apgar = 0
        elif 20 <= breath_rate <= 40:
            self.breathe_apgar = 1
        else:
            self.breathe_apgar = 2
        current_app = App.get_running_app()
        current_app.change_field = 'частота дыхательных движениц'
        current_app.breathe_apgar = self.breathe_apgar
        current_app.calc_apgar()
        current_app.update_log(self.breathe_apgar)


