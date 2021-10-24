from prac_08.car import Car
from random import random


class UnreliableCar(Car):
    """ Specialised version of Car to include reliability"""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if random()*100 < self.reliability:
            return super().drive(distance)
        return 0
