"""
CP1404 prac_07
Kivy program to convert miles to km
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class ConvertMilesKm(App):
    """ Kivy App for converting miles to km """
    output_text = StringProperty()

    def build(self):
        self.title = 'Convert miles to km'
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output_text = 'Temp Text'
        return self.root


ConvertMilesKm().run()
