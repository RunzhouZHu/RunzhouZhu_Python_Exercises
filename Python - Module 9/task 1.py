class Car:
    def __init__(self, registrationNumber, maximumSpeed):
        self.registrationNumber = registrationNumber
        self.maximumSpeed = maximumSpeed
        self.currentSpeed = 0
        self.travelledDistance = 0


# Main program
newCar = Car('ABC-123', 142)
print(f"The registration number is {newCar.registrationNumber}, the maximum speed is {newCar.maximumSpeed}km/h.")