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

# Main program
newCar = Car('ABC-123', 142)
print(f"The registration number is {newCar.registrationNumber}, the maximum speed is {newCar.maximumSpeed}km/h.")

newCar.travelledDistance = 2000
newCar.currentSpeed = 60
newCar.drive(1.5)
print(f"The travelled distance is {newCar.travelledDistance}.")