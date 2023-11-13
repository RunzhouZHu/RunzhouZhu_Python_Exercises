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