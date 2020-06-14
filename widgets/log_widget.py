import datetime

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

Builder.load_string('''
<LogWidget>:
    Label:
        padding_x: 20
        size_hint_y: None
        height: self.texture_size[1]
        text_size: self.width, None
        text: root.text
''')

class LogWidget(ScrollView):
    text = StringProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = f'• Мероприятия начаты в {datetime.timedelta(seconds=App.get_running_app().seconds)} \n'

    def make_injection(self, medicine):
        self.text += f'{str(datetime.timedelta(seconds=App.get_running_app().seconds))} ' \
                     f'Был введен  {medicine} \n' \


    def update(self, code):
        self.text += f'{str(datetime.timedelta(seconds=App.get_running_app().seconds))} ' \
                     f'Изменилось(лся) {App.get_running_app().change_field} на {code} по шкале Апгар. ' \
                     f'Текущий Апгар: {App.get_running_app().apgar_current} \n'

