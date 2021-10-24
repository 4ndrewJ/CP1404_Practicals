from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """ Specialised version of taxi with cost dependent on fanciness + flagfall cost"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return a string like a Taxi but with flagfall cost."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """ Add flagfall cost onto regular Taxi cost """
        return super().get_fare() + self.flagfall


