from Vehicles import Vehicles
from Cars import Car
from Bikes import Bike
from Plans import Plane
from Trains import Train

color = input("Enter color: ")
model = input("Enter model: ")
wheels = int(input("Enter num of wheels: "))
year = int(input("Enter year: "))


def vald(y):
    while year > 2022:
        y = int(input("Invalid year\nEnter valid year: "))
        if y < 2023:
            break
    return y


vald(year)
v1 = Car(color, model, wheels, vald(year))
print(v1)
