from kivy.properties import StringProperty, ObjectProperty
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from functools import partial

import trackhandling


class Gaston(BoxLayout):
    description_text = StringProperty("This program can generate an edited version of the Gaston song from the 1991 "
                                      "Disney film Beauty and the Beast, randomly or based on user's selection.")

    default_text = StringProperty("When I was a LAD I ate FOUR DOZEN EGGS every morning to help me get LARGE,\n "
                                  "And now that I'm GROWN I eat FIVE DOZEN EGGS so I'm roughly the size of a BARGE!")

    preview = ObjectProperty(None)

    def play_callback(self, track, *args):
        trackhandling.play_track(track)

    def change_choice(self, num, obj):
        app = MDApp.get_running_app()
        app.choices[num] = trackhandling.string_dict_rev[obj.text]

    def get_preview(self):
        app = MDApp.get_running_app()
        self.preview.text = str(trackhandling.to_string(*app.choices))

    def generate(self):
        app = MDApp.get_running_app()
        track, text = trackhandling.make_track(*app.choices)
        self.preview.text = str(text)
        Clock.schedule_once(partial(self.play_callback, track))

    def randomize(self):
        track, text = trackhandling.randomize(same_num=True)
        self.preview.text = str(text)
        Clock.schedule_once(partial(self.play_callback, track))

    def same_word_lyrics(self):
        track, text = trackhandling.same_word()
        self.preview.text = str(text)
        Clock.schedule_once(partial(self.play_callback, track))


class GastonApp(MDApp):
    choices = trackhandling.original
    noun_values = list(trackhandling.string_dict.values())[:5]
    number_values = list(trackhandling.string_dict.values())[-2:]

    def build(self):
        return Gaston()


if __name__ == '__main__':
    GastonApp().run()
