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
        self.output_text = '0.0'
        return self.root

    def handle_increment(self, text_input, increment):
        """
        Takes text TextInput object and increments it's value by the increment
        """
        text_input.text = str(float(self.get_valid_value(text_input)) + increment)

    def handle_calculate(self, text_input):
        """ Calculates the equivalent km to the input miles """
        self.output_text = f'{float(self.get_valid_value(text_input)) * MILE_TO_KM_FACTOR:.3f}'

    def get_valid_value(self, text_input):
        """ Checks if the input is valid otherwise returns 0.0 """
        try:
            return float(text_input.text)
        except ValueError:
            return 0.0


ConvertMilesKm().run()
