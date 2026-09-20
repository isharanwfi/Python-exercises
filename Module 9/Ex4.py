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
        distance_driven = self.current_speed * hours

        self.travelled_distance = self.travelled_distance + distance_driven


car_list = []

for i in range(1, 11):
    reg_number = "ABC-" + str(i)
    max_speed = random.randint(100, 200)
    new_car = Car(reg_number, max_speed)
    car_list.append(new_car)

race_continues = True
while race_continues:
    for car in car_list:
     
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        
        car.drive(1)
        
        if car.travelled_distance >= 10000:
            race_continues = False

print("Registration\tMax Speed\tFinal Speed\tDistance (km)")
print("=" * 60)
for car in car_list:
    print(f"{car.registration_number}\t\t{car.maximum_speed}\t\t{car.current_speed}\t\t{car.travelled_distance:.1f}")

