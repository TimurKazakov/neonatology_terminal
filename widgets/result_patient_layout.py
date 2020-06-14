from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

root = Builder.load_string('''

<ResultPatientLayout>:   
    cols : 13
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Пол'
        BoxLayout:
            orientation: 'vertical'
            ToggleButton:
                group: 'gender'
                text: 'М'
            ToggleButton:
                text: 'Ж'
                group: 'gender'
    Separator:
        rgba: 0.7, 0.7, 0.7, 1
        size_hint: 0.025, 1
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Рождение'
        BoxLayout:
            orientation: 'vertical'
            ToggleButton:
                text: 'Живой'
                group: 'born_status'
            ToggleButton:
                text: 'Мертвый'
                group: 'born_status'
    Separator:
        rgba: 0.7, 0.7, 0.7, 1
        size_hint: 0.025, 1
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Неделя гестации'
        TextInput:
    Separator:
        rgba: 0.7, 0.7, 0.7, 1
        size_hint: 0.025, 1            
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Масса'
        TextInput:
    Separator:
        rgba: 0.7, 0.7, 0.7, 1
        size_hint: 0.025, 1            
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Рост'
        TextInput:
    Separator:
        rgba: 0.7, 0.7, 0.7, 1
        size_hint: 0.025, 1            
    BoxLayout:
        orientation: 'vertical'        
        Label:
            text: 'Окружность'
        BoxLayout:
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: 'головы'
                TextInput: 
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: 'груди'
                TextInput: 
    Separator:
        rgba: 0.7, 0.7, 0.7, 1
        size_hint: 0.025, 1
    BoxLayout:
        orientation: 'vertical'    
        Label:
            text: 'Асфиксия'  
        BoxLayout:
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: 'продолжитель.'
                    
                TextInput: 
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: 'меры оживл.'
                TextInput:     
                           
''')

class ResultPatientLayout(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)