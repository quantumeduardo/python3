
class Robot:                                                    #this is a class called Robot
    def __init__(self, name, age, internaltemperature, arm_length = None):         #this is a constructor method that initializes the attributes of the class Robot
        self.name = name                                        #this is an instance variable that stores the name of the robot
        self.age = age                                          #this is an instance variable that stores the age of the robot   
        self.internaltemperature = internaltemperature          #this is an instance variable that stores the internal temperature of the robot
        self.arm_length = arm_length                           #this is an instance variable that stores the arm length of the robot
        

    def greet(self):                                                               #method that prints a greeting message with the robot's name and age                 
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")      #f-string is used to format the string with the robot's name and age

    def init_hardware(self):                                                        #method that initializes the hardware of the robot and prints a message indicating that the hardware is being initialized
        print("Initializing hardware...")
        print("Hardware initialized.")
        print(f"Internal temperature: {self.internaltemperature}")
  

    def print_info(self):
                                                         #method that prints the robot's information by calling the greet and init_hardware methods, and printing the internal temperature    
        self.greet()
        print(f"Age: {self.age}")
        self.init_hardware()
        if self.arm_length is not None:
            print(f"Arm length: {self.arm_length}")

        print("End of robot information.")
        


