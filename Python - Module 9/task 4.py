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
import random

cars = []
for i in range(10):
    cars.append(Car('ABC-'+str(i+1), random.randint(100,200)))
    
t = 0
while True:
    t = t + 1
    print(f"It's the {t} hour.")
    for car in cars:
        car.accelerate(random.randint(-10,15))
        car.drive(1)
        print(f"{car.registrationNumber}-----{car.currentSpeed}km/h-----{car.travelledDistance}km")
    if car.travelledDistance >= 10000:
        break
        
for car in cars:
    print(f"The winner is {car.registrationNumber}, it runs {car.travelledDistance}km.")