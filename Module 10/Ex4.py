import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        self.current_speed = self.current_speed + change_of_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance = self.travelled_distance + (self.current_speed * hours)


class Race:
    def __init__(self, name, distance, car_list):
        self.name = name
        self.distance = distance
        self.cars = car_list

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print("\nRegistration\tMax Speed\tFinal Speed\tDistance (km)")
        print("=============================================================")
        for car in self.cars:
            print(f"{car.registration_number}\t\t{car.maximum_speed}\t\t{car.current_speed}\t\t{car.travelled_distance:.1f}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


participating_cars = []


for i in range(1, 11):
    reg_number = "ABC-" + str(i)
    max_speed = random.randint(100, 200)
    new_car = Car(reg_number, max_speed)
    participating_cars.append(new_car)


race = Race("Grand Demolition Derby", 8000, participating_cars)
hours_elapsed = 0


while not race.race_finished():
    race.hour_passes()
    hours_elapsed = hours_elapsed + 1
    
   
    if hours_elapsed % 10 == 0:
        print(f"\n--- Hour {hours_elapsed} Leaderboard ---")
        race.print_status()


print(f"\nRace finished after {hours_elapsed} hours!")
race.print_status()
