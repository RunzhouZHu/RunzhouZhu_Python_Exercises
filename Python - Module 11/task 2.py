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


class ElectricCar(Car):
    def __init__(self, registrationNumber, maximumSpeed, batteryCapacity):
        super().__init__(registrationNumber, maximumSpeed)
        self.batteryCapacity = batteryCapacity


class GasolineCar(Car):
    def __init__(self, registrationNumber, maximumSpeed, tankVolume):
        super().__init__(registrationNumber, maximumSpeed)
        self.tankVolume = tankVolume


electricCar = ElectricCar('ABC-15', 180, 52.5)
gasolineCar = GasolineCar('ACD-123', 165, 32.3)

for i in range(3):
    electricCar.accelerate(random.randint(-10, 15))
    gasolineCar.accelerate(random.randint(-10, 15))
    electricCar.drive(1)
    gasolineCar.drive(1)
    print(f"The electric car runs at {electricCar.currentSpeed}km/h. It has run {electricCar.travelledDistance}km.")
    print(f"The gasoline car runs at {gasolineCar.currentSpeed}km/h. It has run {gasolineCar.travelledDistance}km.")
