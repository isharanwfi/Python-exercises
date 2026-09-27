
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.kilometer_counter = 0

    def drive(self, hours):
        self.kilometer_counter += self.current_speed * hours

class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume

electric = ElectricCar("ABC-15", 180, 52.5)
gasoline = GasolineCar("ACD-123", 165, 32.3)

electric.current_speed = 120
gasoline.current_speed = 100

electric.drive(3)
gasoline.drive(3)

print(f"Electric Car ({electric.registration_number}) odometer: {electric.kilometer_counter} km")
print(f"Gasoline Car ({gasoline.registration_number}) odometer: {gasoline.kilometer_counter} km")
