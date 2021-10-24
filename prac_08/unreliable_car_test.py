from prac_08.unreliable_car import UnreliableCar


brum = UnreliableCar('Brum', 100, 40)
for i in range(5):
    brum.drive(30)
    print(brum)
