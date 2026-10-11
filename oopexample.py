class Robot:                                                    #this is a class called Robot
    def __init__(self, name, age, internaltemperature):         #this is a constructor method that initializes the attributes of the class Robot
        self.name = name                                        #this is an instance variable that stores the name of the robot
        self.age = age                                          #this is an instance variable that stores the age of the robot   
        self.internaltemperature = 0.0                          #this is an instance variable that stores the internal temperature of the robot

    def greet(self):                                                               #method that prints a greeting message with the robot's name and age                 
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")      #f-string is used to format the string with the robot's name and age

    def init_hardware(self):                                                        #method that initializes the hardware of the robot and prints a message indicating that the hardware is being initialized
        print("Initializing hardware...")                           

    def print_info(self):                                                           #method that prints the robot's information by calling the greet and init_hardware methods, and printing the internal temperature    
        self.greet()                                                                
        self.init_hardware()                                                            
        print(f"Internal temperature: {self.internaltemperature}")
        print("End of robot information.")

# my_robot = Robot("R2D2", 30, 5)

# my_robot2 = Robot("C3PO", 25, 3)

# my_robot.print_info()
# my_robot2.print_info()    

Robot("R2D2", 30, 5).greet()            #this creates an instance of the Robot class with the name "R2D2", age 30, and internal temperature 5, and calls the greet method to print a greeting message - different methods can be called on the same instance of the class, and each method can access the instance variables of the class.