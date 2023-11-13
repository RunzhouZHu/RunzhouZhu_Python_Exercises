import random


class Car:
    def __init__(self, registrationNumber, maximumSpeed):
        self.registrationNumber = registrationNumber
        self.maximumSpeed = maximumSpeed
        self.currentSpeed = 0
        self.travelledDistance = 0

    def accelerate(self, speed):
        self.currentSpeed = self.currentSpeed + speed
        if self.currentSpeed < 0:
            self.currentSpeed = 0
        elif self.currentSpeed > self.maximumSpeed:
            self.currentSpeed = self.maximumSpeed

    def drive(self, time):
        self.travelledDistance = self.travelledDistance + self.currentSpeed * time


class Race:
    def __init__(self, name, distance, carNumber):
        self.name = name
        self.distance = distance
        self.carList = []
        for i in range(carNumber):
            self.carList.append(Car('ABC-' + str(i + 1), random.randint(100, 200)))

    def hour_passed(self, t):
        print(f"It's the {t} hour.")
        for car in self.carList:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        for car in self.carList:
            print(
                f"The {car.registrationNumber} car runs at {car.currentSpeed}km/h and has run {car.travelledDistance}km")

    def race_finished(self):
        for car in self.carList:
            if car.travelledDistance > self.distance:
                print(f"The winner is {car.registrationNumber}")
                return True


newRace = Race('Grand Demolition Derby', 8000, 10)
t = 0
while True:
    t += 1
    newRace.hour_passed(t)
    newRace.print_status()
    if newRace.race_finished() == True:
        break
