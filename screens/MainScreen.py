

from kivy._event import EventDispatcher
from kivy.app import App
from kivy.clock import Clock, ClockBase, ClockBaseBehavior
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from libs.garden.backend_kivyagg import FigureCanvasKivyAgg

import matplotlib.pyplot as plt


from widgets.Timer import Timer
from widgets.breathe_rate import BreatheRate
from widgets.muscle_tone import MuscleTone
from widgets.reflexes import Reflexes
from widgets.results import Results
from widgets.skin_coloring import SkinColoring

root = Builder.load_string('''
<Separator@Widget>:
    rgba: .5, .5, .5, 1
    canvas:
        Color:
            rgba: self.rgba
        Rectangle:
            pos: self.pos
            size: self.size
            
<MainScreen>:
    layer_1_id: layer_1
    layer_2_id: layer_2
    layer_3_id: layer_3
    story_number : story_number
    GridLayout:       
        rows: 5
        GridLayout:
            canvas.before:
                Color:
                    rgba: .5, .5, .5, 1
                Line:
                    width: 2
                    rectangle: self.x, self.y, self.width, self.height        
            cols: 3
            id: layer_1
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text:'Номер истории родов'                    
                TextInput:
                    id: story_number
                Label:     
        Separator:
            rgba: 0.7, 0.7, 0.7, 1 
            size_hint: 1,0.025              
        GridLayout:
            canvas.before:
                Color:
                    rgba: .5, .5, .5, 1
                Line:
                    width: 2
                    rectangle: self.x, self.y, self.width, self.height
            id: layer_2
            cols: 5         
        Separator:
            rgba: 0.7, 0.7, 0.7, 1
            size_hint: 1,0.025     
        GridLayout:
            id: layer_3
            cols:3           
               

''')


class MainScreen(Screen):
    layer_1_id = ObjectProperty()
    layer_2_id = ObjectProperty()
    layer_3_id = ObjectProperty()
    story_number = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.timer = Timer()
        self.start_btn = None
        self.stop_btn = None
        self.reset_btn = None
        self.event = None
        self.layer_1_id.add_widget(self.timer)
        self.start_btn = Button(text='Старт')
        self.layer_1_id.add_widget(self.start_btn)
        self.start_btn.bind(on_press=lambda dt: self.start_timer())
        self.slice = 1

        self.graph = self.ECG(self.slice)
        self.breathe_rate = BreatheRate()
        self.muscle_tone = MuscleTone()

        self.layer_2_id.add_widget(self.breathe_rate)
        self.layer_2_id.add_widget(self.muscle_tone)
        self.layer_2_id.add_widget(self.graph)

        self.reflexes = Reflexes()
        self.skin_coloring = SkinColoring()
        self.results = Results()

        self.widget_array = [self.breathe_rate, self.muscle_tone, self.reflexes, self.skin_coloring]
        self.layer_3_id.add_widget(self.reflexes)
        self.layer_3_id.add_widget(self.skin_coloring)
        self.layer_3_id.add_widget(self.results)

    def update_results(self):
        self.results.update()

    def update_graph(self):
        self.slice += 1
        self.layer_2_id.remove_widget(self.graph)
        self.graph = self.ECG(self.slice)
        self.layer_2_id.add_widget(self.graph)

    def start_timer(self):
        self.timer.start_timer()
        self.layer_1_id.remove_widget(self.start_btn)
        self.stop_btn = Button(text='Стоп')
        self.stop_btn.bind(on_press=lambda dt: self.stop_timer())
        self.layer_1_id.add_widget(self.stop_btn)
        self.event = Clock.schedule_interval(lambda dt: self.update_graph(), .1)

    def stop_timer(self):
        self.timer.stop_timer()
        self.layer_1_id.remove_widget(self.stop_btn)
        self.reset_btn = Button(text='Обнулить')
        self.layer_1_id.add_widget(self.reset_btn)
        self.event.cancel()
        self.reset_btn.bind(on_press=lambda dt: self.reset_timer())

    def reset_timer(self):
        self.timer.reset_timer()
        self.layer_1_id.remove_widget(self.reset_btn)
        self.start_btn = Button(text="Старт")
        self.layer_1_id.add_widget(self.start_btn)
        self.start_btn.bind(on_press=lambda dt: self.start_timer())
        self.event.cancel()
        self.slice = -1
        self.update_graph()

    def reset_data(self):
        if App.get_running_app().apgar_current >= 7:
            with self.canvas.before:
                Color(0, 1, 0, 1)  # green; colors range from 0-1 instead of 0-255
                self.rect = Rectangle(size=self.size, pos=self.pos)
            for widget in self.widget_array:
                widget.reset_data()
            Clock.schedule_once(lambda dt: self.restore_bg(), .5)
        else:
            with self.canvas.before:
                Color(1, 0, 0, 1)  # green; colors range from 0-1 instead of 0-255
                self.rect = Rectangle(size=self.size, pos=self.pos)
            Clock.schedule_once(lambda dt: self.change_screen_to_reanimation(), .5)

    def restore_bg(self):
        with self.canvas.before:
            Color(0, 0, 0, 1)  # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=self.size, pos=self.pos)

    def change_screen_to_reanimation(self):
        App.get_running_app().sm.current ='reanimation_screen'

    def ECG(self, cur_slice):
        if cur_slice == 0:
            plt.clf()
        ar = [0,0,.1,.2,.3,.4,.4,.3,.2,.15,.1,
                  0,0,0
                  -.5,-1,
                  0,2.5,-1,0,
                  0,0,0,
                  .4,.5,.6,.7,.7,.7,.6,.5,.4,
                  0,0,0,
                  ]
        if cur_slice >= len(ar):
            cur_ar = ar*(cur_slice // len(ar))
            cur_ar += ar[:cur_slice % len(ar)]
        else:
            cur_ar = ar[:cur_slice]
        plt.plot(cur_ar)
        plt.ylabel('мВ')

        return FigureCanvasKivyAgg(plt.gcf())

class Separator:

    def __init__(self) -> None:
        super().__init__()
        self.rgba = 0.7, 0.7, 0.7, 1
        self.size_hint = 1, 0.025

