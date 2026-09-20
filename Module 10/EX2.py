class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor = self.current_floor + 1
            print(f"Elevator is at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor = self.current_floor - 1
            print(f"Elevator is at floor {self.current_floor}")

    def go_to_floor(self, destination_floor):
        while self.current_floor < destination_floor:
            self.floor_up()
        while self.current_floor > destination_floor:
            self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = number_of_elevators
        self.elevators = []
        
        for i in range(number_of_elevators):
            new_elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(new_elevator)

    def run_elevator(self, elevator_number, destination_floor):

        print(f"\nRunning elevator #{elevator_number} to floor {destination_floor}")
       
        chosen_elevator = self.elevators[elevator_number]
        chosen_elevator.go_to_floor(destination_floor)

my_building = Building(1, 7, 3) 
my_building.run_elevator(0, 5)   
my_building.run_elevator(1, 3)   