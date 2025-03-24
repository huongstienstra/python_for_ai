class Car:
    max_speed = 120

    def __init__(self, make, model, color, speed = 0):
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed

    def accelerate(self, acceleration):
        if self.speed + acceleration <= Car.max_speed:
            self.speed += acceleration
        else:
            self.speed = Car.max_speed


    def get_speed(self):
        return self.speed


car1 = Car("Toyota", "Camry", "Blue")
car2 = Car("Honda", "Civic", "Red")


car1.accelerate(30)
car2.accelerate(120)


print(f"{car1.make} {car1.model} is currently at {car1.get_speed()} km/h")
print(f"{car2.make} {car2.model} is currently at {car2.get_speed()} km/h")

