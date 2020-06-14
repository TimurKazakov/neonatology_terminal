from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

root = Builder.load_string('''

<PatientLayout>:   
    orientation: 'vertical'
    BoxLayout:
        size_hint: 1,0.5
        Label:
            text:'Вес'
            text_size: self.size
            halign: 'center'
            valign: 'center'
        TextInput:
            text: root.child_weight            
            multiline: False
            input_filter: "float"
            size_hint: None, None
            size: dp(200), dp(40)
            halign: 'center'
            valign: 'middle'
            on_text: root.change_weight(self.text)
           
    BoxLayout:
        size_hint: 1,0.5
        Label:
            text:'Рост'
            text_size: self.size
            halign: 'center'
            valign: 'center'
            
        TextInput:
            text: root.child_height
            multiline: False
            input_filter: "float"
            size_hint: None, None
            size: dp(200), dp(40)
            halign: 'center'
            valign: 'middle'
            on_text : root.change_height(self.text)
            
    BoxLayout:
        size_hint: 1,0.5
        Label:
            text:'Неделя гестации'
            text_size: self.size
            halign: 'center'
            valign: 'center'
        TextInput:
            text: root.gestation_period
            multiline: False
            input_filter: "int"
            size_hint: None, None
            size: dp(200), dp(40)
            halign: 'center'
            valign: 'middle'
            on_text : root.change_gestation_period(self.text)
            
    

''')


class PatientLayout(BoxLayout):
    child_weight = ObjectProperty('0')
    child_height = ObjectProperty('0')
    gestation_period = ObjectProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update_child_info(self):
        current_app = App.get_running_app()
        self.child_weight = current_app.weight
        self.child_height = current_app.height
        self.gestation_period = current_app.gestation_period

    def change_weight(self, weight):
        try:
            App.get_running_app().weight = round(float(weight), 3)
        except:
            self.child_weight = 0
        App.get_running_app().update_child_info()

    def change_height(self, height):
        try:
            App.get_running_app().height = round(float(height), 2)
        except:
            self.child_height = 0

        App.get_running_app().update_child_info()

    def change_gestation_period(self, gestation_period):
        try:
            App.get_running_app().gestation_period = gestation_period
        except:
            self.gestation_period = 0
        App.get_running_app().update_child_info()