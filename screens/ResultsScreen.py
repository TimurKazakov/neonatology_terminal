from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from widgets.result_patient_layout import ResultPatientLayout
from widgets.result_apgar_layout import ResultApgarLayout
from widgets.recommendations import Recommendations
from widgets.born_status import BornStatus
root = Builder.load_string(''' 
<ResultScreen>:
    BoxLayout:
        orientation: 'vertical'        
        ResultPatientLayout:        
        Separator:
            rgba: 0.7, 0.7, 0.7, 1
            size_hint: 1, 0.025 
        BoxLayout:
            ResultApgarLayout:
            
        Separator:
            rgba: 0.7, 0.7, 0.7, 1
            size_hint: 1, 0.025
        BoxLayout: 
            Recommendations:
            Separator:
                rgba: 0.7, 0.7, 0.7, 1
                size_hint:  0.025, 1 
            BornStatus:
        Separator:
            rgba: 0.7, 0.7, 0.7, 1
            size_hint: 1, 0.025 
        GridLayout: 
            cols: 3
            size_hint: 1, 0.5 
            Button:
                text: 'Редактировать'
            Button:
                text: 'Синхронизировать'
            Button:
                text: 'Распечатать'
        
        

''')


class ResultScreen(Screen):
    result = StringProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.result = '/0'

