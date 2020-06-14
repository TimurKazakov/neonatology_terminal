from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
import datetime

class Timer(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.seconds = App.get_running_app().seconds
        self.text = str(datetime.timedelta(seconds=self.seconds))
        self.event = None

    def start_timer(self):
        self.event = Clock.schedule_interval(lambda dt: self.update_text(), 1)

    def update_text(self):
        self.seconds += 1
        self.text = str(datetime.timedelta(seconds=self.seconds))
        if self.seconds == 60:
            App.get_running_app().sm.get_screen('main_screen').reset_data()

    def stop_timer(self):
        self.event.cancel()

    def reset_timer(self):
        self.text = '0:00:00'
        self.seconds = 0
        self.event = None
