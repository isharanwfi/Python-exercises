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

new_car = Car("ABC-123", 142)

new_car.accelerate(+30)
new_car.accelerate(+70)
new_car.accelerate(+50)
print("Current Speed of the car after accelerations:", new_car.current_speed, "km/h")


new_car.accelerate(-200)
print("Current Speed of the car after emergency brake:", new_car.current_speed, "km/h")
