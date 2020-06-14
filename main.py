import threading

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.widget import Widget
from screens.MainScreen import MainScreen
from screens.ReanimationScreen import ReanimationScreen
from VoiceControl import VoiceControl
from screens.ResultsScreen import ResultScreen


class NeonatologyApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gestation_period = 38
        self.weight = 3.243
        self.seconds = 55
        self.apgar_current = 0
        self.apgar_1 = 0
        self.apgar_5 = 0
        self.reflexes_apgar = 0
        self.skin_coloring_apgar = 0
        self.muscle_tone_apgar = 0
        self.breathe_apgar = 0
        self.heart_rate_apgar = 2
        self.change_field = ''

    def calc_apgar(self):
        summary = int(self.reflexes_apgar) + int(self.skin_coloring_apgar) + int(self.muscle_tone_apgar) + int(
            self.breathe_apgar) + self.heart_rate_apgar
        App.get_running_app().apgar_current = summary
        if self.seconds <= 60:
            App.get_running_app().apgar_1 = summary
        else:
            App.get_running_app().apgar_5 = summary

        self.sm.get_screen('main_screen').update_results()

    def update_log(self, text):
        self.sm.get_screen('reanimation_screen').update(text)

    def make_injection(self, medicine):
        self.sm.get_screen('reanimation_screen').make_injection(medicine)

    def update_child_info(self,):
        self.sm.get_screen('reanimation_screen').update_child_info()





    def build(self):
        return sm


if __name__ == '__main__':
    app = NeonatologyApp()
    sm = ScreenManager()
    app.sm = sm
    main_screen = MainScreen(name='main_screen')
    sm.add_widget(main_screen)
    reanimation_screen = ReanimationScreen(name='reanimation_screen')
    result_screen = ResultScreen(name='result_screen')
    sm.add_widget(reanimation_screen)
    sm.add_widget(result_screen)

    # sm.current ='reanimation_screen'

    app.voice_control = VoiceControl()
    threading.Thread(target=app.voice_control.start_recognition, daemon=True).start()
    app.run()
