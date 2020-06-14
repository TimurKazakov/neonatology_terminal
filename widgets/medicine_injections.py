from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


root = Builder.load_string('''

<MedicineInjections>:  
    orientation: 'vertical'
    Label:
        text: root.title
        text_size: self.size
        halign: 'center'
        valign: 'middle'
    BoxLayout:       
        Label:
            text:  root.adrenaline_intravenously      
            text_size: self.size
            halign: 'center'
            valign: 'middle'
        Button
            text: 'Ввести'
            on_press: root.make_injection('адреналин в/в ') 
    BoxLayout:
        Label:
            text:  root.adrenaline_endotracheally
            text_size: self.size
            halign: 'center'
            valign: 'middle'
        Button
            text: 'Ввести'
            on_press: root.make_injection('адреналин э/т')     
    BoxLayout:
        Label:
            text: root.surfactant
            text_size: self.size
            halign: 'center'
            valign: 'middle'
        Button
            text: 'Ввести'
            on_press: root.make_injection('сурфактант') 
    BoxLayout:
        Label:
            text: root.saline
            text_size: self.size
            halign: 'center'
            valign: 'middle'
        Button
            text: 'Ввести'
            on_press: root.make_injection('физиологический раствор')  

''')

0
class MedicineInjections(BoxLayout):
    title = StringProperty('Из расчета массы тела 3,222 \n и гестационного периода 38 недель ')
    adrenaline_intravenously = StringProperty('Адреналин в/в')
    adrenaline_endotracheally = StringProperty('Адреналин э/т')
    saline = StringProperty('Физиологический раствор')
    surfactant = StringProperty(f'Сурфактант ст.д/пов.д ')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def make_injection(self, medicine):
        App.get_running_app().make_injection(medicine)
        self.update_recommendations()

    def update_recommendations(self):
        current_app = App.get_running_app()
        self.title = f'Из расчета массы тела {current_app.weight} \n и гестационного периода {current_app.gestation_period} недель'
        self.saline = f' Физиологический раствор в/в  \n' \
                                       f'{round(10*current_app.weight, 2)}мл'
        self.adrenaline_intravenously = f'Адреналин в/в \n' \
                                       f'{round(0.1*current_app.weight, 2)}мл-{round(0.3*current_app.weight, 2)}мл'
        self.adrenaline_endotracheally = f'Адреналин э/т \n' \
                                       f'{round(0.5*current_app.weight, 2)}мл-{round(1*current_app.weight, 2)}мл'

        self.surfactant = (f'Сурфактант ст.д/пов.д \n  '
                                f'Куросуф { round(1.25*current_app.weight, 2)}мл-{round(2.5*current_app.weight,2)}мл/{round(1.25*current_app.weight,2)}мл')


