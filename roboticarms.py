from robot import Robot

#child class of Robot
class RoboticArm(Robot):
    def __init__(self, name, age, internaltemperature, arm_length): 
        super().__init__(name, age, internaltemperature) #super calls the constructor of the parent class (Robot)
        self.arm_length = arm_length
        # print(f"Arm length: {self.arm_length}")
       
    def pick_object(self, x , y):
        print("pick an object at coordinates:", "(" + str(x) + "," + str(y) + ")")
        print("Object picked successfully.")
        
    def place_object(self, x, y):
        print("place an object at coordinates:", "(" + str(x) + "," + str(y) + ")")
        print("Object placed successfully.")

        #inheritance - class from another class to "help to be"
        #composition - building complex objects by combining simpler ones "to have"


#using composition
class PackagingSolution:

    def __init__(self, Robotic_Armleft, Robotic_Armright):
        self.robotic_armleft = Robotic_Armleft  
        self.robotic_armright = Robotic_Armright
        


    def package(self, pickx, picky, middlex, middley, placex, placey):
        self.robotic_armleft.pick_object(pickx, picky)
        self.robotic_armleft.place_object(middlex, middley)
        self.robotic_armright.pick_object(middlex, middley)
        self.robotic_armright.place_object(placex, placey)

