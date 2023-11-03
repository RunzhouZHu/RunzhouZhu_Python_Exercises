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

# Main program
newCar = Car('ABC-123', 142)
print(f"The registration number is {newCar.registrationNumber}, the maximum speed is {newCar.maximumSpeed}km/h.")

newCar.accelerate(30)
print(f"The car is {newCar.currentSpeed}km/h now.")

newCar.accelerate(70)
print(f"The car is {newCar.currentSpeed}km/h now.")

newCar.accelerate(50)
print(f"The car is {newCar.currentSpeed}km/h now.")

newCar.accelerate(-200)
print(f"The car is {newCar.currentSpeed}km/h now.")