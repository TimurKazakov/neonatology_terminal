from kivy.app import App
from kivy.lang import Builder

from kivy.uix.screenmanager import Screen

from widgets.Timer import Timer
from widgets.breathe_rate import BreatheRate
from widgets.heart_rate import HeartRate
from widgets.muscle_tone import MuscleTone
from widgets.reflexes import Reflexes
from widgets.patient_layout import PatientLayout
from widgets.recommendations import Recommendations
from widgets.log_widget import LogWidget
from widgets.medicine_injections import MedicineInjections
from widgets.skin_coloring import SkinColoring

root = Builder.load_string('''

<ReanimationScreen>:       
    GridLayout:       
        rows: 3
        GridLayout:
            size_hint: 1, .25
            canvas.before:
                Color:
                    rgba: .5, .5, .5, 1
                Line:
                    width: 2
                    rectangle: self.x, self.y, self.width, self.height        
            cols: 3
            
            BoxLayout:
                id: patient_layer
                orientation: 'vertical'                
                # Label:
                #     text:'Вес'                    
                # TextInput:
                #     id: weight
                # BoxLayout:
                #     Label:
            BoxLayout:
                id: timer_layout
            BoxLayout:
                orientation: 'vertical'
                id: apgar_layout                     
        
        Separator:
            rgba: 0.7, 0.7, 0.7, 1 
            size_hint: 1,0.025              
        BoxLayout:
            orientation: 'horizontal'
            canvas.before:
                Color:
                    rgba: .5, .5, .5, 1
                Line:
                    width: 2
                    rectangle: self.x, self.y, self.width, self.height
           
            BoxLayout:
                orientation: 'vertical'
                BoxLayout:
                    orientation: 'horizontal'
                    BoxLayout:
                        orientation: 'vertical'
                        BoxLayout:
                            BoxLayout:
                                id: heart_rate_id                                
                        Separator:
                            rgba: 0.7, 0.7, 0.7, 1
                            size_hint:  1, 0.025     
                        BoxLayout:
                            BoxLayout:
                                id : respiration_rate_id                           
                    Separator:
                        rgba: 0.7, 0.7, 0.7, 1
                        size_hint:  0.025,1               
                    BoxLayout:                    
                        Recommendations:
                             
                Separator:
                    rgba: 0.7, 0.7, 0.7, 1
                    size_hint: 1, 0.025 
                BoxLayout:
                    orientation: 'horizontal'                    
                    LogWidget:
                        id: log_widget_id
                      
                     
                        
            Separator:
                rgba: 0.7, 0.7, 0.7, 1
                size_hint: 0.025,1 
            MedicineInjections:
                id: medicine_injections_id
                size_hint:  .30, 1                

''')


class ReanimationScreen(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.ids['timer_layout'].add_widget(Timer())
        self.ids['apgar_layout'].add_widget(SkinColoring(cols=3, rows=1))
        self.ids['apgar_layout'].add_widget(MuscleTone(cols=3, rows=1))
        self.ids['apgar_layout'].add_widget(Reflexes(cols=3, rows=1))
        self.ids['respiration_rate_id'].add_widget(BreatheRate(cols=3, rows=1))
        self.ids['heart_rate_id'].add_widget(HeartRate(cols=3, rows=1))
        self.ids['patient_layer'].add_widget(PatientLayout())


    def update(self, text):
        self.ids['log_widget_id'].update(text)

    def make_injection(self, text):
        self.ids['log_widget_id'].make_injection(text)

    def update_child_info(self,):

        self.ids['medicine_injections_id'].update_recommendations()
