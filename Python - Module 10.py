
# Question 1
class Elevator:
    def __init__(self, bottomFloor, topFloor):
        self.floor = bottomFloor
        self.bottomFloor = bottomFloor
        self.topFloor = topFloor

    def go_to_floor(self, inputFloor):
        print(f"You are at floor {self.floor}.")
        while True:
            if inputFloor > self.floor:
                self.floor_up()
                print(f"Going up, you are at {self.floor} now.")
            elif inputFloor < self.floor:
                self.floor_down()
                print(f"Going down, you are at {self.floor} now.")
            else:
                print(f"You arrived the floor.")
                break

    def floor_up(self):
        self.floor += 1

    def floor_down(self):
        self.floor -= 1


# Main program
newElevator = Elevator(1, 10)
newElevator.go_to_floor(5)
newElevator.go_to_floor(1)


########################################
# Question 2
class Elevator:
    def __init__(self, bottomFloor, topFloor):
        self.floor = bottomFloor
        self.bottomFloor = bottomFloor
        self.topFloor = topFloor

    def go_to_floor(self, inputFloor):
        print(f"You are at floor {self.floor}.")
        while True:
            if inputFloor > self.floor:
                self.floor_up()
                print(f"Going up, you are at {self.floor} now.")
            elif inputFloor < self.floor:
                self.floor_down()
                print(f"Going down, you are at {self.floor} now.")
            else:
                print(f"You arrived the floor.")
                break

    def floor_up(self):
        self.floor += 1

    def floor_down(self):
        self.floor -= 1


class Building:
    def __init__(self, bottomFloor, topFloor, numberOfElevators):
        self.elevators = []
        for elevator in range(numberOfElevators):
            self.elevators.append(Elevator(bottomFloor, topFloor))

    def run_elevator(self, inputFloor):
        for elevator in self.elevators:
            elevator.go_to_floor(inputFloor)


# Main program
newBuilding = Building(1, 10, 3)
newBuilding.run_elevator(6)


########################################
# Question 3
class Elevator:
    def __init__(self, bottomFloor, topFloor):
        self.floor = bottomFloor
        self.bottomFloor = bottomFloor
        self.topFloor = topFloor

    def go_to_floor(self, inputFloor):
        print(f"You are at floor {self.floor}.")
        while True:
            if inputFloor > self.floor:
                self.floor_up()
                print(f"Going up, you are at {self.floor} now.")
            elif inputFloor < self.floor:
                self.floor_down()
                print(f"Going down, you are at {self.floor} now.")
            else:
                print(f"You arrived the floor.")
                break

    def floor_up(self):
        self.floor += 1

    def floor_down(self):
        self.floor -= 1


class Building:
    def __init__(self, bottomFloor, topFloor, numberOfElevators):
        self.elevators = []
        for elevator in range(numberOfElevators):
            self.elevators.append(Elevator(bottomFloor, topFloor))

    def run_elevator(self, inputFloor):
        for elevator in self.elevators:
            elevator.go_to_floor(inputFloor)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(elevator.bottomFloor)


# Main program
newBuilding = Building(1, 10, 3)
newBuilding.run_elevator(7)
newBuilding.fire_alarm()

########################################
# Question 4
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
