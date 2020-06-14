import datetime

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

Builder.load_string('''
<BornStatus>:
    TextInput:
        padding_x: 20
            
        text_size: self.width, None
        text: root.text
            
''')

class BornStatus(ScrollView):
    text = StringProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text =\
            f'  Пороки развития ______________________________________________\n'\
            f'  Родовые травмы _______________________________________________ \n' \
            f'  Профилактика гонобленореи (название медикамента, часы) _______ \n' \
            f'  ______________________________________________________________ \n' \
            f'  Дежурная акушерка ________________ Дежурный врач _____________ \n' \
            f'  Ребенок переведен в отделение новорожденных _________ 20.. г. \n' \
            f'  ______________ час. _________ мин.          дата перевода \n' \
            f'  Состояние ребенка при переводе из родзала ____________________ \n' \
            f'  _____________________ цвет кожных покровов, характер крика ___ \n' \
            f'  ______________________________________________________________ \n' \
            f'  Ребенка сдала акушерка _______________________________________ \n' \
            f'  Приняла и провела обработку мед. сестра ______________________ \n' \
            f'  Диагноз предварительный ______________________________________ \n' \
            f'  ______________________________________________________________ \n' \
            f'  Диагноз заключительный _______________________________________ \n' \
