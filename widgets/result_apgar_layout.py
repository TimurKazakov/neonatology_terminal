from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.gridlayout import GridLayout

root = Builder.load_string('''
<ResultApgarLayout>:
    rows: 3
    BoxLayout:
        Label:
            text: 'Минута'
        Separator:
            rgba: 0.7, 0.7, 0.7, 1
            size_hint: 0.025, 1
        Label:
            text: 'Сердцебиение'
        Separator:
            rgba: 0.7, 0.7, 0.7, 1
            size_hint: 0.025, 1
        Label:
            text: 'Дыхание'
        Separator:
            rgba: 0.7, 0.7, 0.7, 1
            size_hint: 0.025, 1
        Label:
            text: 'Окраска кожи'
        Separator:
            rgba: 0.7, 0.7, 0.7, 1
            size_hint: 0.025, 1
        Label:
            text: 'Тонус мышц'
        Separator:
            rgba: 0.7, 0.7, 0.7, 1
            size_hint: 0.025, 1
        Label:
            text: 'Рефлексы'
        Separator:
            rgba: 0.7, 0.7, 0.7, 1
            size_hint: 0.025, 1
        Label:
            text: 'Всего'
        Separator:
            rgba: 0.7, 0.7, 0.7, 1
            size_hint: 0.025, 1
    BoxLayout:
        Label:
            text: '1 мин'
        Separator:
            rgba: 0.7, 0.7, 0.7, 1
            size_hint: 0.025, 1
        Label:
            text: '2'
        Separator:
            rgba: 0.7, 0.7, 0.7, 1
            size_hint: 0.025, 1
        Label:
            text: '2'
        Separator:
            rgba: 0.7, 0.7, 0.7, 1
            size_hint: 0.025, 1
        Label:
            text: '2'
        Separator:
            rgba: 0.7, 0.7, 0.7, 1
            size_hint: 0.025, 1
        Label:
            text: '2'
        Separator:
            rgba: 0.7, 0.7, 0.7, 1
            size_hint: 0.025, 1
        Label:
            text: '2'
        Separator:
            rgba: 0.7, 0.7, 0.7, 1
            size_hint: 0.025, 1
        Label:
            text: '10'
        Separator:
            rgba: 0.7, 0.7, 0.7, 1
            size_hint: 0.025, 1
    BoxLayout:
        Label:
            text: '5 мин'
        Separator:
            rgba: 0.7, 0.7, 0.7, 1
            size_hint: 0.025, 1
        Label:
            text: '2'
        Separator:
            rgba: 0.7, 0.7, 0.7, 1
            size_hint: 0.025, 1
        Label:
            text: '2'
        Separator:
            rgba: 0.7, 0.7, 0.7, 1
            size_hint: 0.025, 1
        Label:
            text: '2'
        Separator:
            rgba: 0.7, 0.7, 0.7, 1
            size_hint: 0.025, 1
        Label:
            text: '2'
        Separator:
            rgba: 0.7, 0.7, 0.7, 1
            size_hint: 0.025, 1
        Label:
            text: '2'
        Separator:
            rgba: 0.7, 0.7, 0.7, 1
            size_hint: 0.025, 1
        Label:
            text: '10'
        Separator:
            rgba: 0.7, 0.7, 0.7, 1
            size_hint: 0.025, 1
        



''')


class ResultApgarLayout(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)