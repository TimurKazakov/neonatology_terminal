import speech_recognition as sr
from kivy.app import App


class VoiceControl():

    def __init__(self) -> None:
        super().__init__()
        self.r = sr.Recognizer()
        self.items = dict()
        self.command = ""
        self.item = ""

    def start_recognition(self):
        command = ''
        parsedCommands = ''
        while (1):
            with sr.Microphone() as source:
                print("Speak:")
                audio = self.r.listen(source)
            try:
                speechString = self.r.recognize_google(audio)
                parsedCommands = speechString.split(" ")
                print(parsedCommands)
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

            if len(parsedCommands) == 2:
                command = parsedCommands[0].lower()
                status = parsedCommands[1].lower()
            if len(parsedCommands) == 3:
                command = parsedCommands[0].lower() + ' ' + parsedCommands[1].lower()
                status = parsedCommands[2].lower()

            if command == "program":
                if status == "start":
                    App.get_running_app().sm.get_screen('main_screen').start_timer()
                if status == "stop":
                    App.get_running_app().sm.get_screen('main_screen').stop_timer()

            elif command == "reflexes":
                if status == 'normal':
                    pass
                if status == 'weak':
                    pass
                if status == 'absent':
                    pass

            elif command == "skin":
                if status == 'normal':
                    pass
                if status == 'weak':
                    pass
                if status == 'absent':
                    pass

            elif command == "muscles ":
                if status == 'normal':
                    pass
                if status == 'weak':
                    pass
                if status == 'absent':
                    pass

