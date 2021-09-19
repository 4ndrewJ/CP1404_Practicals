"""
CP1404 prac_07
Kivy program to convert miles to km
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


MILE_TO_KM_FACTOR = 1.60934


class ConvertMilesKm(App):
    """ Kivy App for converting miles to km """
    output_text = StringProperty()

    def build(self):
        self.title = 'Convert miles to km'
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output_text = 'Temp Text'
        return self.root

    def handle_increment(self, text_input, increment):
        """
        Takes text TextInput object and increments it's value by the increment
        """
        text_input.text = str(float(text_input.text) + increment)

    def handle_calculate(self, text_input):
        self.output_text = str(float(text_input.text) * MILE_TO_KM_FACTOR)


ConvertMilesKm().run()
