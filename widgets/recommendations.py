import datetime

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

Builder.load_string('''
<Recommendations>:
    Label:
        padding_x: 20
        size_hint_y: None
        height: self.texture_size[1]
        text_size: self.width, None
        text: root.text
''')

class Recommendations(ScrollView):
    text = StringProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = f'• Положить на реанимационный столик на спину, головой к врачу \n'\
                    f'• Определить признаки живорождения \n'\
                    f'• Ребенка помесить в пластиковый мешок или пленку, обсушивание не проводится. \n'\
                    f'• Подключить температурный датчик, пульсоксиметр/ЭКГ \n'\
                    f'• Провести санацию верхних дыхательных путей (по необходимости) \n'\
                    f'• Мероприятия начаты в {datetime.timedelta(seconds=App.get_running_app().seconds)} \n'


