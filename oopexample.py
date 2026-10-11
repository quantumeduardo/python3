class Robot:
    def __init__(self, name, age, internaltemperature):
        self.name = name
        self.age = age
        self.internaltemperature = 0.0

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def init_hardware(self):
        print("Initializing hardware...")

    def print_info(self):
        self.greet()
        self.init_hardware()
        print(f"Internal temperature: {self.internaltemperature}")
        print("End of robot information.")

my_robot = Robot("R2D2", 30, 5)

my_robot2 = Robot("C3PO", 25, 3)

my_robot.print_info()
my_robot2.print_info()