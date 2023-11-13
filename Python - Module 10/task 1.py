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